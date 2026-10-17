import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Union, Any

try:
    from .config import INBOX_DIR
except ImportError:
    from config import INBOX_DIR

IMAGE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"
}

VIDEO_EXTENSIONS = {
    ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".3gp"
}

DOCUMENT_EXTENSIONS = {
    ".pdf", ".docx", ".doc", ".xlsx", ".xls", ".csv", ".txt", ".md",
    ".json", ".zip", ".rar", ".7z", ".pptx", ".ppt", ".xml", ".html", ".epub"
}

class InboxEngine:
    """Motor de gestión, clasificación y resguardo de la bandeja de entrada M.E.R.F.I."""

    @staticmethod
    def classify_file(file_path: Union[str, Path]) -> str:
        """Determina la subcarpeta de destino según la extensión del archivo."""
        ext = Path(file_path).suffix.lower()
        if ext in IMAGE_EXTENSIONS:
            return "Imagenes"
        elif ext in VIDEO_EXTENSIONS:
            return "Videos"
        return "Archivos"

    @classmethod
    def get_inbox_paths(cls, base_inbox: Path = INBOX_DIR) -> Dict[str, Path]:
        """Obtiene y garantiza las rutas de la bandeja de entrada."""
        sin_procesar = base_inbox / "SIN_PROCESAR"
        procesados = base_inbox / "Procesados"
        corruptos = base_inbox / "Corruptos"

        categories = ["Archivos", "Imagenes", "Videos"]
        for cat in categories:
            (sin_procesar / cat).mkdir(parents=True, exist_ok=True)
            (procesados / cat).mkdir(parents=True, exist_ok=True)
        corruptos.mkdir(parents=True, exist_ok=True)

        return {
            "sin_procesar": sin_procesar,
            "procesados": procesados,
            "corruptos": corruptos
        }

    @classmethod
    def sort_unprocessed_inbox(cls, base_inbox: Path = INBOX_DIR) -> Dict[str, List[str]]:
        """
        Escanea la raíz de SIN_PROCESAR por archivos sueltos depositados directamente
        y los clasifica de forma automática en Archivos/, Imagenes/ o Videos/.
        """
        paths = cls.get_inbox_paths(base_inbox)
        sin_procesar = paths["sin_procesar"]
        moved: Dict[str, List[str]] = {"Archivos": [], "Imagenes": [], "Videos": []}

        for item in sin_procesar.iterdir():
            if item.is_file() and item.name != ".gitkeep":
                category = cls.classify_file(item)
                target_dir = sin_procesar / category
                target_file = target_dir / item.name
                
                # Evitar colisión
                if target_file.exists():
                    target_file = target_dir / f"{item.stem}_copy{item.suffix}"

                shutil.move(str(item), str(target_file))
                moved[category].append(target_file.name)

        return moved

    @classmethod
    def archive_unprocessed(cls, base_inbox: Path = INBOX_DIR, category: Optional[str] = None) -> Dict[str, List[str]]:
        """
        Traslada los archivos de SIN_PROCESAR hacia Procesados/ en sus áreas correspondientes.
        Se invoca al procesar materiales o al cierre de sesión/terminal para mantener la bandeja limpia.
        """
        paths = cls.get_inbox_paths(base_inbox)
        sin_procesar = paths["sin_procesar"]
        procesados = paths["procesados"]

        categories = [category] if category else ["Archivos", "Imagenes", "Videos"]
        archived: Dict[str, List[str]] = {"Archivos": [], "Imagenes": [], "Videos": []}

        for cat in categories:
            src_dir = sin_procesar / cat
            dest_dir = procesados / cat
            if not src_dir.exists():
                continue

            for item in src_dir.iterdir():
                if item.is_file() and item.name != ".gitkeep":
                    target_file = dest_dir / item.name
                    if target_file.exists():
                        import time
                        ts = int(time.time())
                        target_file = dest_dir / f"{item.stem}_{ts}{item.suffix}"

                    shutil.move(str(item), str(target_file))
                    archived[cat].append(target_file.name)

        return archived

    @classmethod
    def audit_inbox(cls, base_inbox: Path = INBOX_DIR) -> Dict[str, Any]:
        """Audita el estado actual de la bandeja de entrada."""
        paths = cls.get_inbox_paths(base_inbox)
        sin_procesar = paths["sin_procesar"]
        procesados = paths["procesados"]

        audit_data: Dict[str, Any] = {
            "sin_procesar": {},
            "procesados": {},
            "total_pendientes": 0
        }

        for cat in ["Archivos", "Imagenes", "Videos"]:
            sp_files = [f.name for f in (sin_procesar / cat).iterdir() if f.is_file() and f.name != ".gitkeep"]
            pr_files = [f.name for f in (procesados / cat).iterdir() if f.is_file() and f.name != ".gitkeep"]
            audit_data["sin_procesar"][cat] = sp_files
            audit_data["procesados"][cat] = len(pr_files)
            audit_data["total_pendientes"] += len(sp_files)

        return audit_data

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "--audit"
    if action == "--sort":
        res = InboxEngine.sort_unprocessed_inbox()
        print(f"Archivos clasificados: {res}")
    elif action == "--archive":
        res = InboxEngine.archive_unprocessed()
        print(f"Archivos resguardados en Procesados: {res}")
    else:
        status = InboxEngine.audit_inbox()
        print("=== ESTADO DE BANDEJA M.E.R.F.I. ===")
        print(f"Pendientes en SIN_PROCESAR: {status['total_pendientes']}")
        for c, fls in status["sin_procesar"].items():
            print(f"  - {c}: {len(fls)} archivo(s)")

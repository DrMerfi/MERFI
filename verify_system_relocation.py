"""
Script de Verificación Pericial: Reubicación de Archivos de Sistema y Gobernanza en 00_Sistema/
Valida que la reubicación de:
- .env.example
- .gitignore
- AGENTS.md
- CLAUDE.md
- GEMINI.md
- LICENSE
- requirements.txt
no perjudique ninguna funcionalidad de la bóveda M.E.R.F.I.
"""

import os
import sys
import tempfile
import zipfile
import subprocess
from pathlib import Path

# Asegurar importación de módulos hermanos
ENGINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ENGINE_DIR))

from config import VAULT_DIR, SYSTEM_DIR, REPO_ROOT, DB_PATH, load_env_file
from memory_engine import MemoryEngine
from quality_framework import UQRLMetamodelAuditor, Ishikawa6MAnalyzer, PokaYokeGate, WebExplorationGate, DeepThinkingEngine

RELOCATED_FILES = [
    ".env.example",
    ".gitignore",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "LICENSE",
    "requirements.txt"
]

def test_1_file_locations():
    print("\n[PRUEBA 1/6] Comprobando ubicación física de archivos del sistema...")
    for f in RELOCATED_FILES:
        in_system = SYSTEM_DIR / f
        in_vault_root = VAULT_DIR / f
        assert in_system.exists(), f"FALLO: No existe {f} en 00_Sistema/"
        assert not in_vault_root.exists(), f"FALLO: {f} aún existe en la raíz de la bóveda."
        print(f"  -> {f}: OK (Ubicado en 00_Sistema/, ausente en raíz de bóveda)")
    
    # Comprobar que en la raíz de la bóveda solo queden carpetas y notas de usuario
    vault_root_files = [f.name for f in VAULT_DIR.iterdir() if f.is_file()]
    expected_root_notes = {"Inicio.md", "COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md", "PREGUNTAS_FRECUENTES.md"}
    assert set(vault_root_files) == expected_root_notes, f"Archivos inesperados en raíz de bóveda: {vault_root_files}"
    print(f"  -> Raíz de bóveda limpia con exactamente 3 notas maestras: {vault_root_files}")
    return True

def test_2_env_loading():
    print("\n[PRUEBA 2/6] Comprobando carga de variables de entorno desde 00_Sistema/.env...")
    test_env_file = SYSTEM_DIR / ".env.test_tmp"
    test_key = "MERFI_TEST_VAR_SYSTEM"
    test_val = "verified_100"
    
    try:
        test_env_file.write_text(f"{test_key}={test_val}\n", encoding="utf-8")
        load_env_file(test_env_file)
        loaded = os.environ.get(test_key)
        assert loaded == test_val, f"FALLO: No se cargó la variable de entorno ({loaded} != {test_val})"
        print(f"  -> Carga de entorno en 00_Sistema exitosa: {test_key}={loaded}")
    finally:
        if test_env_file.exists():
            test_env_file.unlink()
    return True

def test_3_fts5_indexing():
    print("\n[PRUEBA 3/6] Comprobando indexación FTS5 y búsqueda de directivas en 00_Sistema/...")
    engine = MemoryEngine(DB_PATH)
    indexed = engine.index_vault(VAULT_DIR)
    assert indexed > 0, "FALLO: No se indexó ninguna nota."
    print(f"  -> Total de notas indexadas en frío: {indexed}")
    
    # Verificar búsqueda de directivas ahora ubicadas en 00_Sistema
    for term in ["AGENTS", "CLAUDE", "Poka-Yoke"]:
        res = engine.search_notes(term)
        assert len(res) > 0, f"FALLO: Búsqueda FTS5 de '{term}' sin resultados."
        print(f"  -> Búsqueda de '{term}': {len(res)} coincidencias (primera: {res[0]['path']})")
    return True

def test_4_smoke_test_integration():
    print("\n[PRUEBA 4/6] Ejecutando suite integral de motor determinista (smoke_test.py)...")
    from smoke_test import run_smoke_test
    assert run_smoke_test() is True, "FALLO: smoke_test() no superó todas las suites."
    print("  -> Smoke test superado al 100% (7/7 suites).")
    return True

def test_5_repackaging_and_zip_integrity():
    print("\n[PRUEBA 5/6] Verificando empaquetado y aislamiento en MERFI_Starter_Kit_v1.0.zip...")
    zip_path = Path("MERFI_Starter_Kit_v1.0.zip").resolve()
    assert zip_path.exists(), f"FALLO: No existe el archivo {zip_path}"
            
    with zipfile.ZipFile(zip_path, 'r') as zf:
        namelist = zf.namelist()
        
    print(f"  -> Total de archivos en ZIP: {len(namelist)}")
    assert "README.md" in namelist, "FALLO: README.md debe estar fuera de Mi_Boveda/ en el ZIP."
    assert "Mi_Boveda/README.md" not in namelist, "FALLO: README.md no debe estar dentro de Mi_Boveda/."
    
    for rf in RELOCATED_FILES:
        expected_zip_path = f"Mi_Boveda/00_Sistema/{rf}"
        forbidden_zip_path = f"Mi_Boveda/{rf}"
        assert expected_zip_path in namelist, f"FALLO: Falta {expected_zip_path} en el ZIP."
        assert forbidden_zip_path not in namelist, f"FALLO: {forbidden_zip_path} no debe estar en la raíz de Mi_Boveda."
        print(f"  -> ZIP: {expected_zip_path} presente y verificado.")
        
    prohibited = [n for n in namelist if any(ext in n for ext in ['.bat', '.db', '.pyc', '__pycache__'])]
    assert len(prohibited) == 0, f"FALLO: Archivos prohibidos en ZIP: {prohibited}"
    print("  -> Cero archivos prohibidos (.bat, .db, .pyc, __pycache__) en el ZIP.")
    return True

def test_6_clean_extraction():
    print("\n[PRUEBA 6/6] Verificando descompresión limpia y ejecución en entorno aislado...")
    zip_path = Path("MERFI_Starter_Kit_v1.0.zip").resolve()
    with tempfile.TemporaryDirectory() as tmpdir:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(tmpdir)
        
        extracted_engine = Path(tmpdir) / "Mi_Boveda" / "00_Sistema" / "Engine" / "smoke_test.py"
        assert extracted_engine.exists(), f"No se encontró smoke_test.py en {extracted_engine}"
        
        res = subprocess.run([sys.executable, str(extracted_engine)], capture_output=True, text=True)
        assert res.returncode == 0, f"FALLO en ejecución tras descompresión: {res.stderr}"
        print("  -> Ejecución autónoma tras descompresión limpia superada con 100% de éxito.")
    return True

def run_all_tests():
    print("=================================================================")
    print("=== BANCO DE PRUEBAS DE REUBICACIÓN EN 00_Sistema/ (M.E.R.F.I.) ===")
    print("=================================================================")
    test_1_file_locations()
    test_2_env_loading()
    test_3_fts5_indexing()
    test_4_smoke_test_integration()
    test_5_repackaging_and_zip_integrity()
    test_6_clean_extraction()
    print("\n=================================================================")
    print("=== TODAS LAS PRUEBAS SUPERADAS EXITOSAMENTE (6/6 BANCOS AL 100%) ===")
    print("=================================================================")
    return True

if __name__ == "__main__":
    run_all_tests()

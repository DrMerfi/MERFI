import sqlite3
from pathlib import Path
try:
    from .config import DB_PATH, VAULT_DIR
except ImportError:
    from config import DB_PATH, VAULT_DIR

class MemoryEngine:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        """Inicializacion en frio (Cold-Start): crea tablas FTS5 si no existen."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Tabla de notas con busqueda de texto completo (FTS5)
            cursor.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts USING fts5(
                    path,
                    title,
                    content,
                    tokenize='porter unicode61'
                )
            """)
            # Tabla de memoria episódica / sesiones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sessions_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # Tabla de telemetría de calidad
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS quality_audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_id TEXT,
                    dimension TEXT,
                    score REAL,
                    verdict TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def index_vault(self, vault_path: Path = VAULT_DIR) -> int:
        """Escanea e indexa todos los archivos Markdown de la boveda en SQLite FTS5."""
        if not vault_path.exists():
            return 0

        indexed_count = 0
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Limpiar indice previo
            cursor.execute("DELETE FROM notes_fts")
            
            for md_file in vault_path.rglob("*.md"):
                try:
                    rel_path = str(md_file.relative_to(vault_path))
                    title = md_file.stem.replace("_", " ")
                    content = md_file.read_text(encoding="utf-8", errors="ignore")
                    
                    cursor.execute(
                        "INSERT INTO notes_fts(path, title, content) VALUES(?, ?, ?)",
                        (rel_path, title, content)
                    )
                    indexed_count += 1
                except Exception:
                    continue
            conn.commit()
        return indexed_count

    def search_notes(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Busqueda Full-Text Search de alta velocidad."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            # Sanitizar query para sintaxis FTS5 basica
            safe_query = '"' + query.replace('"', '""') + '"'
            try:
                cursor.execute(
                    "SELECT path, title, snippet(notes_fts, 2, '<b>', '</b>', '...', 10) "
                    "FROM notes_fts WHERE notes_fts MATCH ? ORDER BY rank LIMIT ?",
                    (safe_query, limit)
                )
                rows = cursor.fetchall()
                return [{"path": r[0], "title": r[1], "snippet": r[2]} for r in rows]
            except sqlite3.OperationalError:
                # Fallback en caso de caracteres especiales
                cursor.execute(
                    "SELECT path, title, substr(content, 1, 150) FROM notes_fts "
                    "WHERE content LIKE ? LIMIT ?",
                    (f"%{query}%", limit)
                )
                rows = cursor.fetchall()
                return [{"path": r[0], "title": r[1], "snippet": r[2]} for r in rows]

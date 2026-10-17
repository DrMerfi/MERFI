import os
from pathlib import Path

# Carga ligera de variables de entorno sin dependencias forzadas
def load_env_file(env_path: Path):
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())

# Rutas Relativas Dinamicas (Agnosticas al Sistema Operativo y Unidad de Disco)
ENGINE_DIR = Path(__file__).resolve().parent

# Soporte Universal de Ubicación:
# 1. Si Engine está dentro de 00_Sistema/Engine (Arquitectura Canónica)
if ENGINE_DIR.parent.name == "00_Sistema":
    VAULT_DIR = ENGINE_DIR.parent.parent
    REPO_ROOT = VAULT_DIR
# 2. Si Engine está en la raíz de la bóveda
elif (ENGINE_DIR.parent / "00_Sistema").exists():
    VAULT_DIR = ENGINE_DIR.parent
    REPO_ROOT = ENGINE_DIR.parent
# 3. Si Engine está fuera de la bóveda con subcarpeta Mi_Boveda
elif (ENGINE_DIR.parent / "Mi_Boveda").exists():
    VAULT_DIR = ENGINE_DIR.parent / "Mi_Boveda"
    REPO_ROOT = ENGINE_DIR.parent
elif (ENGINE_DIR.parent / "Vault_Template").exists():
    VAULT_DIR = ENGINE_DIR.parent / "Vault_Template"
    REPO_ROOT = ENGINE_DIR.parent
else:
    VAULT_DIR = ENGINE_DIR.parent
    REPO_ROOT = ENGINE_DIR.parent

# Directorios de la Boveda
SYSTEM_DIR = VAULT_DIR / "00_Sistema"
WORKING_MEM_FILE = SYSTEM_DIR / "01_Memoria_Trabajo" / "sesion_actual.md"
SHORT_TERM_DIR = SYSTEM_DIR / "02_Memoria_Corto_Plazo"
LONG_TERM_DIR = SYSTEM_DIR / "03_Memoria_Largo_Plazo"
INBOX_DIR = VAULT_DIR / "10_Entrada"
PROJECTS_DIR = VAULT_DIR / "20_Proyectos"
KNOWLEDGE_DIR = VAULT_DIR / "30_Conocimiento"

# Cargar archivo .env si existe (en 00_Sistema, en la raiz de la boveda o en el repo)
load_env_file(REPO_ROOT / ".env")
load_env_file(VAULT_DIR / ".env")
load_env_file(SYSTEM_DIR / ".env")

# Base de Datos SQLite FTS5 Local
DB_PATH = ENGINE_DIR / "merfi.db"

# Configuracion de LLM
LLM_PROVIDER = os.getenv("MERFI_LLM_PROVIDER", "gemini").lower()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

# Hiperparametros Metacognitivos
TEMPERATURE = float(os.getenv("MERFI_TEMPERATURE", "0.2"))
CONFIDENCE_THRESHOLD = float(os.getenv("MERFI_CONFIDENCE_THRESHOLD", "0.85"))

# Configuracion Discreta de Gobernanza y Razonamiento (Ejecucion Silenciosa en Segundo Plano)
# El usuario no tiene que lidiar con estos parametros: el sistema los autogestiona
AUTO_DEEP_THINKING = os.getenv("MERFI_AUTO_DEEP_THINKING", "true").lower() in ("true", "1", "yes")
DEEP_THINKING_BRANCHES = int(os.getenv("MERFI_DEEP_BRANCHES", "5"))
FAST_PATH_TEMP = float(os.getenv("MERFI_FAST_TEMP", "0.3"))
DEEP_PATH_TEMP = float(os.getenv("MERFI_DEEP_TEMP", "0.0"))
AUTO_POKA_YOKE = os.getenv("MERFI_AUTO_POKA_YOKE", "true").lower() in ("true", "1", "yes")
REQUIRE_HUMAN_GATE_WEB = os.getenv("MERFI_HUMAN_GATE_WEB", "true").lower() in ("true", "1", "yes")
AUTO_UQRL_GOVERNANCE = os.getenv("MERFI_AUTO_UQRL", "true").lower() in ("true", "1", "yes")
AUTO_ISHIKAWA = os.getenv("MERFI_AUTO_ISHIKAWA", "true").lower() in ("true", "1", "yes")

# Nivel de Exposicion al Usuario (Modo Amigable por Defecto)
# False = Respuestas claras, directas y amigables (la maquinaria trabaja discretamente de fondo)
# True = Expone desgloses tecnicos, ramas MCTS y metricas solo si el usuario lo solicita explicitamente
VERBOSE_TECHNICAL_DETAILS = os.getenv("MERFI_VERBOSE_DETAILS", "false").lower() in ("true", "1", "yes")

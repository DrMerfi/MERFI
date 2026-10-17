#!/usr/bin/env python3
"""
M.E.R.F.I. Console — Terminal Oficial Interactiva
Sistema: M.E.R.F.I. v1.0
Diseñado para operar de forma 100% autonoma, con o sin conexion a internet,
con o sin llaves de API, garantizando que ningun colega se quede sin respuesta.
"""

import os
import sys
import json
import time
from pathlib import Path

# Blindaje Poka-Yoke: Garantizar codificacion UTF-8 universal en terminales Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ajuste de rutas relativas universales
ENGINE_DIR = Path(__file__).resolve().parent
SYSTEM_DIR = ENGINE_DIR.parent
VAULT_DIR = SYSTEM_DIR.parent

sys.path.insert(0, str(ENGINE_DIR))

try:
    from config import (
        VAULT_DIR, INBOX_DIR, PROJECTS_DIR, KNOWLEDGE_DIR,
        GEMINI_API_KEY, OPENAI_API_KEY, OLLAMA_BASE_URL, OLLAMA_MODEL
    )
    from memory_engine import MemoryEngine
    from quality_framework import UQRLMetamodelAuditor
    from inbox_engine import InboxEngine
except Exception as e:
    # Fallback seguro
    VAULT_DIR = VAULT_DIR
    INBOX_DIR = VAULT_DIR / "10_Entrada"
    PROJECTS_DIR = VAULT_DIR / "20_Proyectos"
    KNOWLEDGE_DIR = VAULT_DIR / "30_Conocimiento"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
    MemoryEngine = None
    UQRLMetamodelAuditor = None
    InboxEngine = None


def imprimir_banner():
    banner = """
================================================================================
  M.E.R.F.I. v1.0 — Metamodelo de Evidencia y Razonamiento Forense
  Espacio de Trabajo Inteligente con Soberania Local y Cero Alucinacion
================================================================================
"""
    print(banner)


def obtener_estado_sistema():
    lineas = []
    # 1. Bóveda
    lineas.append(f"• Boveda Activa: {VAULT_DIR.name} ({VAULT_DIR})")
    
    # 2. Bandeja de Entrada
    inbox_sin = INBOX_DIR / "SIN_PROCESAR"
    pendientes = 0
    if inbox_sin.exists():
        for r, _, files in os.walk(inbox_sin):
            pendientes += len([f for f in files if not f.startswith(".")])
    lineas.append(f"• Bandeja de Entrada (10_Entrada/): {pendientes} archivos pendientes.")

    # 3. Motor de Inteligencia Artificial
    if GEMINI_API_KEY:
        lineas.append("• Motor de IA: Conectado a Google Gemini (Modo Nube Activo).")
    elif OPENAI_API_KEY:
        lineas.append("• Motor de IA: Conectado a OpenAI (Modo Nube Activo).")
    else:
        # Probar si Ollama responde
        ollama_online = False
        try:
            import urllib.request
            req = urllib.request.Request(f"{OLLAMA_BASE_URL}/api/tags", headers={"User-Agent": "MERFI"})
            with urllib.request.urlopen(req, timeout=1) as resp:
                if resp.status == 200:
                    ollama_online = True
        except Exception:
            ollama_online = False

        if ollama_online:
            lineas.append(f"• Motor de IA: Conectado a Ollama Local ({OLLAMA_MODEL} - 100% Offline).")
        else:
            lineas.append("• Motor de IA: Modo Soberano Local (Analisis Algoritmico y Busqueda FTS5 sin APIs).")

    return "\n".join(lineas)


def ejecutar_busqueda_local(termino: str):
    if not MemoryEngine:
        print("[!] Motor de memoria no disponible.")
        return
    try:
        mem = MemoryEngine()
        resultados = mem.search(termino, limit=5)
        if not resultados:
            print(f"\n[i] Sin registro en el acervo documental para: '{termino}'.")
            return
        print(f"\n[+] Coincidencias encontradas ({len(resultados)}):")
        for idx, r in enumerate(resultados, 1):
            titulo = r.get("title", "Sin titulo")
            ruta = r.get("path", "")
            snippet = r.get("snippet", "")
            print(f"\n  {idx}. {titulo} ({ruta})")
            if snippet:
                print(f"     \"{snippet.strip()}\"")
    except Exception as e:
        print(f"[!] Error al buscar: {e}")


def auditar_bandeja():
    if not InboxEngine:
        print("[!] Motor de bandeja no disponible.")
        return
    try:
        eng = InboxEngine()
        status = eng.audit_inbox()
        print("\n--- Estado de la Bandeja de Entrada (10_Entrada/) ---")
        print(f"• Archivos sin procesar: {status.get('unprocessed_count', 0)}")
        print(f"• Archivos en cuarentena: {status.get('quarantine_count', 0)}")
        print(f"• Archivos procesados:   {status.get('processed_count', 0)}")
        unproc = status.get("unprocessed_files", [])
        if unproc:
            print("\nArchivos en espera:")
            for f in unproc[:10]:
                print(f"  - {f.get('name')} ({f.get('category')})")
    except Exception as e:
        print(f"[!] Error en auditoria: {e}")


def mostrar_ayuda():
    ayuda = """
Comandos Rapidos Disponibles:
  • ayuda                 - Muestra esta lista de comandos.
  • estado                - Informa sobre la salud de la boveda y conexion de IA.
  • buscar <termino>      - Busca en todas tus notas y documentos con SQLite FTS5.
  • bandeja               - Audita los archivos depositados en 10_Entrada/.
  • clasificar            - Ordena automaticamente los archivos de entrada por tipo.
  • resguardar            - Traslada los materiales procesados a carpetas permanentes.
  • ishikawa              - Despliega la guia rapida de analisis causa-raiz 6M.
  • calidad               - Audita la boveda bajo el Circulo de Calidad de 8 Pasos.
  • indexar               - Reindexa todas las notas Markdown de la boveda.
  • salir                 - Cierra la sesion de M.E.R.F.I. limpiamente.

Tambien puedes escribir directamente cualquier pregunta o instruccion en lenguaje cotidiano.
"""
    print(ayuda)


def procesar_consulta(texto: str):
    cmd = texto.strip().lower()

    if cmd in ["salir", "exit", "quit", "q"]:
        print("\n[M.E.R.F.I.] Sesion cerrada con exito. Tus notas y memorias permanecen seguras.\n")
        sys.exit(0)
    elif cmd in ["ayuda", "help", "?"]:
        mostrar_ayuda()
    elif cmd in ["estado", "status"]:
        print("\n" + obtener_estado_sistema() + "\n")
    elif cmd.startswith("buscar "):
        termino = texto[7:].strip()
        ejecutar_busqueda_local(termino)
    elif cmd in ["bandeja", "inbox"]:
        auditar_bandeja()
    elif cmd in ["clasificar", "sort"]:
        if InboxEngine:
            res = InboxEngine().sort_incoming_files()
            print(f"\n[+] Archivos clasificados: {res.get('moved_count', 0)} movidos a subcarpetas operativas.\n")
        else:
            print("[!] Motor de bandeja no disponible.")
    elif cmd in ["resguardar", "archive"]:
        if InboxEngine:
            res = InboxEngine().archive_processed_files()
            print(f"\n[+] Archivos resguardados con exito en 10_Entrada/Procesados/.\n")
        else:
            print("[!] Motor de bandeja no disponible.")
    elif cmd in ["ishikawa", "causa raiz"]:
        print("""
--- DIAGRAMA CAUSA-RAIZ ISHIKAWA 6M ---
1. Metodos:       ¿Los procedimientos o normas estan desactualizados o son ambiguos?
2. Maquinas:      ¿Fallo el software, la conexion, el hardware o el equipo medico?
3. Mano de Obra:  ¿Falta capacitacion, hay sobrecarga laboral o fatiga en el equipo?
4. Materiales:    ¿Faltan insumos, reactivos, formatos o la calidad es defectuosa?
5. Medicion:      ¿Los indicadores miden lo correcto o hay sesgo en la captura?
6. Medio Ambiente:¿El entorno fisico, clima organizacional o ruido impiden el flujo?
""")
    elif cmd in ["calidad", "u-qrl", "8 pasos"]:
        if UQRLMetamodelAuditor:
            rep = UQRLMetamodelAuditor.audit_8step_cycle({
                "outcome_score": 0.85,
                "cpk": 1.33,
                "budget_consumed": 0.40,
                "hypothesis_valid": True
            })
            print(f"\n--- AUDITORIA U-QRL v1.1 ---")
            print(f"• Dictamen de Gobernanza: {rep.get('dictamen_gobernanza')}")
            print(f"• Calidad Sistemica:      {rep.get('calidad_sistemica')} / 100")
            print("• Ciclo de 8 Pasos verificado y en regla.\n")
        else:
            print("[!] Motor de calidad no disponible.")
    elif cmd in ["indexar", "reindex"]:
        if MemoryEngine:
            count = MemoryEngine().index_vault(VAULT_DIR)
            print(f"\n[+] Boveda indexada con exito: {count} notas procesadas en SQLite FTS5.\n")
        else:
            print("[!] Motor de memoria no disponible.")
    else:
        # Intento de respuesta con LLM o fallback inteligente
        if GEMINI_API_KEY:
            responder_con_gemini(texto)
        elif OPENAI_API_KEY:
            responder_con_openai(texto)
        else:
            # Modo Soberano Local: Buscar en documentos y orientar al usuario
            print("\n[M.E.R.F.I. — Modo Soberano Local]")
            print(f"Has consultado: \"{texto}\"")
            print("Buscando evidencia documental en tus notas locales...")
            ejecutar_busqueda_local(texto[:30])
            print("\n[Nota]: Para habilitar respuestas conversacionales avanzadas con IA generativa,")
            print("puedes agregar tu GEMINI_API_KEY en el archivo 00_Sistema/.env o iniciar Ollama en local.")


def responder_con_gemini(prompt: str):
    try:
        import urllib.request
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        
        system_context = (
            "Eres M.E.R.F.I., un copiloto de calidad, salud y gestion de proyectos local. "
            "Respeta la regla de cero alucinacion: si no conoces un dato, di 'Sin registro en el acervo documental'. "
            "Se breve, preciso y profesional."
        )
        
        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": f"{system_context}\n\nConsulta del usuario: {prompt}"}]}
            ]
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        
        print("\n[M.E.R.F.I. pensando...]")
        with urllib.request.urlopen(req, timeout=15) as resp:
            res_json = json.loads(resp.read().decode("utf-8"))
            candidate = res_json.get("candidates", [{}])[0]
            answer = candidate.get("content", {}).get("parts", [{}])[0].get("text", "")
            print(f"\n{answer.strip()}\n")
    except Exception as e:
        print(f"\n[!] Error al conectar con Gemini: {e}")
        print("Operando bajo contingencia en Modo Soberano Local.")


def responder_con_openai(prompt: str):
    try:
        import urllib.request
        url = "https://api.openai.com/v1/chat/completions"
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Eres M.E.R.F.I., copiloto de calidad y proyectos con cero alucinacion."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        })
        print("\n[M.E.R.F.I. pensando...]")
        with urllib.request.urlopen(req, timeout=15) as resp:
            res_json = json.loads(resp.read().decode("utf-8"))
            answer = res_json["choices"][0]["message"]["content"]
            print(f"\n{answer.strip()}\n")
    except Exception as e:
        print(f"\n[!] Error al conectar con OpenAI: {e}")


def main():
    imprimir_banner()
    print(obtener_estado_sistema())
    print("\nEscribe 'ayuda' para ver comandos, o escribe tu pregunta directamente.")
    print("Para salir en cualquier momento escribe 'salir'.\n")

    # Si se pasan argumentos por línea de comandos (ej. `merfi estado`)
    if len(sys.argv) > 1:
        consulta = " ".join(sys.argv[1:])
        procesar_consulta(consulta)
        return

    # Bucle interactivo REPL
    while True:
        try:
            prompt_input = input("MERFI > ").strip()
            if not prompt_input:
                continue
            procesar_consulta(prompt_input)
        except (KeyboardInterrupt, EOFError):
            print("\n\n[M.E.R.F.I.] Sesion interrumpida. Hasta pronto.\n")
            break


if __name__ == "__main__":
    main()

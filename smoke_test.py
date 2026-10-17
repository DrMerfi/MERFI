import sys
from pathlib import Path

# Asegurar importacion relativa
sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_engine import MemoryEngine
from quality_framework import UQRLMetamodelAuditor, Ishikawa6MAnalyzer, PokaYokeGate
from config import VAULT_DIR, DB_PATH

def run_smoke_test():
    print("=== INICIANDO SMOKE TEST DE M.E.R.F.I. CORE ===")
    
    # 1. Prueba de Memoria y Cold-Start
    print("\n[1/4] Probando inicializacion en frio y motor FTS5...")
    engine = MemoryEngine(DB_PATH)
    indexed = engine.index_vault(VAULT_DIR)
    print(f"  -> Archivos de la boveda indexados con exito: {indexed}")
    assert indexed > 0, "Fallo: No se indexo ningun archivo de la boveda plantilla."
    
    # Busqueda FTS
    results = engine.search_notes("Poka-Yoke")
    print(f"  -> Coincidencias para 'Poka-Yoke': {len(results)}")
    assert len(results) > 0, "Fallo: La busqueda FTS5 no arrojo resultados."
    print(f"  -> Primera coincidencia: {results[0]['path']}")

    # 2. Prueba de Ishikawa 6M
    print("\n[2/4] Probando analisis de causa-raiz Ishikawa 6M...")
    ish = Ishikawa6MAnalyzer()
    ish.add_factor("Metodos", "Falta de procedimiento estandarizado en la entrega.")
    ish.add_factor("Metodos", "Ausencia de lista de verificacion previa.")
    ish.add_factor("Materiales_Datos", "Datos de entrada incompletos en el formulario.")
    summary = ish.generate_diagnostic_summary()
    print(f"  -> Total de factores: {summary['total_factores_identificados']}")
    print(f"  -> Dimension dominante: {summary['dimension_dominante']}")
    assert summary["dimension_dominante"] == "Metodos", "Fallo en dimension dominante de Ishikawa."

    # 3. Prueba de Metamodelo U-QRL v1.1 y Circulo de Calidad de 8 Pasos
    print("\n[3/6] Probando Circulo de Calidad U-QRL v1.1 (8 Pasos y Compuerta Cuatripartita)...")
    # Caso 1: Proceso excelente -> Automatizar
    v1 = UQRLMetamodelAuditor.evaluate_decision_gate(outcome_score=0.92, cpk=1.45, budget_consumed=0.70, hypothesis_valid=True)
    assert "AUTOMATIZAR" in v1
    print(f"  -> Caso Nominal: {v1}")
    
    # Caso 2: Costos agotados sin resultados -> Kill Switch
    v2 = UQRLMetamodelAuditor.evaluate_decision_gate(outcome_score=0.40, cpk=0.80, budget_consumed=1.0, hypothesis_valid=True)
    assert "ABANDONAR" in v2
    print(f"  -> Caso Critico: {v2}")

    # Caso 3: Auditoria completa del ciclo de 8 pasos
    ciclo_auditado = UQRLMetamodelAuditor.audit_8step_cycle({
        "outcome_score": 0.88,
        "cpk": 1.40,
        "budget_consumed": 0.65,
        "hypothesis_valid": True,
        "resilience": 1.2,
        "process_waste": 0.05,
        "cycle_latency": 0.8
    })
    assert ciclo_auditado["total_pasos"] == 8
    assert len(ciclo_auditado["ciclo_auditado"]) == 8
    print(f"  -> Círculo de Calidad de 8 Pasos auditado exitosamente (Calidad Sistémica: {round(ciclo_auditado['calidad_sistemica'], 2)})")

    # 4. Prueba de Poka-Yoke y Metrica Empirica
    print("\n[4/5] Probando compuertas Poka-Yoke...")
    valido = PokaYokeGate.validate_inbox_file("reporte_ventas.csv", 1024)
    invalido = PokaYokeGate.validate_inbox_file("archivo_vacio.csv", 0)
    assert valido is True and invalido is False, "Fallo en validacion Poka-Yoke de entrada."
    
    confianza = PokaYokeGate.calculate_empirical_confidence(verified_variables=18, required_variables=20)
    print(f"  -> Cobertura de evidencia calculada: {confianza}%")
    assert confianza == 90.0, "Fallo en calculo de confianza empirica."

    # 5. Prueba de Cero Alucinacion y Compuerta Humana de Red
    print("\n[5/5] Probando Compuerta Humana para Exploracion en la Red...")
    from quality_framework import WebExplorationGate
    web_gate = WebExplorationGate()
    assert web_gate.can_access_web() is False, "Fallo: la compuerta de red debe nacer cerrada por defecto."
    
    req = web_gate.request_permission("Tasa de inflacion anual 2026")
    print(f"  -> Solicitud formal de permiso: {req['mensaje_al_usuario']}")
    assert req["estado"] == "BLOQUEADO_COMPUERTA_HUMANA"
    assert "Sin registro en el acervo documental local" in req["mensaje_al_usuario"]
    assert web_gate.can_access_web() is False

    # Simulacion: El usuario otorga permiso
    web_gate.grant_permission(human_approval=True)
    assert web_gate.can_access_web() is True, "Fallo al abrir compuerta tras aprobacion humana."
    print("  -> Compuerta desbloqueada con autorizacion explicita del usuario.")

    # 6. Prueba de Asignación de Cómputo Dinámico y DeepThinking
    print("\n[6/6] Probando Asignador de Cómputo y Ruta Deep-Thinking...")
    from quality_framework import DeepThinkingEngine, ComputeDepth

    # Caso A: Pregunta cotidiana -> Fast-Path
    route_fast = DeepThinkingEngine.allocate_compute_route("Hola, ¿cómo estás hoy?")
    print(f"  -> Pregunta cotidiana: {route_fast['route']} ({route_fast['depth_level']})")
    assert route_fast["route"] == "FAST_PATH"
    assert route_fast["branches_explored"] == 1

    # Caso B: Tarea altamente demandante -> Deep-Thinking
    prompt_complex = "Ejecuta una auditoría integral U-QRL v1.1 y análisis de causa raíz Ishikawa 6M para diagnosticar el cuello de botella y optimizar el presupuesto del proyecto."
    route_deep = DeepThinkingEngine.allocate_compute_route(prompt_complex)
    print(f"  -> Tarea demandante: {route_deep['route']} ({route_deep['depth_level']})")
    print(f"     Score de complejidad: {route_deep['complexity_score']} | Ramas MCTS: {route_deep['branches_explored']}")
    assert route_deep["route"] == "DEEP_PATH"
    assert route_deep["branches_explored"] == 5
    assert route_deep["sampling_temperature"] == 0.0
    assert route_deep["tree_search_active"] is True

    # 7. Prueba de Gestión de Bandeja Multimodal y Resguardo Automático
    print("\n[7/7] Probando Bandeja Multimodal (Archivos, Imágenes, Videos) y Resguardo Automático...")
    from inbox_engine import InboxEngine
    from config import INBOX_DIR

    # A. Verificación de carpetas estructurales
    for sub in ["Archivos", "Imagenes", "Videos"]:
        assert (INBOX_DIR / "SIN_PROCESAR" / sub).exists(), f"Falta carpeta SIN_PROCESAR/{sub}"
        assert (INBOX_DIR / "Procesados" / sub).exists(), f"Falta carpeta Procesados/{sub}"
    print("  -> Subcarpetas estructurales (Archivos, Imagenes, Videos) verificadas en SIN_PROCESAR y Procesados.")

    # B. Clasificación automática por extensión
    assert InboxEngine.classify_file("diagrama_flujo.png") == "Imagenes"
    assert InboxEngine.classify_file("banner.jpg") == "Imagenes"
    assert InboxEngine.classify_file("presentacion.mp4") == "Videos"
    assert InboxEngine.classify_file("clase.mkv") == "Videos"
    assert InboxEngine.classify_file("tesis.docx") == "Archivos"
    assert InboxEngine.classify_file("datos.xlsx") == "Archivos"
    print("  -> Clasificación determinista por tipo de archivo validada.")

    # C. Auditoría de bandeja
    audit = InboxEngine.audit_inbox(INBOX_DIR)
    assert "sin_procesar" in audit and "procesados" in audit
    print(f"  -> Auditoría de bandeja en frío completada (Pendientes: {audit['total_pendientes']}).")

    print("\n=== SMOKE TEST SUPERADO CON 100% DE EXITO (7/7 SUITES) ===")
    return True

if __name__ == "__main__":
    run_smoke_test()


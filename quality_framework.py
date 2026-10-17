from typing import Dict, List, Any

class UQRLMetamodelAuditor:
    """Implementacion ejecutable del Metamodelo Universal U-QRL v1.1 (Donabedian 2.0 y Circulo de Calidad de 8 Pasos)."""

    EIGHT_STEPS = [
        {"paso": 1, "nombre": "Cuestionar Requisitos", "fase": "Fase 0: Primeros Principios", "clave": "cuestionar_requisitos"},
        {"paso": 2, "nombre": "Poda Activa y De-implementacion", "fase": "Fase 0: Primeros Principios", "clave": "poda_activa"},
        {"paso": 3, "nombre": "Alineacion de Modelos Mentales", "fase": "Fase 0: Primeros Principios", "clave": "modelos_mentales"},
        {"paso": 4, "nombre": "Configuracion de Sustrato (Estructura 2.0)", "fase": "Nucleo Aumentado", "clave": "sustrato_estructura"},
        {"paso": 5, "nombre": "Flujo Esbelto y Barreras Poka-Yoke (Proceso 2.0)", "fase": "Nucleo Aumentado", "clave": "flujo_esbelto"},
        {"paso": 6, "nombre": "Auto-Reflexion Agéntica y Cero Alucinacion", "fase": "Nucleo Aumentado", "clave": "auto_reflexion"},
        {"paso": 7, "nombre": "Telemetria de Rendimiento y Outcome (Resultado 2.0)", "fase": "Nucleo Aumentado", "clave": "telemetria_outcome"},
        {"paso": 8, "nombre": "Compuerta Cuatripartita de Decision", "fase": "Gobernanza Final", "clave": "decision_gate"}
    ]

    @classmethod
    def audit_8step_cycle(cls, project_eval: Dict[str, Any]) -> Dict[str, Any]:
        """
        Audita el ciclo completo de los 8 pasos para un proyecto y emite el dictamen consolidado.
        """
        outcome = float(project_eval.get("outcome_score", 0.0))
        cpk = float(project_eval.get("cpk", 1.0))
        budget_consumed = float(project_eval.get("budget_consumed", 0.0))
        hypothesis_valid = bool(project_eval.get("hypothesis_valid", True))
        
        gate_decision = cls.evaluate_decision_gate(outcome, cpk, budget_consumed, hypothesis_valid)

        pasos_auditados = []
        for step in cls.EIGHT_STEPS:
            num = step["paso"]
            nombre = step["nombre"]
            fase = step["fase"]
            clave = step["clave"]
            
            estado = "SUPERADO"
            if num <= 3 and not hypothesis_valid:
                estado = "REQUIERE_REVISION"
            elif num == 4 and budget_consumed > 0.9 and outcome < 0.5:
                estado = "DEFICIENTE"
            elif num == 8:
                estado = gate_decision.split(" — ")[0]
                
            pasos_auditados.append({
                "paso": num,
                "nombre": nombre,
                "fase": fase,
                "estado": estado
            })

        return {
            "metamodelo": "U-QRL v1.1",
            "total_pasos": 8,
            "ciclo_auditado": pasos_auditados,
            "dictamen_gobernanza": gate_decision,
            "calidad_sistemica": cls.calculate_systemic_quality(
                outcome_utility=outcome,
                resilience=float(project_eval.get("resilience", 1.0)),
                process_waste=float(project_eval.get("process_waste", 0.1)),
                cycle_latency=float(project_eval.get("cycle_latency", 1.0))
            )
        }

    @staticmethod
    def calculate_systemic_quality(outcome_utility: float, resilience: float, process_waste: float, cycle_latency: float) -> float:
        """
        Calculo de Calidad Sistémica:
        (Outcome * Resiliencia) / (Desperdicio * Latencia)
        """
        denominator = max(process_waste * cycle_latency, 0.001)
        return (outcome_utility * resilience) / denominator

    @staticmethod
    def evaluate_decision_gate(outcome_score: float, cpk: float, budget_consumed: float, hypothesis_valid: bool) -> str:
        """
        Compuerta Cuatripartita de Decision (Paso 8 U-QRL v1.1):
        1. AUTOMATIZAR & ESCALAR: Outcome >= 0.85 y Cpk >= 1.33
        2. CALIBRAR: Outcome entre 0.60 y 0.84 (variacion de causa comun)
        3. PIVOTAR: Hipotesis base refutada pero el fin estrategico se mantiene
        4. ABANDONAR (KILL SWITCH): Consumo >= 100% y Outcome < 0.60
        """
        if budget_consumed >= 1.0 and outcome_score < 0.60:
            return "ABANDONAR (KILL SWITCH) — Extirpar proyecto para evitar falacia de costos hundidos."
        if not hypothesis_valid:
            return "PIVOTAR — Hipótesis refutada; re-alinear modelos mentales (Fase 0)."
        if outcome_score >= 0.85 and cpk >= 1.33:
            return "AUTOMATIZAR & ESCALAR — Proceso estabilizado; proceder a estandarización."
        return "CALIBRAR — Variación dentro de límites de causa común; realizar ajustes locales."


class Ishikawa6MAnalyzer:
    """Diagnostico Pericial de Causa-Raiz Universal (6M)."""

    DIMENSIONS = [
        "Metodos",
        "Mano_de_Obra",
        "Maquinas_Software",
        "Materiales_Datos",
        "Medicion",
        "Medio_Ambiente"
    ]

    def __init__(self):
        self.factors: Dict[str, List[str]] = {d: [] for d in self.DIMENSIONS}

    def add_factor(self, dimension: str, description: str):
        if dimension in self.factors:
            self.factors[dimension].append(description)
        else:
            raise ValueError(f"Dimension no valida. Debe ser una de: {self.DIMENSIONS}")

    def generate_diagnostic_summary(self) -> Dict[str, Any]:
        total_factors = sum(len(f) for f in self.factors.values())
        dominant_dimension = max(self.factors.items(), key=lambda x: len(x[1]))[0] if total_factors > 0 else "Ninguna"
        
        return {
            "total_factores_identificados": total_factors,
            "dimension_dominante": dominant_dimension,
            "distribucion_6m": {k: len(v) for k, v in self.factors.items()},
            "detalle_factores": self.factors
        }

class PokaYokeGate:
    """Compuertas Deterministas Anti-Error."""

    @staticmethod
    def validate_inbox_file(file_path_str: str, file_bytes_len: int) -> bool:
        """Poka-Yoke de Entrada: rechaza archivos vacios o de extension desconocida."""
        if file_bytes_len == 0:
            return False
        valid_extensions = {".md", ".txt", ".pdf", ".csv", ".json", ".xlsx"}
        return any(file_path_str.lower().endswith(ext) for ext in valid_extensions)

    @staticmethod
    def calculate_empirical_confidence(verified_variables: int, required_variables: int) -> float:
        """Metrica determinista de cobertura de evidencia (0 a 100%)."""
        if required_variables == 0:
            return 100.0
        return round((verified_variables / required_variables) * 100.0, 2)

class WebExplorationGate:
    """Compuerta Humana Obligatoria para Exploracion Externa en la Red."""

    def __init__(self):
        self.is_authorized: bool = False
        self.pending_reason: str = ""

    def request_permission(self, missing_data_description: str) -> Dict[str, Any]:
        """Bloquea la consulta externa y genera la peticion formal al usuario."""
        self.is_authorized = False
        self.pending_reason = missing_data_description
        return {
            "estado": "BLOQUEADO_COMPUERTA_HUMANA",
            "mensaje_al_usuario": (
                f"Sin registro en el acervo documental local para: '{missing_data_description}'. "
                "¿Autorizas realizar una exploracion en la red externa para localizar esta informacion?"
            ),
            "requiere_confirmacion_humana": True
        }

    def grant_permission(self, human_approval: bool) -> bool:
        """Desbloquea o mantiene cerrado el acceso a herramientas de red."""
        self.is_authorized = bool(human_approval)
        return self.is_authorized

    def can_access_web(self) -> bool:
        """Comprueba si la compuerta humana esta abierta."""
        return self.is_authorized

from enum import Enum

class ComputeDepth(str, Enum):
    LEVEL_1_DIRECT = "Fast-Path (1 Paso / Interacción Directa y Baja Latencia)"
    LEVEL_2_BALANCED = "Balanced-Deep (3 Ramas de Pensamiento / Reflexión Intermedia)"
    LEVEL_3_DEEP_THINKING = "Exhaustive-DeepThinking (5 Ramas MCTS + Poda Unipaso + Temperatura 0.0)"

class DeepThinkingEngine:
    """
    Motor de Razonamiento Profundo y Asignador de Cómputo Dinámico (Test-Time Compute).
    Detecta automáticamente la demanda cognitiva de la tarea y enruta la inferencia hacia:
    - Fast-Path: Preguntas cotidianas, saludos, consultas rápidas.
    - Deep-Thinking: Tareas altamente demandantes (análisis de causa-raíz, optimización, auditoría U-QRL,
      diseño de arquitectura, matemáticas, modelos financieros, contratos o diagnósticos complejos).
    """

    HIGH_DEMAND_TERMS = [
        "ishikawa", "causa raiz", "causa-raiz", "u-qrl", "donabedian", "auditoria",
        "optimizacion", "primeros principios", "poka-yoke", "cuello de botella",
        "estrategia", "falla", "defecto", "desviacion", "presupuesto", "financiero",
        "roi", "cpk", "seis sigma", "seis-sigma", "lean", "arquitectura", "reestructuracion",
        "contrafactual", "what-if", "simulacion", "matriz de decision", "evaluar proyecto"
    ]

    CRITICAL_RISK_TERMS = [
        "kill switch", "abandonar proyecto", "perdida critica", "fraude", "demanda legal",
        "incumplimiento contractual", "colapso", "quiebra", "vulnerabilidad critica"
    ]

    @classmethod
    def allocate_compute_route(cls, prompt_text: str) -> Dict[str, Any]:
        p_lower = prompt_text.lower()
        words = p_lower.split()
        word_count = len(words)

        is_high_demand = any(term in p_lower for term in cls.HIGH_DEMAND_TERMS)
        is_critical_risk = any(term in p_lower for term in cls.CRITICAL_RISK_TERMS)

        # Cálculo de Score de Complejidad [0.0 a 1.0]
        score = 0.10
        if word_count > 15:
            score += 0.20
        if word_count > 40:
            score += 0.20
        if is_high_demand:
            score += 0.35
        if is_critical_risk:
            score += 0.45

        score = min(1.0, round(score, 2))

        if score >= 0.65 or is_critical_risk:
            return {
                "route": "DEEP_PATH",
                "depth_level": ComputeDepth.LEVEL_3_DEEP_THINKING.value,
                "complexity_score": score,
                "branches_explored": 5,
                "sampling_temperature": 0.0,
                "top_p": 0.05,
                "tree_search_active": True,
                "unipass_pruning_active": True,
                "rationale": "Tarea altamente demandante o riesgo crítico: ruta Deep-Thinking activada con 5 ramas MCTS, poda unipaso de hipótesis débiles y temperatura determinista (0.0)."
            }
        elif score >= 0.35 or is_high_demand:
            return {
                "route": "BALANCED_PATH",
                "depth_level": ComputeDepth.LEVEL_2_BALANCED.value,
                "complexity_score": score,
                "branches_explored": 3,
                "sampling_temperature": 0.2,
                "top_p": 0.8,
                "tree_search_active": True,
                "unipass_pruning_active": False,
                "rationale": "Complejidad analítica media: ruta balanceada con exploración de 3 ramas de hipótesis y temperatura controlada (0.2)."
            }
        else:
            return {
                "route": "FAST_PATH",
                "depth_level": ComputeDepth.LEVEL_1_DIRECT.value,
                "complexity_score": score,
                "branches_explored": 1,
                "sampling_temperature": 0.3,
                "top_p": 0.9,
                "tree_search_active": False,
                "unipass_pruning_active": False,
                "rationale": "Consulta cotidiana o directa: ruta Fast-Path de respuesta inmediata en 1 paso."
            }

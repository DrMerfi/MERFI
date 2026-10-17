---
tipo: directiva_sistema
codigo: DIR-COMPUTE-004
sistema: M.E.R.F.I. 1.0
nombre: Directiva de Asignación de Cómputo Dinámico y Razonamiento Profundo (DeepThinking)
version: 1.0.0
---

# Directiva de Asignación de Cómputo Dinámico y Razonamiento Profundo (DeepThinking)

## 1. Propósito y Principio Rector
El sistema M.E.R.F.I. no procesa todas las solicitudes con el mismo consumo de cómputo. Para optimizar la latencia y la profundidad analítica, el motor implementa **Asignación Dinámica de Cómputo en Tiempo de Inferencia (*Test-Time Compute Allocation*)**:
- Las interacciones cotidianas se resuelven de forma ágil e instantánea (**Fast-Path**).
- Las actividades de alta exigencia metodológica, técnica o financiera activan automáticamente la **Ruta de Razonamiento Profundo (*Deep-Thinking Path*)**.

---

## 2. Los Tres Niveles de Profundidad Cognitiva

| Nivel | Denominación Técnica | Ramas Exploradas | Muestreo y Temperatura | Cuándo se Activa |
| :--- | :--- | :---: | :---: | :--- |
| **Nivel 1** | **Fast-Path (Directo)** | 1 paso directo | Temp: 0.3 / Top-P: 0.9 | Saludos, consultas de agenda, resúmenes rápidos, navegación de notas. |
| **Nivel 2** | **Balanced-Deep (Reflexivo)** | 3 ramas de hipótesis | Temp: 0.2 / Top-P: 0.8 | Preguntas de proyectos con múltiples variables o consultas estructuradas. |
| **Nivel 3** | **Exhaustive Deep-Thinking** | 5 ramas MCTS | Temp: 0.0 (Determinista) | Auditorías U-QRL, diagnósticos Ishikawa 6M, cuellos de botella, modelos financieros, contratos y riesgos críticos. |

---

## 3. Criterios de Activación Automática de la Ruta Deep-Thinking

La ruta Deep-Thinking se dispara sin intervención manual cuando el sistema detecta:
1. **Palabras Clave de Alta Demanda:** Términos como *ishikawa*, *causa raíz*, *u-qrl*, *donabedian*, *auditoría*, *optimización*, *poka-yoke*, *cuello de botella*, *financiero*, *presupuesto*, *roi*, *cpk*, *seis sigma*, *contrafactual*, *simulación* o *evaluar proyecto*.
2. **Condiciones de Riesgo Crítico:** Términos de decisión irreversible como *kill switch*, *abandonar proyecto*, *pérdida crítica*, *vulnerabilidad* o *incumplimiento*.
3. **Complejidad Textual:** Solicitudes densas con más de 40 palabras o que involucran la correlación cruzada de múltiples documentos.

---

## 4. Algoritmo Interno de la Ruta Deep-Thinking (MCTS y Poda Unipaso)

Al entrar en la ruta Deep-Thinking, M.E.R.F.I. ejecuta el siguiente ciclo determinista:

```text
[ Entrada Compleja ] 
       │
       ▼
[ Generación de 5 Hipótesis Alternativas ] (Ramas MCTS)
       │
       ▼
[ Verificación de Respaldo Documental Local ] (Cotejo contra bóveda)
       │
       ▼
[ Regla de Poda Unipaso ] -> Descarta ramas sin sustento o con sesgo
       │
       ▼
[ Selección de Hipótesis Ganadora ] (Mayor función de recompensa)
       │
       ▼
[ Emisión en Formato Doble Bloque ] (Resolución Directa + Desglose Metodológico)
```

1. **Generación Multirrama:** No se compromete con la primera respuesta probabilística. Genera 5 ángulos de solución o diagnóstico.
2. **Cotejo con Evidencia:** Evalúa qué rama tiene sustento en las notas de `10_Entrada/`, `20_Proyectos/` y `30_Conocimiento/`.
3. **Regla de Poda Unipaso:** Elimina cualquier rama que especule o carezca de base documental verificable.
4. **Respuesta Verificada:** Emite la conclusión ganadora con su métrica de confianza empírica real.

---

## 5. Invariante de Operación Discreta (Gobernanza Silenciosa por Defecto)

Para garantizar que la bóveda sea intuitiva y amigable para cualquier persona:
1. **Cero Fricción de Configuración:** Todas las salvaguardas (asignación dinámica de cómputo, 5 ramas MCTS, filtros Poka-Yoke y compuertas U-QRL) se ejecutan de manera 100% automatizada e invisible en el fondo. El usuario no debe ajustar perillas, comandos ni parámetros técnicos.
2. **Salida Limpia y Amigable por Defecto:** La respuesta entregada al usuario es clara, concisa y orientada a la acción.
3. **Desglose Técnico Exclusivamente Bajo Demanda:** Los metadatos de computación (árbol de decisiones, ramas podadas, score numérico de complejidad y temperatura de muestreo) permanecen resguardados discretamente en el sistema y solo se desglosan en pantalla si el usuario lo solicita de forma expresa (por ejemplo: *"muéstrame el razonamiento técnico"* o *"explica las ramas descartadas"*).


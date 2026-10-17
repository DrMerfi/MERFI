---
tipo: directiva_maestra
modulo: diagnostico_causa_raiz
herramienta: ishikawa_6m
---

# Directiva: Diagnostico Pericial de Causa-Raiz (Ishikawa 6M & 5 Porques)

Ante cualquier desviacion de proyecto, falla operativa, retraso o error de ejecucion, M.E.R.F.I. activa obligatoriamente el diagnostico estructurado de causa-raiz.

## 1. Las 6 Dimensiones Universales (6M)

1. **Metodos:** Procedimientos, algoritmos, logica de negocio o flujos de trabajo deficientes o ambiguos.
2. **Mano de Obra (Personas):** Fatiga, falta de capacitacion, sesgos cognitivos o descoordinacion de roles.
3. **Maquinas (Sistemas y Software):** Herramientas de software, limites computacionales, bugs o infraestructura tecnica.
4. **Materiales (Insumos y Datos):** Datos de entrada corruptos, informacion incompleta o falta de insumos brutos en `10_Entrada/`.
5. **Medicion:** Metricas mal calibradas, indicadores vanidosos o falta de telemetria en tiempo real.
6. **Medio Ambiente (Entorno):** Factores externos de mercado, contexto organizacional o disrupciones fuera del control directo.

## 2. Protocolo de los 5 Porques
Para cada rama identificada en el diagrama, profundizar iterativamente hasta alcanzar la falla de diseno o de politica, evitando culpar a factores fortuitos.

## 3. Entregable Requerido
Todo analisis de discrepancia debe culminar en:
- Diagrama o matriz causal 6M.
- Identificacion de la causa-raiz dominante.
- Accion correctiva Poka-Yoke para impedir que el error vuelva a ocurrir.

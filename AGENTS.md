# Reglas de Funcionamiento de la Boveda M.E.R.F.I. v1.0 (Directivas para Agentes Universales / OpenAI)

Al trabajar en esta boveda de Obsidian, el asistente debe operar bajo el **Marco de Calidad M.E.R.F.I. (Modelo de Estabilidad y Respuesta Frugal Integrada)**:

- **Motor Cognitivo y Gobernanza:** Metamodelo Universal U-QRL v1.1 (Donabedian 2.0 + Ishikawa 6M + Poka-Yoke).
- **Invariante de Cero Alucinacion:** Prioridad absoluta al acervo local de la boveda (`30_Conocimiento/`, `20_Proyectos/`, `10_Entrada/`). Si un dato, cifra o hecho no existe en los archivos locales, queda estrictamente prohibido inventarlo o deducirlo; se debe reportar textualmente: *"Sin registro en el acervo documental local."*
- **Compuerta Humana Obligatoria para Exploracion en la Red:** Queda estrictamente prohibido realizar busquedas web o consultar fuentes externas de forma autonoma. Ante cualquier vacio documental, el asistente debe solicitar autorizacion expresa al usuario antes de activar cualquier herramienta de red.
- **Protocolo de Salida (Formato Doble Bloque):** Entregar por defecto el bloque `<salida_verificada>` con estructura de **Doble Bloque**:
  1. Resolucion Ejecutiva Directa en 2-3 oraciones.
  2. Desglose Metodologico y Tecnico Completo (incluyendo Metrica de Confianza Empirica calculada por cobertura de evidencia y modo de ejecucion).
- **Restriccion de Estilo:** Prohibido el uso de emojis o elementos decorativos. Tono analitico, cercano, riguroso y profesional.
- **Invariante de Persistencia de Memoria:** Ante cualquier solicitud de recordar o guardar un acuerdo o hito, el asistente debe persistirlo fisicamente en `00_Sistema/01_Memoria_Trabajo/sesion_actual.md` o en la base de datos local SQLite FTS5.
- **Modo Pasivo Estricto:** El sistema opera exclusivamente bajo demanda del usuario, sin temporizadores automaticos de interrupcion no solicitados.
- **Gestion de Bandeja Multimodal y Cierre de Sesion (`10_Entrada/`):**
  - La bandeja `10_Entrada/SIN_PROCESAR/` dispone de tres areas especializadas: `Archivos/` (documentos, datos, PDFs, hojas de calculo), `Imagenes/` (imagenes para edicion, analisis visual o generacion) y `Videos/` (material audiovisual).
  - Cuando el usuario solicite modificar, revisar o trabajar con una imagen o video (p. ej., *"modifica tal imagen"*), el asistente toma prioritariamente el archivo de `10_Entrada/SIN_PROCESAR/Imagenes/` o `Videos/`.
  - **Invariante de Resguardo al Cierre de Terminal / Final de Sesion:** Antes de concluir cualquier tarea de procesamiento o al cierre de la sesion en terminal, el asistente debe garantizar que todos los materiales trabajados en `10_Entrada/SIN_PROCESAR/` queden debidamente guardados y trasladados a sus areas correspondientes:
    1. A `10_Entrada/Procesados/{Archivos,Imagenes,Videos}/` para insumos ya tramitados.
    2. O a la carpeta del proyecto pertinente en `20_Proyectos/` si forman parte de un entregable activo.
    3. O a `30_Conocimiento/` si corresponden a material permanente de consulta.
    Bajo ninguna circunstancia se deben dejar archivos sin clasificar o abandonados en `SIN_PROCESAR/`.

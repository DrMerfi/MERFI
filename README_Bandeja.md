# Bandeja de Entrada Multimodal (Ingesta Poka-Yoke)

Este directorio gestiona la recepcion organizada de documentos, imagenes y videos para su procesamiento asistido por IA.

## Estructura de Flujo

### 1. `SIN_PROCESAR/` (Buzón de Recepción)
Deposita aquí los insumos brutos en su respectiva subcarpeta:
- **`Archivos/`:** Documentos, reportes, hojas de cálculo y bases de datos (PDF, CSV, Excel, Word, TXT, JSON, MD, ZIP).
- **`Imagenes/`:** Fotografías, diagramas, capturas e imágenes para análisis, edición o generación (PNG, JPG, JPEG, SVG, WebP, GIF). Si le pides a MERFI *"modifica tal imagen"*, colócala aquí.
- **`Videos/`:** Grabaciones, clips y material audiovisual para cortes, transcripción o revisión (MP4, MKV, MOV, AVI, WebM).

> *Nota:* Si depositas archivos directamente en la raíz de `SIN_PROCESAR/`, el motor interno los clasifica automáticamente en la subcarpeta que les corresponde según su extensión.

### 2. `Procesados/` (Resguardo Histórico y Orden)
Cuando el asistente procesa tus insumos o cuando cierras la terminal/sesión de trabajo, los archivos se trasladan de forma ordenada a sus carpetas correspondientes:
- **`Archivos/`:** Documentos ya leídos, indexados o resumidos.
- **`Imagenes/`:** Imágenes analizadas o modificadas.
- **`Videos/`:** Videos procesados o transcritos.

### 3. `Corruptos/` (Aislamiento Seguro)
Archivos con daño estructural o ilegibles se resguardan aquí con su respectivo diagnóstico para no contaminar la memoria del sistema.

---

> **Regla de Oro:** Mantener `SIN_PROCESAR/` siempre limpia. Al terminar cada tarea o al cerrar la terminal, todos los archivos trabajados se resguardan automáticamente en sus áreas correspondientes.

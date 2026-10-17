# Política de Seguridad y Privacidad de M.E.R.F.I.

## Compromiso con la Confidencialidad y Privacidad Médica

M.E.R.F.I. está diseñado específicamente para entornos asistenciales, epidemiológicos y de calidad hospitalaria donde se procesa información sensible sujeta a secreto profesional y normativas de protección de datos (como la Ley Federal de Protección de Datos Personales y la NOM-004-SSA3-2012 del Expediente Clínico en México).

### 1. Arquitectura Local-First (Aislamiento de Datos)
- **Cero Telemetría No Autorizada:** M.E.R.F.I. no envía métricas de uso, telemetría oculta ni documentos a servidores externos.
- **Indexación Local:** Las búsquedas semánticas y de texto completo se procesan exclusivamente en una base de datos local SQLite FTS5 (`merfi.db`) almacenada en el equipo del usuario.
- **Sin Retención en Nube:** Cuando se configuran APIs en la nube (como Google Gemini o OpenAI), las consultas se transmiten vía HTTPS cifrado únicamente al proveedor seleccionado, sin almacenamiento intermedio de terceros.

### 2. Manejo de Secretos y Llaves de API
- Las llaves de API nunca deben guardarse en archivos con seguimiento de versiones.
- El archivo `.gitignore` preconfigurado bloquea la subida accidental de archivos `.env`, bases de datos SQLite y expedientes clínicos colocados en la bandeja de entrada.

### 3. Reporte Responsable de Vulnerabilidades
Si detectas alguna vulnerabilidad de seguridad o potencial fuga de datos:
- Por favor no abras un issue público.
- Contacta directamente al equipo mantenedor a través del canal privado del repositorio en GitHub o por correo institucional para una mitigación coordinada.

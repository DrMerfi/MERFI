# Guía de Contribución a M.E.R.F.I.

¡Gracias por tu interés en contribuir a **M.E.R.F.I.** (*Metamodelo de Evidencia y Razonamiento Forense*)! Este proyecto busca empoderar a profesionales de la salud, calidad clínica, investigación e ingeniería con un espacio de trabajo inteligente, privado y con soberanía local absoluta.

---

## Principios de Diseño Innegociables

Toda contribución debe respetar los siguientes principios arquitectónicos:

1. **Soberanía Local y Privacidad (Local-First):**
   - El sistema debe ser 100% operativo sin conexión a internet ni requerir claves de API de pago.
   - Todo LLM o API externa es estrictamente opcional.
2. **Invariante de Cero Alucinación:**
   - Si un dato o documento no existe en el acervo documental del usuario, el sistema debe reportar "Sin registro en el acervo documental" y activar una compuerta humana antes de realizar consultas externas.
3. **Poka-Yoke y Filosofía Anti-Fricción:**
   - Las herramientas deben ser accesibles para personal de salud no técnico (médicos, enfermeras, auditores). Si una función requiere comandos complejos, debe encapsularse en un script de un solo clic o comando amigable.
4. **Preservación Documental:**
   - No modificar formatos de notas médicas o registros sensibles sin validación determinista.

---

## ¿Cómo Contribuir?

### 1. Reportar Errores o Sugerir Mejoras
- Abre un *Issue* en GitHub describiendo:
  - Comportamiento observado vs. comportamiento esperado.
  - Sistema operativo y versión de Python.
  - Pasos exactos para reproducir.

### 2. Proponer Nuevas Habilidades o Plantillas de Calidad
- Las plantillas de auditoría clínica, diagramas Ishikawa o rúbricas de calidad deben ubicarse en `Mi_Boveda/30_Conocimiento/` o documentarse en el metamodelo U-QRL.

### 3. Modificaciones de Código
1. Haz un *Fork* del repositorio.
2. Crea una rama descriptiva (`git checkout -b feature/nueva-herramienta`).
3. Realiza tus cambios asegurando compatibilidad con Python 3.10+.
4. Ejecuta las pruebas locales (`python 00_Sistema/Engine/smoke_test.py`).
5. Abre un *Pull Request* explicando el impacto y los beneficios de tu cambio.

---

## Licencia
Al contribuir al proyecto M.E.R.F.I., aceptas que tus contribuciones queden licenciadas bajo la **Licencia MIT**.

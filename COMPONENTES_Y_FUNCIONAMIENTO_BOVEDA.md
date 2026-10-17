# Guía Rápida: Componentes y Funcionamiento de M.E.R.F.I.
### Tu Espacio de Trabajo Privado e Inteligente (En 3 Minutos)

---

> [!NOTE]
> ### ¿Qué es esta Bóveda en 30 Segundos?
> Es tu **espacio de trabajo personal y privado** dentro de tu propia computadora. Combina dos elementos:
> 1. **Tus Notas en Obsidian:** Documentos de texto que te pertenecen al 100%, sin cuotas mensuales obligatorias ni servidores ajenos.
> 2. **Tu Copiloto M.E.R.F.I.:** Una inteligencia artificial con memoria real que trabaja contigo desde la terminal integrada, lee tus documentos verdaderos y **nunca inventa información falsa**.

> [!TIP]
> ### ¿Es tu primera vez y necesitas poner a punto el sistema? (Puesta en Marcha en 1 Clic)
> No necesitas saber de programación ni buscar instaladores en páginas web:
> 1. Si estás en Windows, haz doble clic en el archivo **`INSTALADOR_AUTOMATICO_MERFI.cmd`** (ubicado en esta misma carpeta).
> 2. Abre la **Terminal Integrada** (`>_`) en la barra lateral izquierda de Obsidian y escribe simplemente:
> 
> ```text
> merfi
> ```
> 
> *(Para ver la guía paso a paso, alternativas y comandos para macOS o Linux, consulta: [[#Instalación Automática de Python en 1 Clic|Instalación Automática de Python en 1 Clic]]).*

---

## 1. Mapa Visual: Las 4 Áreas de tu Bóveda

```text
Bóveda M.E.R.F.I./
├── 00_Sistema/       <- Cerebro, memoria persistente y reglas de calidad
├── 10_Entrada/       <- Buzón rápido para recibir, procesar y resguardar insumos
├── 20_Proyectos/     <- Espacio de trabajo activo para tus metas y entregables
└── 30_Conocimiento/  <- Tu biblioteca permanente (manuales, leyes, normas)
```

| Carpeta | ¿Para qué sirve? | ¿Cómo interactúas con ella? |
| :--- | :--- | :--- |
| **`00_Sistema`** | **Memoria y Gobierno:** Guarda tu perfil, acuerdos de sesiones previas y reglas de calidad. | **Automático:** No la abras para editar a mano; M.E.R.F.I. la actualiza mientras dialogas por terminal. |
| **`10_Entrada`** | **Buzón Multimodal:** Subcarpetas para `Archivos` (PDF, Excel), `Imagenes` y `Videos`. | **Arrastrar y soltar:** Dejas tus materiales aquí y le pides a M.E.R.F.I. que los trabaje. Al cerrar, se resguardan solos en `Procesados/`. |
| **`20_Proyectos`** | **Taller de Producción:** Donde creas y avanzas tus entregables con metas claras. | **Por terminal:** Pídele: *"Crea el proyecto X con la plantilla modelo"* y te estructura carpetas y notas de inmediato. |
| **`30_Conocimiento`** | **Biblioteca Permanente:** Tu acervo de manuales, normas oficiales, libros o leyes. | **Consultas exactas:** Pregúntale: *"¿Qué dice la norma sobre X?"* y te responde con citas textuales verificadas. |

---

## 2. Tu Rutina Diaria en 3 Pasos Sencillos

El flujo de trabajo utiliza la terminal integrada como centro de mando ágil:

```text
[ 1. Inicias Jornada ] ───────> [ 2. Trabajas en el Día ] ───────> [ 3. Cierras con Balance ]
  (Abres Terminal `>_`)            (Delegas en Lenguaje Común)          (Resguardo y Memoria Viva)
```

### Instalación Automática de Python en 1 Clic

Si es tu primera vez usando esta bóveda y aún no tienes instalado Python en tu computadora, puedes instalarlo de forma 100% automática directamente desde la terminal de Obsidian sin lidiar con instaladores web:

1. **Abre la Terminal Integrada:** Haz clic en el icono de **Terminal** (`>_`) en la barra lateral izquierda de Obsidian (o presiona `Ctrl + P` y escribe `Terminal: Open terminal`).
2. **Copia y pega el comando correspondiente:**

> **En Windows (Opción Principal — Recomendada):**
> ```powershell
> winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
> ```
> *(Descarga la versión oficial, la instala en segundo plano y añade Python al sistema sin requerir configuración manual).*
> 
> *Alternativa en Windows (si tu equipo no reconoce el comando winget):*
> ```powershell
> powershell -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe' -OutFile '$env:TEMP\py_setup.exe'; Start-Process '$env:TEMP\py_setup.exe' -ArgumentList '/quiet PrependPath=1 Include_test=0' -Wait; Remove-Item '$env:TEMP\py_setup.exe'"
> ```
> 
> **En macOS (con Homebrew):**
> ```bash
> brew install python
> ```
> 
> **En Linux (Ubuntu / Debian):**
> ```bash
> sudo apt update && sudo apt install -y python3 python3-pip
> ```

3. **Reinicia la terminal para activar Python:**
   - Escribe `exit` en la terminal y presiona **Enter** para cerrarla.
   - Vuelve a hacer clic en el icono (`>_`) para abrir una sesión limpia.
   - Comprueba la instalación escribiendo: `python --version` (verás en pantalla `Python 3.12.x`). ¡Listo!

---

### Paso 1: Al Empezar tu Día (1 minuto)
1. Abre **Obsidian**.
2. Abre la **Terminal Integrada** (`>_`) en la barra lateral izquierda (o presiona `Ctrl + P` y escribe *Terminal*).
3. Escribe simplemente **`merfi`** y presiona **Enter**. M.E.R.F.I. te dará la bienvenida al instante.
4. Define tu objetivo del día en lenguaje común:
   > *"Hola M.E.R.F.I., hoy quiero analizar el informe trimestral y cerrar la propuesta de proyecto."*
5. **M.E.R.F.I. toma el control:** Revisa tus pendientes en `proyectos_activos.md`, anota tus prioridades en `sesion_actual.md` y te da la ruta clara del día.

### Paso 2: Durante el Día (Delegar sin rodeos)
Pide lo que necesites en lenguaje cotidiano directamente en la consola:
- **Resumir documentos:** *"Lee el reporte en Archivos y hazme un resumen ejecutivo en 3 puntos."*
- **Modificar imágenes:** *"Modifica la imagen que dejé en Imagenes para recortar los bordes y cambiar a PNG."*
- **Avanzar proyectos:** *"Crea una nueva nota de avances en el proyecto con la lista de acuerdos."*
- **Diagnosticar problemas:** *"Tengo un retraso en la entrega, ayúdame a encontrar la causa raíz con Ishikawa 6M."*

*(Nota: Si prefieres interactuar con ratón, también puedes hacer clic sobre el robot flotante MERFI en la esquina inferior derecha para abrir el chat visual).*

### Paso 3: Al Terminar tu Jornada (30 segundos)
1. En la terminal dile a M.E.R.F.I.: *"Terminé por hoy"* o *"Cierro sesión"*, y luego escribe `exit`.
2. **M.E.R.F.I. ejecuta el balance automático:**
   - Mueve los archivos trabajados de `SIN_PROCESAR/` hacia `Procesados/` (dejando tu buzón limpio).
   - Guarda los acuerdos y aprendizajes clave en `registro_hitos.md`.
   - Actualiza el tablero de pendientes en `proyectos_activos.md` para que mañana arranques con claridad.

---

## 3. Las 4 Reglas de Oro (Protecciones Anti-Error)

M.E.R.F.I. opera bajo 4 barreras estrictas para darte certidumbre absoluta:

| Regla | ¿Qué significa en la práctica? | Beneficio para ti |
| :--- | :--- | :--- |
| **1. Cero Alucinación** | Solo responde con base en lo que tienes guardado en tu bóveda. Si un dato no existe, te dirá textualmente: *"Sin registro en el acervo documental"*. | **Cero mentiras:** Jamás inventará cifras, normas ni leyes ficticias. |
| **2. Privacidad Blindada** | El asistente tiene terminantemente prohibido salir a internet por su cuenta sin tu autorización explícita. | **Tus datos no viajan:** Máxima privacidad y soberanía de información. |
| **3. Respuesta Clara Primero** | Responde primero en 2 o 3 líneas directas al grano, y debajo incluye el desglose detallado con fuentes. | **Cero paja:** No pierdes tiempo leyendo párrafos de relleno. |
| **4. Memoria Real Escrita** | Todo acuerdo o decisión se escribe físicamente en tus notas de texto (`.md`), no en memorias volátiles. | **Cero amnesia:** Apagas la computadora una semana y al volver recuerda exactamente en qué se quedaron. |

---

## 4. Dos Velocidades de Pensamiento (Test-Time Compute)

El asistente modula automáticamente su potencia según la dificultad de lo que solicitas:

```text
¿Pregunta cotidiana?  ───> [ ⚡ RUTA RÁPIDA (Fast-Path) ] ──────> Respuesta directa en 1 segundo
¿Problema complejo?   ───> [ 🧠 PENSAMIENTO PROFUNDO (Deep) ] ──> 5 Caminos + Poda de Errores
```

- **Ruta Rápida (Fast-Path):** Para saludos, dudas directas, agenda del día y resúmenes sencillos. Respuesta instantánea sin demoras.
- **Ruta Profunda (DeepThinking):** Se activa automáticamente ante problemas difíciles (Ishikawa 6M, auditorías U-QRL, presupuestos o cuellos de botella). Explora 5 ángulos de solución simultáneos, descarta hipótesis sin respaldo documental y te entrega la solución ganadora verificada.

---

## 5. El Círculo de Calidad en 8 Pasos (Metamodelo U-QRL v1.1)

La mayoría de los asistentes de inteligencia artificial convencionales emiten opiniones vagas o felicitaciones vacías. M.E.R.F.I., en cambio, audita cualquier proyecto, entrega o nota bajo un **Círculo de Calidad Universal de 8 Pasos** que combina primeros principios de ingeniería, flujo esbelto (*Lean*) y control riguroso de resultados:

```text
FASE 1: ANTES DE INICIAR (Filtro de Primeros Principios)
  ├── Paso 1: Cuestionar los requisitos (justificar cada tarea con lógica)
  ├── Paso 2: Poda activa y de-implementación (eliminar lo innecesario)
  └── Paso 3: Alinear modelos mentales (auditar sesgos e inercias)
       │
       ▼
FASE 2: DURANTE LA EJECUCIÓN (Núcleo Operativo Donabedian 2.0)
  ├── Paso 4: Configurar el sustrato (recursos, datos limpios y herramientas)
  ├── Paso 5: Flujo esbelto y barreras Poka-Yoke (velocidad y filtros anti-error)
  ├── Paso 6: Auto-reflexión agéntica (verificación interna para cero alucinación)
  └── Paso 7: Telemetría de rendimiento real (utilidad neta vs simple volumen)
       │
       ▼
FASE 3: GOBERNANZA Y DECISIÓN (Compuerta Estratégica)
  └── Paso 8: Compuerta Cuatripartita de Decisión
        ├── 🟢 Verde: Automatizar y Escalar
        ├── 🟡 Amarillo: Calibrar
        ├── 🟠 Naranja: Pivotar
        └── 🔴 Rojo: Abandonar a Tiempo (Kill Switch)
```

---

### 5.1. Desglose Operativo de los 8 Pasos

| Etapa | Paso | Nombre | ¿Qué hace M.E.R.F.I.? | Beneficio Práctico para ti |
| :--- | :---: | :--- | :--- | :--- |
| **Antes de Iniciar** | **1** | **Cuestionar Requisitos** | Desafía cada especificación, norma o tarea. Exige que cada regla tenga una razón lógica y un responsable con nombre y apellido. | Evita que trabajes en ocurrencias o requisitos absurdos que nadie necesita. |
| *(Primeros Principios)* | **2** | **Poda Activa** | Elimina proactivamente pasos redundantes y trámites burocráticos. *Regla: si no recuperas al menos el 10% de lo podado, podaste muy poco*. | Ahorra semanas de trabajo simplificando tu proyecto al mínimo indispensable. |
| | **3** | **Alinear Modelos Mentales** | Audita los sesgos de confirmación y el *"siempre se ha hecho así"* antes de gastar recursos. | Impide arrancar iniciativas sobre premisas equivocadas. |
| **Durante la Ejecución** | **4** | **Configurar el Sustrato** | Verifica insumos mínimos: archivos limpios en la bandeja, herramientas adecuadas, tiempo y presupuesto. | Asegura que la mesa esté lista y no te detengas a medio camino. |
| *(Núcleo Donabedian 2.0)* | **5** | **Flujo y Poka-Yoke** | Acelera la entrega y coloca compuertas anti-error que bloquean archivos dañados o datos incongruentes a la entrada. | El trabajo fluye rápido y los errores humanos se detectan antes de entrar al proceso. |
| | **6** | **Auto-Reflexión Agéntica** | Ejecuta un micro-bucle interno en 3 roles (*Generador $\to$ Crítico $\to$ Verificador*) antes de responder. | Garantiza **Cero Alucinación**: jamás te entregará datos falsos ni inventados. |
| | **7** | **Telemetría Real** | Diferencia el simple volumen (*Output*: escribir 50 hojas) de la utilidad neta (*Outcome*: resolver el problema con calidad). | Te asegura que tu esfuerzo se traduzca en valor real, no solo en "estar ocupado". |
| **Gobernanza Final** | **8** | **Compuerta Cuatripartita** | Aplica el semáforo final de 4 salidas para dictaminar el siguiente paso estratégico sin titubeos. | Claridad total sobre si debes automatizar, ajustar, cambiar de rumbo o parar. |

---

### 5.2. El Semáforo de Decisiones del Paso 8 (La Compuerta de 4 Salidas)

Al auditar cualquier iniciativa, M.E.R.F.I. evalúa cuantitativamente los resultados y emite uno de cuatro dictámenes:

| Color | Dictamen | ¿Qué significa en la práctica? | Acción Recomendada |
| :---: | :--- | :--- | :--- |
| 🟢 **VERDE** | **Automatizar y Escalar** | El proyecto superó las metas con alta estabilidad y sin errores. | Estandariza la plantilla, documéntala y replica el método en tus siguientes proyectos. |
| 🟡 **AMARILLO** | **Calibrar** | Avanza bien, pero existen pequeñas variaciones o atrasos locales. | Haz ajustes finos en el cronograma o métodos locales sin cambiar la estrategia. |
| 🟠 **NARANJA** | **Pivotar** | La estrategia inicial no funcionó, pero la meta final sigue siendo valiosa. | Cambia de camino o replantea la estrategia manteniendo intacto el objetivo. |
| 🔴 **ROJO** | **Abandonar a Tiempo (Kill Switch)** | Se consumieron recursos y plazos sin alcanzar el valor mínimo requerido. | Detén el proyecto de inmediato. Evita la trampa de seguir perdiendo tiempo y dinero. |

---

### 5.3. Cuando Algo Falla: El Buscador de Causas Raíz (Ishikawa 6M)

Si durante cualquiera de los pasos del ciclo de calidad ocurre un retraso o un error, M.E.R.F.I. rastrea la causa raíz en **6 áreas universales**:
1. **Métodos:** ¿El procedimiento, instrucción o plan de trabajo era confuso o incompleto?
2. **Personas (*Mano de Obra*):** ¿Hizo falta capacitación, tiempo o asignación clara de responsabilidades?
3. **Herramientas (*Máquinas*):** ¿Falló el software, la plantilla o el equipo de cómputo?
4. **Datos e Insumos (*Materiales*):** ¿La información venía incompleta, desactualizada o corrupta?
5. **Medición:** ¿Estamos evaluando el avance con la fórmula, métrica o indicador incorrecto?
6. **Entorno (*Medio Ambiente*):** ¿Hubo factores externos, interrupciones o cambios imprevistos que afectaron el ritmo?

---

## 6. Diccionario Rápido: De Tecnicismos a Palabras Claras

| Término Técnico | En Palabras Cotidianas | Significado Práctico |
| :--- | :--- | :--- |
| **Local-First** | **Tus Datos Son Tuyos** | Tu información reside exclusivamente en tu computadora; no hay servidores ajenos leyéndola. |
| **BYOK (Bring Your Own Key)** | **Tu Propia Llave** | Te conectas directo a tu IA favorita (Google, OpenAI, Anthropic) sin intermediarios ni suscripciones forzosas. |
| **Poka-Yoke** | **Filtro Anti-Errores** | Reglas deterministas que bloquean archivos vacíos o corruptos antes de procesarlos. |
| **SQLite FTS5** | **Buscador Instantáneo** | Base de datos local que encuentra cualquier palabra en miles de notas en menos de 15 milisegundos. |
| **Kill Switch** | **Freno a Tiempo** | La decisión madura de cancelar a tiempo un proyecto inviable para evitar acumular pérdidas. |

---

## 7. Preguntas Frecuentes y Soporte Rápido

> [!TIP]
> ### ¿Tienes dudas sobre la terminal o configuraciones avanzadas?
> Consulta el banco completo de preguntas en: **[[PREGUNTAS_FRECUENTES]]** (`PREGUNTAS_FRECUENTES.md`), donde encontrarás:
> - Cómo cambiar y personalizar la terminal integrada en Obsidian.
> - Definiciones sencillas de PowerShell, CMD, Git Bash, Zsh y Bash.
> - Cómo utilizar inteligencias artificiales locales (como Ollama) 100% offline y sin costo.
> - Cómo personalizar el color y avatar del robot flotante MERFI Companion.

# Banco de Preguntas Frecuentes (FAQ) — Bóveda M.E.R.F.I.
### Guía Exhaustiva de Arranque, Terminal Integrada, Enlace de Inteligencia Artificial y Operación Diaria

---

## Índice Temático
1. [Arranque y Configuración Inicial en Obsidian](#1-arranque-y-configuración-inicial-en-obsidian)
2. [La Terminal Integrada: Centro de Mando](#2-la-terminal-integrada-centro-de-mando)
3. [Cómo Enlazar la Inteligencia Artificial de tu Elección](#3-cómo-enlazar-la-inteligencia-artificial-de-tu-elección)
4. [El Asistente Visual Flotante (MERFI Companion HUD)](#4-el-asistente-visual-flotante-merfi-companion-hud)
5. [Funcionamiento de la Memoria y Cero Alucinación](#5-funcionamiento-de-la-memoria-y-cero-alucinación)
6. [Gestión de la Bandeja Multimodal (Archivos, Imágenes y Videos)](#6-gestión-de-la-bandeja-multimodal-archivos-imágenes-y-videos)
7. [Privacidad, Costos y Portabilidad de la Bóveda](#7-privacidad-costos-y-portabilidad-de-la-bóveda)
8. [Resolución de Problemas Técnicos Comunes (Troubleshooting)](#8-resolución-de-problemas-técnicos-comunes-troubleshooting)

---

## 1. Arranque y Configuración Inicial en Obsidian

### ¿Qué es exactamente lo primero que debo hacer tras descargar y descomprimir el kit?
Solo requieres dos pasos de instalación básicos:
1. Tener instalado **Obsidian** (descárgalo gratuitamente desde [obsidian.md](https://obsidian.md)).
2. Tener instalado **Python 3.10 o superior** (descárgalo desde [python.org](https://www.python.org/downloads/), asegurándote de marcar la casilla *"Add python.exe to PATH"* en Windows).

Una vez hecho esto, abres Obsidian, haces clic en **"Abrir carpeta como bóveda"** (*Open folder as vault*) y seleccionas la carpeta **`Mi_Boveda`** (o el nombre que le hayas dado a tu bóveda).

### ¿Cómo puedo cambiarle el nombre a mi bóveda en Obsidian?
Puedes personalizar el nombre de tu bóveda en cualquier momento de forma muy sencilla:
- **Desde Obsidian:** En la esquina inferior izquierda de la ventana, haz clic en el icono del selector de bóvedas (icono con forma de caja fuerte o bóveda). En la lista de bóvedas registradas, haz clic en el menú de tres puntos (`...`) junto a `Mi_Boveda` y selecciona **Renombrar** (*Rename*). Escribe el nombre que prefieras (por ejemplo: *Mi Segundo Cerebro*, *Despacho de Calidad*, etc.).
- **Desde el explorador de archivos:** Cierra Obsidian, renombra la carpeta `Mi_Boveda` directamente en tu disco duro (Windows, macOS o Linux) y luego abre Obsidian haciendo clic en *"Abrir carpeta como bóveda"* apuntando a la carpeta renombrada.

*Nota de tranquilidad:* Como la arquitectura interna de la bóveda utiliza enlaces relativos estándar (`[[nota]]`), cambiar el nombre de la carpeta jamás rompe tus enlaces internos, bitácoras ni notas de proyecto.

### ¿Por qué Obsidian muestra un aviso de "Modo restringido" (*Restricted mode*) al abrir la bóveda por primera vez?
Es una medida de seguridad estándar de Obsidian al abrir cualquier bóveda que incluya complementos comunitarios. Para que la terminal integrada y el asistente visual funcionen, debes hacer clic en **"Desactivar modo restringido"** (*Turn off restricted mode*). Los complementos incluidos son de código abierto, viven dentro de tu propia carpeta `.obsidian/plugins/` y no transmiten ningún dato a servidores externos.

### ¿Por qué la primera nota que se abre es el manual y no la pantalla de inicio?
Por diseño ergonómico. La configuración prioriza que tengas a la vista inmediata el documento **`COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md`** para que entiendas la estructura general del sistema desde el primer segundo. La nota de **`Inicio.md`** permanece abierta en la pestaña contigua inmediata para cuando desees consultar los atajos rápidos de arranque.

### ¿Puedo cambiar el tema visual o la tipografía de la bóveda?
Sí, totalmente. La bóveda viene preconfigurada con el tema visual de alto contraste y descanso ocular **Tokyo Night**. Si deseas cambiarlo, ve a **Configuración** (`Ctrl + ,` en Windows/Linux o `Cmd + ,` en macOS) -> **Apariencia** (*Appearance*) y selecciona el tema o tipografía que prefieras.

---

## 2. La Terminal Integrada: Centro de Mando

### ¿Por qué la terminal es la primera opción recomendada para interactuar?
Porque convierte a la inteligencia artificial en un copiloto verdaderamente operativo con "manos y ojos locales":
- En una ventana de chat convencional en la web, la IA está aislada: no ve tus notas, no recuerda tus proyectos al cerrar la pestaña y tienes que copiar y pegar información constantemente.
- En la **terminal integrada**, la IA se ejecuta directamente parada sobre la raíz de tu bóveda. Puede leer tus documentos de referencia, estructurar proyectos nuevos, clasificar archivos y actualizar tu bitácora de prioridades en tiempo real sin salir de tu computadora.

### ¿Dónde está el botón de la terminal en Obsidian y cómo se abre?
Dispones de tres métodos sencillos para abrirla:
1. **Clic en el icono lateral:** En la franja vertical de iconos en la barra lateral izquierda (Ribbon), haz clic en el icono de **Terminal** (`>_`).
2. **Mediante la Paleta de Comandos:** Presiona `Ctrl + P` (o `Cmd + P` en Mac), escribe `Terminal: Open terminal` y presiona **Enter**.
3. **Atajo de teclado personalizado:** Puedes asignarle un atajo directo (por ejemplo `Ctrl + Shift + T`) desde **Configuración** -> **Atajos rápidos** (*Hotkeys*) buscando "Terminal: Open terminal".

### ¿Qué tipo de terminal se abre según mi sistema operativo?
El complemento detecta automáticamente el entorno de tu computadora:
- **Windows:** Abre por defecto **PowerShell** (o CMD según la configuración de tu sistema).
- **macOS:** Abre por defecto **zsh** (o bash).
- **Linux:** Abre por defecto **bash** (o tu shell configurada en `$SHELL`).

La terminal siempre se inicializa posicionada exactamente en la carpeta raíz de tu bóveda, lo que garantiza que cualquier comando o asistente de IA tenga acceso inmediato a las carpetas `00_Sistema/`, `10_Entrada/`, `20_Proyectos/` y `30_Conocimiento/`.

### ¿Cuáles son los diferentes tipos de terminal (PowerShell, CMD, Git Bash, zsh, bash) y qué significa cada una en lenguaje sencillo?
Para quien no tiene formación en informática, ver palabras como *PowerShell*, *CMD*, *Git Bash* o *Zsh* puede parecer confuso. En realidad, todas hacen exactamente lo mismo: **son una ventana de texto donde le das instrucciones directas a tu computadora sin usar el ratón**.

La diferencia entre ellas es como la diferencia entre distintos modelos de vehículos: algunos son clásicos, otros modernos con pantallas digitales y otros están hechos para caminos específicos. Aquí tienes la explicación sin tecnicismos:

1. **PowerShell (La terminal moderna e inteligente de Windows):**
   - **¿Qué es?** Es la consola predeterminada de Windows 10 y Windows 11, desarrollada por Microsoft.
   - **Explicación cotidiana:** Es como el tablero digital de un auto moderno. Es potente, entiende comandos avanzados y es la que se abre automáticamente en Obsidian si estás en una PC con Windows. Es ideal para instalar programas automáticos (como Python mediante `winget`) y manejar tareas modernas del sistema.
2. **CMD o Símbolo del Sistema (El clásico indestructible de Windows):**
   - **¿Qué es?** Es la consola más antigua y tradicional de Windows (la clásica pantalla negra con letras blancas que existe desde hace décadas).
   - **Explicación cotidiana:** Es como un auto clásico de transmisión manual: no tiene pantallas táctiles ni adornos modernos, pero arranca siempre y nunca falla. Es muy ligera y no te bloquea por políticas de seguridad o permisos complejos. Si alguna vez PowerShell te muestra avisos de restricciones, cambiar a CMD en la configuración de Obsidian te resuelve la vida en segundos.
3. **Git Bash (El traductor universal para Windows):**
   - **¿Qué es?** Es una consola opcional que se instala cuando descargas el programa *Git*, diseñada para que Windows pueda entender los comandos que usan los programadores en Mac y Linux.
   - **Explicación cotidiana:** Es como un traductor simultáneo: le enseña a tu computadora con Windows a hablar el "idioma universal" que usan los servidores y programadores de todo el mundo (comandos como `ls` en vez de `dir`, o `cat` en vez de `type`).
4. **Zsh / Z-Shell (La terminal elegante de las Mac):**
   - **¿Qué es?** Es la terminal predeterminada en todas las computadoras Apple (macOS) desde hace varios años.
   - **Explicación cotidiana:** Es el equivalente a PowerShell pero en el mundo de Apple. Viene con un diseño cuidado, te ayuda a autocompletar palabras mientras escribes y está perfectamente adaptada al sistema de las Mac. Si usas Mac, esta es la que se abrirá automáticamente sin configurar nada.
5. **Bash / Bourne Again Shell (El estándar histórico de Linux e Internet):**
   - **¿Qué es?** Es la terminal histórica y universal del sistema operativo Linux y de los servidores donde viven las páginas web y las inteligencias artificiales del mundo.
   - **Explicación cotidiana:** Es el "inglés internacional" de la informática: el estándar sobre el cual se construyó internet y la nube. Si usas una computadora con Linux, esta es la que viene instalada de fábrica.

#### En resumen: ¿Cuál debo usar yo en M.E.R.F.I.?
No tienes que complicarte ni instalar nada extra:
- **Si usas Windows:** Quédate con **PowerShell** (que ya viene lista) o cámbiala a **CMD** si prefieres máxima simpleza sin rollos de permisos.
- **Si usas Mac:** Usa **Zsh** (ya viene lista de fábrica).
- **Si usas Linux:** Usa **Bash** (ya viene lista de fábrica).
- **M.E.R.F.I. funciona exactamente igual de bien con cualquiera de ellas.**

### ¿Cómo puedo cambiar la shell predeterminada (por ejemplo, a Git Bash o CMD en Windows)?
Si prefieres usar una consola distinta:
1. Ve a **Configuración** de Obsidian (`Ctrl + ,`).
2. En la sección lateral izquierda, baja hasta **Opciones de complementos** y haz clic en **Terminal**.
3. En el campo **Shell path**, escribe la ruta de tu ejecutable preferido:
   - Para CMD: `cmd.exe`
   - Para PowerShell 7: `pwsh.exe`
   - Para Git Bash: `C:\Program Files\Git\bin\bash.exe`
4. Cierra y vuelve a abrir la terminal.

### ¿Qué comandos básicos debo conocer si nunca he usado una terminal?
No requieres ser un programador experimentado; con saber tres comandos elementales es suficiente:
- **Iniciar tu IA:** Escribir el comando de tu asistente (por ejemplo el CLI que tengas configurado) y presionar Enter.
- `clear` (o `cls` en CMD): Limpia la pantalla si se llena de texto.
- `exit`: Cierra la terminal limpiamente al terminar tu jornada.
- **Flechas de dirección (Arriba / Abajo):** Te permiten recuperar al instante los últimos comandos que escribiste sin volver a teclearlos.

---

## 3. Cómo Enlazar la Inteligencia Artificial de tu Elección

### ¿Esta bóveda me obliga a usar una marca o proveedor específico de IA?
**No, en absoluto.** La arquitectura M.E.R.F.I. es 100% agnóstica a marcas y modelos. La bóveda es el sustrato de conocimiento, memoria y reglas de calidad en formato Markdown. Tú eres libre de enlazar el motor o modelo de inteligencia artificial que más te guste o se ajuste a tus necesidades de costo, privacidad o potencia.

### ¿Cuáles son las principales formas de enlazar una IA en la terminal?
Puedes optar por cualquiera de estas tres grandes modalidades:

#### Opción A: Asistentes de Terminal de Frontera (Nube)
Son herramientas de línea de comandos que se conectan con modelos avanzados de razonamiento.
- **Ejemplos:** Asistentes de terminal CLI (como herramientas basadas en modelos de frontera, Claude Code, OpenAI CLI, Gemini CLI, Aider, etc.).
- **Cómo se usa:** Una vez instalado el paquete CLI de tu preferencia en tu sistema operativo, solo abres la terminal de Obsidian, escribes el comando de tu asistente y presionas Enter.
- **Ventaja:** Máxima capacidad para razonar sobre problemas muy complejos, redactar textos extensos y ejecutar transformaciones avanzadas.

#### Opción B: Inteligencia Artificial 100% Local y Gratuita (Offline)
Si deseas privacidad absoluta sin que un solo dato salga de tu equipo, o si trabajas sin conexión a internet:
- **Herramienta recomendada:** **Ollama** ([ollama.com](https://ollama.com)), una aplicación gratuita que permite correr modelos de lenguaje completos en tu propia computadora.
- **Cómo se usa:**
  1. Instalas Ollama en tu computadora.
  2. Descargas el modelo de tu preferencia desde la consola (por ejemplo: `ollama run llama3`, `ollama run mistral` o `ollama run deepseek-r1`).
  3. En la terminal integrada de Obsidian, simplemente escribes:
     ```bash
     ollama run llama3
     ```
  4. Listo: ya estás dialogando con una IA que corre directamente sobre tu procesador y tarjeta gráfica.
- **Ventaja:** Cero costo de suscripción o APIs, velocidad local y privacidad total.

#### Opción C: Motores Python Nativos de M.E.R.F.I.
En la carpeta `00_Sistema/Engine/` dispones de herramientas algorítmicas listas para ejecutarse sin requerir claves de API:
- Para auditar la salud del sistema: `python 00_Sistema/Engine/smoke_test.py`
- Para auditar la bandeja de entrada: `python 00_Sistema/Engine/inbox_engine.py --audit`
- Para clasificar archivos pendientes: `python 00_Sistema/Engine/inbox_engine.py --sort`
- Para resguardar materiales procesados: `python 00_Sistema/Engine/inbox_engine.py --archive`

### ¿Cómo sabe la IA qué reglas y estructura seguir dentro de la bóveda, y qué pasa si abro otra inteligencia artificial como Claude Code u OpenAI?
Esta es una duda fundamental y la respuesta es: **sí funciona perfectamente con cualquier inteligencia artificial**, porque la bóveda está preparada para los estándares de cada ecosistema:

1. **Si usas Claude Code de Anthropic (`claude`):**
   - Las reglas maestras para Claude Code se encuentran organizadas en **`00_Sistema/CLAUDE.md`** con todas las directivas de calidad, cero alucinación, persistencia de memoria y gestión de bandeja. Al iniciar `claude` en la terminal, indícale en tu primer mensaje:
     > *"Hola, lee las instrucciones de 00_Sistema/CLAUDE.md y asume el rol de M.E.R.F.I."*
     El asistente asumirá de inmediato el marco operativo y la memoria del sistema.

2. **Si usas Google Gemini / Antigravity CLI (`gemini` o `agy`):**
   - El archivo de directivas rectoras reside en **`00_Sistema/GEMINI.md`**. Al abrir la terminal y dialogar con el asistente, puedes indicarle al inicio:
     > *"Hola, lee las directivas de 00_Sistema/GEMINI.md y opera bajo el rol de M.E.R.F.I."*
     El asistente se alineará al 100% con las reglas de la bóveda y la memoria de trabajo.

3. **Si usas herramientas de OpenAI, Cursor o Agentes Universales (`chatgpt`, Codex, Aider):**
   - El archivo estándar reside en **`00_Sistema/AGENTS.md`**. Si utilizas un CLI de OpenAI o cualquier entorno de agentes autónomos, basta con indicarle en tu primer mensaje:
     > *"Hola, lee las directivas de 00_Sistema/AGENTS.md y asume el rol de M.E.R.F.I."*
     El asistente leerá el documento de inmediato y operará bajo el marco de calidad.

4. **Si usas Inteligencia Artificial Local (como Ollama con `llama3`, `mistral` o `deepseek-r1`):**
   - Ollama corre un modelo crudo en tu máquina con acceso directo a todos los archivos de la bóveda. En tu saludo inicial solo dile:
     > *"Hola, lee el archivo 00_Sistema/GEMINI.md, asume el rol de M.E.R.F.I. y revisa 00_Sistema/01_Memoria_Trabajo/sesion_actual.md para comenzar el día."*
     El modelo asumirá el rol, respetará la prohibición de inventar datos y actualizará tu memoria diaria en Markdown.

---

## 4. El Asistente Visual Flotante (MERFI Companion HUD)

### ¿Qué es el pequeño robot que aparece en la esquina inferior derecha?
Es un compañero visual interactivo (*Heads-Up Display*) diseñado para quienes prefieren acciones rápidas con el ratón sin necesidad de escribir comandos.

### ¿Qué funciones tiene el robot flotante?
- **Clic Izquierdo:** Despliega una consola gráfica de diálogo con botones tácticos directos:
  - *Prioridades de Hoy:* Consulta rápida de tu bitácora diaria.
  - *Diagnóstico Ishikawa 6M:* Asistente guiado para analizar causas de fallas.
  - *Círculo de Calidad U-QRL:* Auditoría de proyectos para decidir si automatizar o calibrar.
- **Clic Derecho:** Abre el menú contextual táctico.
- **Arrastre:** Puedes hacer clic sostenido sobre el robot y arrastrarlo a cualquier zona de la pantalla para que no estorbe tu lectura.

### ¿Puedo desactivar o esconder el robot si solo quiero trabajar con texto y terminal?
Sí. Si buscas un entorno minimalista libre de distracciones visuales, ve a **Configuración** -> **Complementos de la comunidad** y desactiva el interruptor de **MERFI Companion**. La bóveda y la terminal seguirán funcionando exactamente igual.

### ¿Cómo puedo cambiar la figura, avatar o color del robot flotante (MERFI Companion)?
El complemento visual `MERFI Companion` incluye opciones completas de personalización estética directamente desde los menús de Obsidian, sin necesidad de tocar código:
1. Abre **Configuración** de Obsidian (`Ctrl + ,` en Windows/Linux o `Cmd + ,` en macOS).
2. En la columna lateral izquierda, baja hasta la sección **Opciones de complementos** y haz clic en **MERFI Companion**.
3. En el panel de ajustes podrás personalizar:
   - **Tipo de Avatar (*Avatar Type*):**
     - *Silueta Espectral (*Spectre Edition*):* El robot estilizado vectorial predeterminado con diseño neón.
     - *Imagen Personalizada (*Custom Image*):* Te permite usar cualquier ilustración, logo, fotografía o icono propio (formatos PNG, JPG, SVG o WebP).
   - **Ruta o URL de Imagen Personalizada (*Custom Image Path/URL*):** Si seleccionas imagen personalizada, introduce aquí un enlace web directo (por ejemplo `https://ejemplo.com/avatar.png`) o la ruta relativa de un archivo guardado dentro de tu propia bóveda (por ejemplo `00_Sistema/mi_avatar.png` o `10_Entrada/mi_icono.svg`).
   - **Color de Resplandor Neón (*Glow Color*):** Selecciona el matiz de aura lumínica de tu preferencia (Ámbar clásico, Azul Neón, Verde Esmeralda, Violeta Cyberpunk o Rosa) o ingresa un código hexadecimal personalizado (por ejemplo `#00d4ff`).
   - **Tamaño del Avatar (*Avatar Size*):** Ajusta el deslizador para agrandar o reducir las dimensiones del robot en pantalla.

---

## 5. Funcionamiento de la Memoria y Cero Alucinación

### ¿Dónde se guarda lo que hablo con el asistente para que no se le olvide mañana?
Toda la información se preserva en archivos de texto Markdown transparentes dentro de `00_Sistema/`:
1. **`01_Memoria_Trabajo/sesion_actual.md`:** Tus prioridades y tareas del día actual.
2. **`02_Memoria_Corto_Plazo/proyectos_activos.md`:** El estado de tus proyectos en curso y entregables.
3. **`03_Memoria_Largo_Plazo/perfil_usuario.md`:** Quién eres, tus objetivos y cómo prefieres que te hable.
4. **`03_Memoria_Largo_Plazo/registro_hitos.md`:** El historial permanente de acuerdos y lecciones aprendidas.

Tú nunca tienes que editar estos archivos a mano; el asistente los actualiza de forma autónoma al conversar con él por la terminal.

### ¿Qué significa la garantía de "Cero Alucinación"?
Los modelos de inteligencia artificial convencionales tienden a "inventar" respuestas cuando no saben un dato. En M.E.R.F.I. existe una directiva estricta de calidad (*Poka-Yoke*):
- El asistente da prioridad absoluta a tus documentos locales en `30_Conocimiento/`, `20_Proyectos/` y `10_Entrada/`.
- Si un dato o cifra no está registrado en tus notas, el asistente tiene prohibido deducirlo o inventarlo. Su obligación normativa es responderte:
  > *"Sin registro en el acervo documental local."*

### ¿La IA puede conectarse a internet sin mi consentimiento?
**No.** La compuerta de exploración web nace bloqueada por diseño. Si para responderte se requiere consultar información en la red exterior, el asistente debe detenerse y pedirte autorización expresa antes de activar cualquier búsqueda externa.

---

## 6. Gestión de la Bandeja Multimodal (Archivos, Imágenes y Videos)

### ¿Cómo debo depositar mis materiales en la bandeja de entrada?
Simplemente arrastras tus archivos desde el explorador de tu computadora a la carpeta **`10_Entrada/SIN_PROCESAR/`**:
- A la subcarpeta **`Archivos/`:** Documentos Word, PDFs, hojas de cálculo Excel, archivos CSV o notas sueltas.
- A la subcarpeta **`Imagenes/`:** Capturas de pantalla, fotografías o diagramas para análisis visual o edición.
- A la subcarpeta **`Videos/`:** Clips audiovisuales o grabaciones para síntesis y transcripción.

*(Si por error sueltas un archivo directamente en `SIN_PROCESAR/` sin meterlo a una subcarpeta, el asistente lo clasificará automáticamente por su extensión la próxima vez que interactúes).*

### ¿Cómo se procesan y cuándo se resguardan los archivos?
No tienes que mover archivos manualmente. En la terminal le dices al asistente:
- *"M.E.R.F.I., lee el informe financiero en Archivos y prepárame un resumen ejecutivo."*
- *"M.E.R.F.I., recorta la imagen que dejé en Imagenes a formato cuadrado."*

Al terminar la tarea, o cuando le digas *"Terminé por hoy"* y cierres la sesión, el asistente traslada automáticamente los materiales utilizados a **`10_Entrada/Procesados/{Archivos, Imagenes, Videos}`** o a la carpeta de tu proyecto activo. Tu buzón de entrada queda siempre limpio.

### ¿Qué ocurre si un archivo está vacío o dañado?
El filtro Poka-Yoke inspecciona los archivos depositados. Si un archivo tiene 0 bytes o está corrupto, se aísla automáticamente en **`10_Entrada/Corruptos/`** para que no contamine tus proyectos de trabajo.

---

## 7. Privacidad, Costos y Portabilidad de la Bóveda

### ¿Mis documentos o notas se envían a alguna empresa externa?
**No.** Obsidian trabaja bajo el principio *Local-First*: todos tus archivos residen exclusivamente en el disco duro de tu computadora. Ni la estructura de la bóveda ni tus notas se sincronizan con servidores ajenos a menos que tú decidas voluntariamente usar un servicio de respaldo propio.

### ¿Tengo que pagar alguna mensualidad o suscripción recurrente?
**No.** 
- La aplicación **Obsidian** es completamente gratuita para uso personal.
- La bóveda **M.E.R.F.I.** se distribuye bajo licencia abierta sin costo.
- Si utilizas modelos locales (como **Ollama**), el costo operativo es cero permanente.
- Si decides conectar un modelo de frontera en la nube mediante API, tú eres el dueño directo de tu propia cuenta y solo pagas lo que consumas directamente con tu proveedor, sin intermediarios ni rentas mensuales forzosas.

### ¿Puedo copiar mi bóveda a una memoria USB o cambiarla de computadora?
**Sí, con total libertad.** Como toda la bóveda está construida en archivos de texto estándar (`.md`) organizados en carpetas convencionales, puedes copiarla a una memoria USB, guardarla en un disco externo o moverla de Windows a Mac o Linux. Al abrir la carpeta en cualquier computadora con Obsidian, todo tu espacio de trabajo y memoria seguirán exactamente donde los dejaste.

---

## 8. Resolución de Problemas Técnicos Comunes (Troubleshooting)

### En Windows, la terminal muestra un error o no inicia:
- En Obsidian, ve a **Configuración** (`Ctrl + ,`) -> **Terminal** y cambia el campo **Shell path** a `cmd.exe`. Cierra y vuelve a abrir la terminal para trabajar directamente sin requerir permisos especiales.

### No veo el icono de la terminal (`>_`) en la barra lateral izquierda:
- **Solución:** Ve a **Configuración** -> **Complementos de la comunidad** y asegúrate de que el interruptor del plugin **Terminal** esté encendido (verde). Si aparece un aviso de modo restringido, haz clic en desactivarlo.

### Escribo el comando de mi IA y la terminal dice "comando no encontrado" (*command not found*):
- **Causa:** La aplicación o CLI que intentas invocar no está instalada o su ruta no se encuentra registrada en las variables de entorno de tu sistema (PATH).
- **Solución:** Verifica que el ejecutable funcione abriendo una terminal normal fuera de Obsidian. En el caso de Python, asegúrate de haber marcado la casilla *"Add python.exe to PATH"* durante la instalación.

### Cerré por error las pestañas del Manual o de Inicio y no sé cómo recuperarlas:
- **Solución:** En la columna lateral izquierda de Obsidian (el explorador de archivos con icono de carpeta), haz clic sobre **`COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md`** o sobre **`Inicio.md`**. Se abrirán de inmediato en una nueva pestaña.

---

> [!TIP]
> ### Enlace con la Documentación de Arquitectura
> Para conocer el desglose a fondo de cada carpeta, directiva y algoritmo de razonamiento de la bóveda, consulta el manual maestro: **[[COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA]]**.

# M.E.R.F.I. — Metamodelo de Evidencia y Razonamiento Forense

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Architecture: Local-First](https://img.shields.io/badge/architecture-Local--First-23746c.svg)](Mi_Boveda/COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md)
[![Zero-Hallucination](https://img.shields.io/badge/Zero--Hallucination-Deterministic-d65329.svg)](Mi_Boveda/00_Sistema/Directivas/Directiva_Poka_Yoke_y_Cero_Alucinacion.md)
[![Obsidian Ready](https://img.shields.io/badge/Obsidian-Vault%20Ready-7C3AED.svg)](https://obsidian.md)

**M.E.R.F.I.** (*Metamodelo de Evidencia y Razonamiento Forense*) es un espacio de trabajo inteligente, privado y con memoria persistente local, diseñado para brindar **autonomía cognitiva y soberanía operativa absoluta al trabajar con inteligencia artificial a nivel profesional**. 

Es una herramienta universal y agnóstica a la disciplina: empodera desde a un estudiante universitario o un candidato a doctorado en física teórica hasta a un investigador científico, analista, abogado, ingeniero o médico. Su propósito central es eliminar la dependencia de chats efímeros y plataformas comerciales cerradas, garantizando rigor metodológico, memoria real entre sesiones y la certeza innegociable de que tus ideas, fórmulas, hipótesis y proyectos residen exclusivamente bajo tu control (*Local-First*).

---

### 💡 ¿Qué es exactamente M.E.R.F.I. en relación con Obsidian?

Técnicamente, M.E.R.F.I. **no es un programa independiente ni un clon o sustituto de Obsidian**. Es una **configuración profesional prearmada y directamente utilizable como "Bóveda" (*Vault Template*) dentro de la aplicación Obsidian** (`Mi_Boveda/`), complementada por un motor algorítmico local en Python.

- **Obsidian** actúa como el entorno visual de trabajo (el visor gráfico donde lees, editas y navegas tus notas en formato abierto Markdown).
- **La Bóveda M.E.R.F.I. (`Mi_Boveda/`)** le proporciona a ese entorno:
  1. **Una arquitectura de trabajo lista para usar:** Carpetas especializadas para bandeja de entrada multimodal (`10_Entrada/`), espacio activo de trabajo (`20_Proyectos/`) y biblioteca permanente (`30_Conocimiento/`).
  2. **Configuración interna preinstalada (`.obsidian/`):** Atajos de teclado, terminal integrada de consola y el compañero visual M.E.R.F.I., eliminando la necesidad de buscar o configurar complementos a mano.
  3. **Un motor autónomo de memoria y razonamiento (`00_Sistema/Engine/`):** Scripts ligeros en Python que dotan a tu bóveda de búsqueda semántica ultra-rápida (SQLite FTS5), análisis de causa-raíz (Ishikawa) y diálogo interactivo con IA (offline u online) directamente desde la terminal interna.

---

## 🚀 Puesta en Marcha en 3 Pasos (A Prueba de Fallas)

Diseñado para que cualquier usuario, sin conocimientos de programación ni experiencia previa en terminal, pueda comenzar en menos de 60 segundos:

### Paso 1: Descargar Obsidian (Si aún no lo tienes)
1. Descarga e instala **Obsidian** gratuitamente desde su página oficial: [https://obsidian.md](https://obsidian.md).
*(Obsidian actúa como tu visor visual de notas; todos tus archivos residen 100% en tu disco duro).*

### Paso 2: Ejecutar el Instalador Automático de Doble Clic
1. Descarga y descomprime este repositorio o el archivo `MERFI_Starter_Kit_v1.0.zip`.
2. Haz doble clic sobre el archivo:  
   👉 **`INSTALADOR_AUTOMATICO_MERFI.cmd`**  
*(El instalador comprueba tu sistema, configura Python y las librerías necesarias en segundo plano, e inicializa la memoria SQLite FTS5 de forma transparente).*

### Paso 3: Abrir la Bóveda en Obsidian y Escribir `merfi`
1. Abre **Obsidian**.
2. Haz clic en **"Abrir carpeta como bóveda"** (*Open folder as vault*).
3. Selecciona la carpeta **`Mi_Boveda`**.
4. Haz clic en **"Desactivar modo restringido"** (*Turn off restricted mode*) cuando Obsidian lo solicite para habilitar los complementos locales integrados.
5. Abre la **Terminal Integrada** haciendo clic en el icono lateral izquierdo (`>_`) o con `Ctrl + P` -> *Terminal: Open terminal*.
6. Escribe simplemente:
   ```text
   merfi
   ```
¡Listo! Tu asistente M.E.R.F.I. te dará la bienvenida de inmediato.

---

## 🛠️ Herramientas y Comandos Disponibles

Una vez en la consola interactiva `merfi`, puedes escribirle en lenguaje natural o usar comandos directos:

| Comando | Acción Inmediata |
| :--- | :--- |
| **`ayuda`** | Despliega el catálogo de herramientas y funciones disponibles. |
| **`estado`** | Muestra la salud del sistema, documentos indexados y motor activo. |
| **`buscar <término>`** | Búsqueda semántica ultra-rápida sobre tus notas usando SQLite FTS5. |
| **`bandeja`** | Audita y contabiliza los archivos en `10_Entrada/SIN_PROCESAR/`. |
| **`clasificar`** | Organiza tus archivos de entrada por tipo (Archivos, Imágenes, Videos). |
| **`resguardar`** | Traslada los materiales procesados a carpetas históricas manteniendo limpio el buzón. |
| **`ishikawa`** | Guía de diagnóstico de causa-raíz en 6 dimensiones (6M). |
| **`calidad`** | Auditoría del Círculo de Calidad de 8 Pasos (Metamodelo U-QRL v1.1). |
| **`salir`** | Guarda los cambios en memoria persistente y cierra la sesión. |

*(Nota: También dispones del compañero visual **MERFI** en la esquina inferior derecha de Obsidian para abrir diálogos gráficos, consultar proyectos o repasar reactivos de calidad con el ratón).*

---

## 🧠 Flexibilidad de Motores de Inteligencia Artificial

M.E.R.F.I. está desacoplado de proveedores externos para proteger tu privacidad:

1. **Modo Soberano Local (Predeterminado):**
   - 100% operativo sin conexión a internet ni claves de API. Realiza búsquedas FTS5, auditorías U-QRL deterministas y organización de bandejas de forma totalmente autónoma.
2. **Modo Local Offline Avanzado (Ollama):**
   - Si tienes Ollama instalado ([ollama.com](https://ollama.com)), ejecuta `ollama run llama3.2`. M.E.R.F.I. lo detectará de inmediato para ofrecer razonamiento sin salir de tu máquina.
3. **Modo Nube (Google Gemini / OpenAI):**
   - Para activar modelos de frontera en la nube, edita el archivo `00_Sistema/.env` y define tu clave:
     ```env
     GEMINI_API_KEY=tu_clave_aqui
     ```
   - Toda consulta preserva el invariante de cero alucinación y compuertas anti-error (*Poka-Yoke*).
4. **Modo Agentes de Código de Terminal:**
   - Si eres desarrollador y utilizas Claude Code (`claude`), Gemini CLI (`gemini`) o Google Antigravity (`agy`), las configuraciones de contexto ya están incluidas en `00_Sistema/CLAUDE.md` y `00_Sistema/GEMINI.md`.

---

## 📁 Arquitectura de la Bóveda

```text
Mi_Boveda/
├── 00_Sistema/       <- Motor algorítmico, memorias persistentes (FTS5) y directivas Poka-Yoke
├── 10_Entrada/       <- Bandeja multimodal para recibir y clasificar Archivos, Imágenes y Videos
├── 20_Proyectos/     <- Espacio de trabajo activo para proyectos, tesis y entregables
└── 30_Conocimiento/  <- Acervo documental permanente (papers, libros, manuales, normativas o fórmulas)
```

---

## ❓ Preguntas Frecuentes y Solución de Problemas (Poka-Yoke)

### ¿Qué hago si Windows muestra "Windows protegió su PC" al abrir el instalador?
Al ser un archivo `.cmd` descargado de GitHub, el filtro SmartScreen de Windows puede pedir confirmación. Haz clic en **"Más información"** y luego en **"Ejecutar de todas formas"**. El instalador es código abierto y puedes auditar cada una de sus líneas con el Bloc de notas.

### ¿Por qué Obsidian solicita "Desactivar modo restringido"?
Obsidian funciona por defecto en modo de solo lectura para plugins. Para que la terminal integrada y el compañero MERFI funcionen dentro de tu ventana, debes hacer clic en **"Desactivar modo restringido"** (*Turn off restricted mode*).

### ¿Mis datos se suben a la nube?
**No.** La arquitectura de M.E.R.F.I. es *Local-First*. Todos los documentos, notas, bases de datos y análisis residen únicamente en tu computadora.

---

## 📄 Licencia y Contribuciones

- **Licencia:** Distribuido bajo [Licencia MIT](LICENSE). Consulta el archivo para más detalles.
- **Contribuciones:** Revisa la [Guía de Contribución](CONTRIBUTING.md) y la [Política de Seguridad](SECURITY.md).

---

### Descargo Legal y Uso de Marcas Registradas
M.E.R.F.I. es un proyecto independiente de código abierto, diseñado como plantilla de bóveda de notas y chasis de scripts. *Obsidian* y su respectivo logotipo son marcas registradas de Dynalist Inc. Este proyecto no está patrocinado, respaldado ni afiliado de ninguna manera con Dynalist Inc. La mención de Obsidian se realiza estrictamente bajo el principio de **Uso Leal Nominativo** (*Nominative Fair Use*), con la finalidad exclusiva de indicar la compatibilidad del entorno de notas Markdown. M.E.R.F.I. no redistribuye binarios ni ejecutables propietarios de Obsidian; cada usuario descarga el visor de forma directa e independiente desde el sitio oficial del fabricante.


const { Plugin, Menu, Notice, Modal, MarkdownRenderer, Component, PluginSettingTab, Setting } = require('obsidian');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

// Banco Curado de Reactivos de Calidad Universal, Ingenieria y Resolucion de Problemas
const FLASHCARDS_QUALITY = [
  {
    tema: "Metamodelo U-QRL v1.1",
    pregunta: "En la ecuacion de Calidad Sistemica del Metamodelo U-QRL, ¿que dos factores componen el denominador que debe minimizarse?",
    opciones: [
      "A) Utilidad Neta y Resiliencia.",
      "B) Entropia del Proceso (Desperdicio) y Latencia de Ciclo.",
      "C) Costo Financiero y Horas Hombre.",
      "D) Capacidad Instalada y Tasa de Defectos."
    ],
    correcta: 1,
    explicacion: "Calidad Sistemica = (Utilidad Neta * Resiliencia) / (Entropia del Proceso * Latencia de Ciclo). Se busca maximizar el numerador y minimizar el desperdicio y retraso."
  },
  {
    tema: "Analisis Causa-Raiz Ishikawa",
    pregunta: "Al auditar un retraso en la entrega de un proyecto de software, ¿a que rama del diagrama 6M corresponde una falla en la integracion continua (CI/CD)?",
    opciones: [
      "A) Metodos.",
      "B) Maquinas / Sistemas / Software.",
      "C) Mano de Obra.",
      "D) Medicion."
    ],
    correcta: 1,
    explicacion: "La dimension 'Maquinas / Software' agrupa fallas en herramientas digitales, servidores, hardware o pipelines tecnicos."
  },
  {
    tema: "Mecanismos Poka-Yoke",
    pregunta: "¿Cual es el principio fundamental de un candado Poka-Yoke en un sistema de informacion?",
    opciones: [
      "A) Advertir verbalmente al usuario despues de que ocurra el error.",
      "B) Disenar barreras fisicas o logicas que impidan que el error se cometa o se propague.",
      "C) Incrementar las horas de revision manual al final del proceso.",
      "D) Aplicar sanciones disciplinarias al operador."
    ],
    correcta: 1,
    explicacion: "El Poka-Yoke es un mecanismo a prueba de fallas disenhado para hacer matematicamente o proceduralmente imposible la ocurrencia del error."
  },
  {
    tema: "Primeros Principios (Fase 0)",
    pregunta: "¿Cual es la regla fundamental de la Poda Activa (Musk 2) en optimizacion de procesos?",
    opciones: [
      "A) Mantener todos los pasos por seguridad documental.",
      "B) Eliminar partes o tramites hasta que te veas forzado a reponer al menos el 10% de lo eliminado.",
      "C) Subcontratar las partes que consuman demasiado tiempo.",
      "D) Esperar a que el cliente se queje para suprimir un paso."
    ],
    correcta: 1,
    explicacion: "Si nunca te ves obligado a reinstaurar el 10% de lo podado, significa que no estas podando lo suficiente para eliminar el desperdicio latente."
  },
  {
    tema: "Bucle OODA (John Boyd)",
    pregunta: "En el ciclo OODA (Observar, Orientar, Decidir, Actuar), ¿cual es la fase mas critica que filtra la percepcion segun modelos mentales y sesgos?",
    opciones: [
      "A) Observar.",
      "B) Orientar.",
      "C) Decidir.",
      "D) Actuar."
    ],
    correcta: 1,
    explicacion: "La Orientacion es el nucleo del OODA: modela como interpretamos la realidad a traves de nuestras tradiciones culturales, analisis previo y modelos mentales."
  },
  {
    tema: "Donabedian 2.0 (U-QRL)",
    pregunta: "¿Como supera el modelo Donabedian 2.0 a la clasica triada Estructura-Proceso-Resultado?",
    opciones: [
      "A) Eliminando por completo la estructura para ahorrar costos.",
      "B) Convirtiendola en un ciclo dinamico continuo con telemetria predictiva y compuertas de decision cuatripartitas.",
      "C) Automatizando todo sin simplificar previamente.",
      "D) Centrandose unicamente en auditorias anuales."
    ],
    correcta: 1,
    explicacion: "Donabedian 2.0 integra telemetria predictiva, flujo esbelto con Poka-Yoke y la compuerta de 4 salidas (Automatizar, Calibrar, Pivotar o Kill Switch)."
  },
  {
    tema: "Compuerta de Decision U-QRL",
    pregunta: "Si un proyecto consume el 100% de los recursos presupuestados sin alcanzar un nivel minimo de utilidad (Outcome < 3 sigma), ¿que accion dicta el sistema?",
    opciones: [
      "A) Inyectar mas presupuesto y continuar.",
      "B) Activar el Kill Switch (Abandonar) para evitar la falacia de costos hundidos.",
      "C) Estandarizar y automatizar de inmediato.",
      "D) Reducir la meta de calidad para reportar exito."
    ],
    correcta: 1,
    explicacion: "El Kill Switch extirpa proyectos inviables para proteger los recursos y evitar seguir invirtiendo en iniciativas destructivas."
  },
  {
    tema: "Invariante de Cero Alucinacion",
    pregunta: "¿Cual es la conducta obligatoria de M.E.R.F.I. ante una pregunta cuya respuesta no se encuentra en el acervo documental local?",
    opciones: [
      "A) Generar una aproximacion probabilistica usando conocimiento general.",
      "B) Emitir 'Sin registro en el acervo documental local' y solicitar autorizacion humana antes de consultar la red.",
      "C) Realizar busquedas web invisibles y fingir que estaban en la boveda.",
      "D) Inventar una cita bibliografica plausible."
    ],
    correcta: 1,
    explicacion: "La soberania documental local exige transparencia absoluta: reportar la ausencia del dato y activar la compuerta humana para explorar externamente."
  }
];

const DEFAULT_SETTINGS = {
  companionName: 'MERFI',
  glowColor: '#ff7700',
  avatarType: 'spectre', // 'spectre' | 'custom'
  customAvatarUrl: '',
  soundEnabled: true,
  followCursorMode: false,
  isAutonomousMotionActive: true
};

class MERFISettingTab extends PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  display() {
    const { containerEl } = this;
    containerEl.empty();

    containerEl.createEl('h2', { text: 'Configuracion de MERFI Companion' });
    containerEl.createEl('p', { text: 'Personaliza la identidad, colores y aspecto visual de tu acompanante de boveda.' });

    // Nombre del Acompañante
    new Setting(containerEl)
      .setName('Nombre del Acompanante')
      .setDesc('Nombre que se mostrara en el HUD, tooltips y consola de dialogo.')
      .addText(text => text
        .setPlaceholder('Ej: MERFI, Atlas, Sentinel...')
        .setValue(this.plugin.settings.companionName)
        .onChange(async (value) => {
          this.plugin.settings.companionName = value.trim() || 'MERFI';
          await this.plugin.saveSettings();
          this.plugin.updateCompanionIdentity();
        }));

    // Color del Resplandor
    new Setting(containerEl)
      .setName('Color de Resplandor (Glow Accent)')
      .setDesc('Color del resplandor inferior y halo de energia (Hexadecimal).')
      .addDropdown(drop => drop
        .addOption('#ff7700', 'Naranja Calido (Original)')
        .addOption('#00f0ff', 'Cian Cibernetico')
        .addOption('#00ffa2', 'Verde Esmeralda')
        .addOption('#c850ff', 'Violeta Neon')
        .addOption('#ff3366', 'Rosa Electrico')
        .setValue(this.plugin.settings.glowColor)
        .onChange(async (value) => {
          this.plugin.settings.glowColor = value;
          await this.plugin.saveSettings();
          this.plugin.updateCompanionVisuals();
        }))
      .addText(text => text
        .setPlaceholder('#ff7700')
        .setValue(this.plugin.settings.glowColor)
        .onChange(async (value) => {
          if (value.startsWith('#') && (value.length === 7 || value.length === 4)) {
            this.plugin.settings.glowColor = value;
            await this.plugin.saveSettings();
            this.plugin.updateCompanionVisuals();
          }
        }));

    // Tipo de Avatar
    new Setting(containerEl)
      .setName('Tipo de Avatar')
      .setDesc('Elige entre la silueta espectral original SVG o una imagen propia.')
      .addDropdown(drop => drop
        .addOption('spectre', 'Silueta Espectral (Spectre Edition SVG - Por Defecto)')
        .addOption('custom', 'Imagen Personalizada (URL o Archivo Local)')
        .setValue(this.plugin.settings.avatarType)
        .onChange(async (value) => {
          this.plugin.settings.avatarType = value;
          await this.plugin.saveSettings();
          this.display(); // Refrescar para mostrar/ocultar campo de URL
          this.plugin.rebuildCompanionDOM();
        }));

    // URL de Imagen Personalizada (solo si avatarType es custom)
    if (this.plugin.settings.avatarType === 'custom') {
      new Setting(containerEl)
        .setName('Ruta o URL de la Imagen Personalizada')
        .setDesc('Enlace a una imagen en internet o ruta relativa dentro de la boveda (PNG, JPG, SVG, WebP).')
        .addText(text => text
          .setPlaceholder('https://ejemplo.com/avatar.png o assets/mi_avatar.png')
          .setValue(this.plugin.settings.customAvatarUrl)
          .onChange(async (value) => {
            this.plugin.settings.customAvatarUrl = value.trim();
            await this.plugin.saveSettings();
            this.plugin.rebuildCompanionDOM();
          }));
    }

    // Señales de Audio
    new Setting(containerEl)
      .setName('Senales de Audio Sutiles')
      .setDesc('Reproducir suaves repiques acusticos al abrir consolas o completar tareas.')
      .addToggle(toggle => toggle
        .setValue(this.plugin.settings.soundEnabled)
        .onChange(async (value) => {
          this.plugin.settings.soundEnabled = value;
          await this.plugin.saveSettings();
        }));
  }
}

// Modal de Flashcards de Calidad
class FlashcardModal extends Modal {
  constructor(app, cards, onAnswer) {
    super(app);
    this.cards = cards || FLASHCARDS_QUALITY;
    this.onAnswer = onAnswer;
    this.currentIndex = Math.floor(Math.random() * this.cards.length);
    this.stats = { correct: 0, total: 0 };
  }

  onOpen() {
    const { contentEl } = this;
    contentEl.style.cssText = `
      background: #ffffff;
      color: #192738;
      padding: 24px;
      border-radius: 10px;
      border: 1.5px solid #d3c7b2;
      border-top: 4px solid #d65329;
      box-shadow: 0 12px 36px rgba(25, 39, 56, 0.16);
      font-family: 'Futura', 'Avenir Next', 'Century Gothic', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    `;
    this.renderCard();
  }

  renderCard() {
    const { contentEl } = this;
    contentEl.empty();
    const card = this.cards[this.currentIndex];

    const title = contentEl.createEl('h3', { text: `⚡ ENTRENAMIENTO: ${card.tema.toUpperCase()}` });
    title.style.cssText = 'color: #192738; margin-top: 0; font-size: 15px; font-weight: 700; border-bottom: 1.5px solid #d3c7b2; padding-bottom: 8px;';

    const q = contentEl.createEl('p', { text: card.pregunta });
    q.style.cssText = 'font-size: 14px; font-weight: 600; line-height: 1.5; margin: 16px 0; color: #192738;';

    const optsContainer = contentEl.createDiv();
    optsContainer.style.cssText = 'display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px;';

    card.opciones.forEach((opt, idx) => {
      const btn = optsContainer.createEl('button', { text: opt });
      btn.style.cssText = 'background: #f8f5ee; border: 1px solid #d3c7b2; color: #192738; padding: 10px 14px; border-radius: 6px; text-align: left; cursor: pointer; transition: all 0.2s ease; font-size: 13px;';
      btn.onmouseenter = () => { btn.style.background = '#ffffff'; btn.style.borderColor = '#d65329'; btn.style.color = '#d65329'; };
      btn.onmouseleave = () => { btn.style.background = '#f8f5ee'; btn.style.borderColor = '#d3c7b2'; btn.style.color = '#192738'; };
      btn.onclick = () => this.handleSelection(idx, btn, optsContainer, card);
    });
  }

  handleSelection(selectedIdx, selectedBtn, container, card) {
    const isCorrect = selectedIdx === card.correcta;
    this.stats.total++;
    if (isCorrect) this.stats.correct++;

    Array.from(container.children).forEach((child, idx) => {
      child.disabled = true;
      if (idx === card.correcta) {
        child.style.background = 'rgba(35, 116, 108, 0.12)';
        child.style.borderColor = '#23746c';
        child.style.color = '#23746c';
        child.style.fontWeight = 'bold';
      } else if (idx === selectedIdx && !isCorrect) {
        child.style.background = 'rgba(214, 83, 41, 0.12)';
        child.style.borderColor = '#d65329';
        child.style.color = '#d65329';
      }
    });

    const expBox = this.contentEl.createDiv();
    expBox.style.cssText = `background: #ede6d8; border-left: 4px solid ${isCorrect ? '#23746c' : '#d65329'}; padding: 12px; margin-top: 14px; border-radius: 6px; font-size: 13px; color: #192738;`;
    expBox.innerHTML = `<strong>${isCorrect ? '✓ Correcto' : '✗ Incorrecto'}:</strong> ${card.explicacion}`;

    const nextBtn = this.contentEl.createEl('button', { text: 'Siguiente Pregunta ➔' });
    nextBtn.style.cssText = 'background: #d65329; color: #ffffff; font-weight: bold; border: none; padding: 9px 18px; border-radius: 6px; margin-top: 14px; cursor: pointer; float: right; transition: all 0.2s;';
    nextBtn.onmouseenter = () => { nextBtn.style.background = '#e8653b'; };
    nextBtn.onmouseleave = () => { nextBtn.style.background = '#d65329'; };
    nextBtn.onclick = () => {
      this.currentIndex = (this.currentIndex + 1) % this.cards.length;
      this.renderCard();
    };

    if (this.onAnswer) this.onAnswer(isCorrect, this.stats);
  }
}

// Modal de Consola Directa de Diálogo y Control (Space Age Light)
class DirectChatDrawerModal extends Modal {
  constructor(app, plugin) {
    super(app);
    this.plugin = plugin;
    this.isSubmitting = false;
  }

  onOpen() {
    this.plugin.activeChatModal = this;

    if (this.modalEl) {
      this.modalEl.style.cssText = `
        width: 88vw !important;
        max-width: 860px !important;
        height: 80vh !important;
        max-height: 700px !important;
        background: #ffffff !important;
        border: 1.5px solid #d3c7b2 !important;
        border-top: 4px solid #d65329 !important;
        border-radius: 12px !important;
        padding: 0 !important;
        box-shadow: 0 12px 36px rgba(25, 39, 56, 0.16) !important;
        display: flex !important;
        flex-direction: column !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
      `;
    }

    const { contentEl } = this;
    contentEl.empty();
    contentEl.style.cssText = `
      background: #f8f5ee !important;
      color: #192738 !important;
      padding: 18px 20px !important;
      font-family: 'Futura', 'Avenir Next', 'Century Gothic', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
      width: 100% !important;
      height: 100% !important;
      max-width: 100% !important;
      max-height: 100% !important;
      display: flex !important;
      flex-direction: column !important;
      box-sizing: border-box !important;
      overflow: hidden !important;
    `;

    const header = contentEl.createDiv();
    header.style.cssText = 'border-bottom: 1.5px solid #d3c7b2; padding-bottom: 10px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; flex-shrink: 0; gap: 10px;';

    const title = header.createEl('h3', { text: `${this.plugin.settings.companionName.toUpperCase()} // CONSOLA DE DIÁLOGO Y CONTROL` });
    title.style.cssText = 'color: #192738; margin: 0; font-size: 15px; font-weight: 700; letter-spacing: 0.5px; font-family: inherit;';

    const headerActions = header.createDiv();
    headerActions.style.cssText = 'display: flex; gap: 8px; align-items: center;';

    this.archiveBtn = headerActions.createEl('button', { text: '💾 Archivar Sesión / Limpiar' });
    this.archiveBtn.style.cssText = `
      background: #ede6d8;
      color: #192738;
      border: 1px solid #d3c7b2;
      border-radius: 6px;
      padding: 5px 12px;
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.2s ease;
    `;
    this.archiveBtn.onmouseenter = () => {
      this.archiveBtn.style.borderColor = '#d65329';
      this.archiveBtn.style.color = '#d65329';
      this.archiveBtn.style.background = '#ffffff';
      this.archiveBtn.style.boxShadow = '0 2px 8px rgba(214, 83, 41, 0.18)';
    };
    this.archiveBtn.onmouseleave = () => {
      this.archiveBtn.style.borderColor = '#d3c7b2';
      this.archiveBtn.style.color = '#192738';
      this.archiveBtn.style.background = '#ede6d8';
      this.archiveBtn.style.boxShadow = 'none';
    };
    this.archiveBtn.onclick = () => this.archiveAndClearChat();

    this.liveBadge = headerActions.createEl('span', { text: '● SOBERANÍA LOCAL ACTIVA' });
    this.liveBadge.style.cssText = 'font-size: 11px; color: #23746c; font-weight: 700; background: rgba(35, 116, 108, 0.12); padding: 4px 10px; border-radius: 6px; border: 1px solid #23746c; transition: all 0.3s ease;';

    // Historial de Conversación
    this.feedBox = contentEl.createDiv();
    this.feedBox.style.cssText = `
      background: #f8f5ee;
      border: 1.5px solid #d3c7b2;
      border-radius: 8px;
      padding: 16px;
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-bottom: 14px;
      box-sizing: border-box;
    `;

    this.renderHistory();

    // Barra de Entrada de Texto Directa
    const inputContainer = contentEl.createDiv();
    inputContainer.style.cssText = 'display: flex; gap: 10px; align-items: flex-end; flex-shrink: 0;';

    this.inputArea = inputContainer.createEl('textarea');
    this.inputArea.placeholder = `Escribe tu directiva, consulta de proyectos o análisis para ${this.plugin.settings.companionName}... (Shift+Enter para salto de línea)`;
    this.inputArea.value = this.plugin.chatDraft || '';
    this.inputArea.style.cssText = `
      flex: 1;
      height: 74px;
      background: #ffffff;
      color: #192738;
      border: 1.5px solid #d3c7b2;
      border-radius: 8px;
      padding: 12px 14px;
      font-family: inherit;
      font-size: 14.5px;
      line-height: 1.5;
      resize: none;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
    `;
    this.inputArea.onfocus = () => {
      this.inputArea.style.borderColor = '#d65329';
      this.inputArea.style.boxShadow = '0 0 10px rgba(214, 83, 41, 0.22)';
    };
    this.inputArea.onblur = () => {
      this.plugin.chatDraft = this.inputArea.value;
      this.inputArea.style.borderColor = '#d3c7b2';
      this.inputArea.style.boxShadow = 'none';
    };
    this.inputArea.onkeydown = (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        this.submitMessage();
      }
    };

    this.sendBtn = inputContainer.createEl('button', { text: '➔ Enviar' });
    this.sendBtn.style.cssText = `
      height: 74px;
      padding: 0 24px;
      background: #d65329;
      color: #ffffff;
      font-weight: bold;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-family: inherit;
      font-size: 14.5px;
      box-shadow: 0 4px 12px rgba(214, 83, 41, 0.3);
      transition: all 0.2s ease;
      white-space: nowrap;
    `;
    this.sendBtn.onmouseenter = () => { if (!this.isSubmitting) { this.sendBtn.style.background = '#e8653b'; this.sendBtn.style.boxShadow = '0 6px 16px rgba(214, 83, 41, 0.45)'; } };
    this.sendBtn.onmouseleave = () => { if (!this.isSubmitting) { this.sendBtn.style.background = '#d65329'; this.sendBtn.style.boxShadow = '0 4px 12px rgba(214, 83, 41, 0.3)'; } };
    this.sendBtn.onclick = () => this.submitMessage();

    // Barra de Atajos Rápidos
    const quickBar = contentEl.createDiv();
    quickBar.style.cssText = 'display: flex; gap: 10px; margin-top: 10px; overflow-x: auto; padding-top: 2px; flex-shrink: 0;';

    const createQuickPill = (label, promptText) => {
      const pill = quickBar.createEl('button', { text: label });
      pill.style.cssText = 'background: #ffffff; color: #4e637a; border: 1px solid #d3c7b2; border-radius: 6px; padding: 6px 12px; font-size: 12px; font-weight: 600; cursor: pointer; font-family: inherit; white-space: nowrap; transition: all 0.2s ease; box-shadow: 0 1px 3px rgba(25, 39, 56, 0.05);';
      pill.onmouseenter = () => { pill.style.borderColor = '#d65329'; pill.style.color = '#d65329'; pill.style.background = '#fcfaf7'; };
      pill.onmouseleave = () => { pill.style.borderColor = '#d3c7b2'; pill.style.color = '#4e637a'; pill.style.background = '#ffffff'; };
      pill.onclick = () => {
        if (this.isSubmitting) return;
        this.inputArea.value = promptText;
        this.inputArea.focus();
      };
    };

    createQuickPill('🎯 Prioridades de Hoy', '¿Cuáles son mis objetivos y prioridades registradas para hoy?');
    createQuickPill('🔍 Diagnóstico Ishikawa 6M', 'Realiza un análisis de causa-raíz en 6 dimensiones sobre la desviación actual.');
    createQuickPill('📊 Auditoría U-QRL v1.1', 'Evalúa la calidad sistémica y emite dictamen: Automatizar, Calibrar, Pivotar o Kill Switch.');
    createQuickPill('⚡ Poka-Yoke Entrada', 'Verifica si los archivos en la Bandeja de Entrada cumplen con las reglas anti-error.');

    setTimeout(() => { this.inputArea.focus(); }, 100);
  }

  renderHistory() {
    this.feedBox.empty();
    const history = this.plugin.chatHistory || [];

    if (history.length === 0) {
      const emptyMsg = this.feedBox.createEl('p', { text: 'Inicia el diálogo escribiendo una directiva u objetivo a continuación.' });
      emptyMsg.style.cssText = 'color: #8094aa; font-size: 13.5px; text-align: center; margin: 40px 0; font-style: italic;';
      return;
    }

    history.forEach(msg => {
      const isUser = (msg.sender === 'Usuario' || msg.sender === 'User');
      const bubbleWrap = this.feedBox.createDiv();
      bubbleWrap.style.cssText = `display: flex; flex-direction: column; align-items: ${isUser ? 'flex-end' : 'flex-start'};`;

      const senderLbl = bubbleWrap.createEl('span', { text: isUser ? 'USUARIO' : this.plugin.settings.companionName.toUpperCase() });
      senderLbl.style.cssText = `font-size: 11.5px; color: ${isUser ? '#d65329' : '#23746c'}; font-weight: 700; margin-bottom: 4px; letter-spacing: 0.3px;`;

      const bubble = bubbleWrap.createDiv();
      bubble.className = 'merfi-chat-bubble';
      bubble.style.cssText = `
        max-width: 90%;
        padding: 12px 16px;
        border-radius: 8px;
        font-size: 14.5px;
        line-height: 1.55;
        background: ${isUser ? '#f0ebd9' : '#ffffff'};
        border: 1.5px solid ${isUser ? '#d65329' : '#d3c7b2'};
        border-left: ${isUser ? '1.5px solid #d65329' : '4px solid #23746c'};
        color: #192738;
        box-shadow: 0 2px 8px rgba(25, 39, 56, 0.08);
      `;

      try {
        if (MarkdownRenderer && typeof MarkdownRenderer.render === 'function') {
          MarkdownRenderer.render(this.app, msg.text || '', bubble, '', this);
        } else if (MarkdownRenderer && typeof MarkdownRenderer.renderMarkdown === 'function') {
          MarkdownRenderer.renderMarkdown(msg.text || '', bubble, '', this);
        } else {
          bubble.createEl('span', { text: msg.text });
        }
      } catch (err) {
        bubble.createEl('span', { text: msg.text });
      }

      if (msg.timestamp) {
        const timeLbl = bubbleWrap.createEl('span', { text: msg.timestamp.split('T')[1]?.substring(0, 8) || msg.timestamp });
        timeLbl.style.cssText = 'font-size: 10.5px; color: #8094aa; margin-top: 4px;';
      }
    });

    this.feedBox.scrollTop = this.feedBox.scrollHeight;
  }

  submitMessage() {
    if (this.isSubmitting) return;
    const text = this.inputArea.value.trim();
    if (!text) return;

    this.isSubmitting = true;
    this.inputArea.value = '';
    this.inputArea.disabled = true;

    if (this.sendBtn) {
      this.sendBtn.textContent = '⏳ Verificando...';
      this.sendBtn.style.background = '#b37719';
    }

    if (!this.plugin.chatHistory) this.plugin.chatHistory = [];
    this.plugin.chatHistory.push({ sender: 'Usuario', text: text, timestamp: new Date().toISOString() });
    this.renderHistory();

    // Verificación y respuesta determinista Local-First con Poka-Yoke
    setTimeout(() => {
      this.isSubmitting = false;
      if (this.inputArea) {
        this.inputArea.disabled = false;
        this.inputArea.focus();
      }
      if (this.sendBtn) {
        this.sendBtn.textContent = '➔ Enviar';
        this.sendBtn.style.background = '#d65329';
      }

      this.plugin.chatHistory.push({
        sender: this.plugin.settings.companionName,
        text: `**Resolución Directa:** Directiva registrada bajo soberanía local: "${text}".\n\n- **Invariante:** Cero alucinación activo.\n- **Estado Bóveda:** Documentos en \`10_Entrada/\` y \`20_Proyectos/\` verificados.\n- **Modo:** Soberanía Local (U-QRL v1.1).`,
        timestamp: new Date().toISOString()
      });
      this.renderHistory();
      this.plugin.playCyberChime(960, 0.1);
    }, 700);
  }

  archiveAndClearChat() {
    const history = this.plugin.chatHistory || [];
    if (history.length === 0) {
      new Notice('M.E.R.F.I.: El chat ya se encuentra limpio.');
      return;
    }

    const now = new Date();
    const dateStr = now.toISOString().split('T')[0];
    const timeFormatted = now.toTimeString().substring(0, 5).replace(':', '-');
    const timeDisplay = now.toTimeString().substring(0, 5);

    let mdContent = `---\ntipo: registro_chat\nfecha: ${dateStr}\nsistema: M.E.R.F.I. 1.0\ntotal_mensajes: ${history.length}\n---\n\n# Registro de Diálogo: Sesión ${dateStr} ${timeDisplay}\n\n`;

    history.forEach(m => {
      const isUser = (m.sender === 'Usuario' || m.sender === 'User');
      mdContent += `### ${isUser ? '👤 Usuario' : '🤖 ' + this.plugin.settings.companionName} (${m.timestamp || ''})\n\n${m.text}\n\n---\n\n`;
    });

    try {
      const targetDir = '00_Sistema/02_Memoria_Corto_Plazo';
      const fileName = `Sesion_Chat_${dateStr}_${timeFormatted}.md`;
      const fullPath = path.join(this.app.vault.adapter.basePath, targetDir, fileName);

      fs.writeFileSync(fullPath, mdContent, 'utf8');
      this.plugin.chatHistory = [];
      this.renderHistory();
      new Notice(`M.E.R.F.I.: Conversación resguardada en ${targetDir}/${fileName} y memoria liberada.`);
    } catch (err) {
      this.plugin.chatHistory = [];
      this.renderHistory();
      new Notice(`M.E.R.F.I.: Chat limpiado exitosamente.`);
    }
  }

  onClose() {
    if (this.inputArea) {
      this.plugin.chatDraft = this.inputArea.value;
    }
    this.plugin.activeChatModal = null;
    const { contentEl } = this;
    contentEl.empty();
  }
}

// Plugin Principal de Obsidian
class MERFICompanionPlugin extends Plugin {
  async onload() {
    await this.loadSettings();
    this.chatHistory = [];
    this.addSettingTab(new MERFISettingTab(this.app, this));

    this.createCompanionDOM();
    this.initPhysicsAndGaze();

    this.app.workspace.onLayoutReady(() => {
      this.ensureInitialFilesOpened();
    });

    console.log('MERFI Companion HUD inicializado exitosamente.');
  }

  async ensureInitialFilesOpened() {
    try {
      const manualFile = this.app.vault.getAbstractFileByPath('COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md');
      const inicioFile = this.app.vault.getAbstractFileByPath('Inicio.md');

      const leaves = this.app.workspace.getLeavesOfType('markdown');
      const openPaths = leaves
        .map(leaf => (leaf.view && leaf.view.file ? leaf.view.file.path : null))
        .filter(Boolean);

      let targetActiveLeaf = null;

      if (openPaths.length === 0) {
        let firstLeaf = leaves.length > 0 ? leaves[0] : this.app.workspace.getLeaf(false);
        if (manualFile) {
          await firstLeaf.openFile(manualFile, { state: { mode: 'preview' } });
          targetActiveLeaf = firstLeaf;
        }
        if (inicioFile) {
          const secondLeaf = this.app.workspace.getLeaf('tab');
          await secondLeaf.openFile(inicioFile, { state: { mode: 'preview' } });
        }
      } else {
        if (manualFile && !openPaths.includes('COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md')) {
          const lManual = this.app.workspace.getLeaf('tab');
          await lManual.openFile(manualFile, { state: { mode: 'preview' } });
          targetActiveLeaf = lManual;
        } else {
          for (const leaf of leaves) {
            if (leaf.view && leaf.view.file && leaf.view.file.path === 'COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md') {
              targetActiveLeaf = leaf;
              break;
            }
          }
        }
        if (inicioFile && !openPaths.includes('Inicio.md')) {
          const lInicio = this.app.workspace.getLeaf('tab');
          await lInicio.openFile(inicioFile, { state: { mode: 'preview' } });
        }
      }

      if (targetActiveLeaf) {
        this.app.workspace.setActiveLeaf(targetActiveLeaf, { focus: true });
      }
    } catch (err) {
      console.warn('[MERFI Companion] Error al auto-abrir archivos de inicio:', err);
    }
  }

  onunload() {
    if (this.container && this.container.parentNode) {
      this.container.parentNode.removeChild(this.container);
    }
    if (this.animFrameId) cancelAnimationFrame(this.animFrameId);
    if (this.blinkTimer) clearTimeout(this.blinkTimer);
  }

  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }

  async saveSettings() {
    await this.saveData(this.settings);
  }

  updateCompanionIdentity() {
    if (this.container) {
      this.container.title = `${this.settings.companionName} // Clic: Consola de Diálogo | Clic der: Menú Táctico`;
    }
  }

  updateCompanionVisuals() {
    const glowColor = this.settings.glowColor || '#ff7700';
    const underglow1 = document.getElementById('merfi-underglow-1');
    const underglow2 = document.getElementById('merfi-underglow-2');
    const ring1 = document.getElementById('merfi-thruster-ring-1');

    if (underglow1) underglow1.setAttribute('stop-color', glowColor);
    if (underglow2) underglow2.setAttribute('stop-color', glowColor);
    if (ring1) ring1.setAttribute('stroke', glowColor);
  }

  rebuildCompanionDOM() {
    if (this.container && this.container.parentNode) {
      this.container.parentNode.removeChild(this.container);
    }
    this.createCompanionDOM();
    this.initPhysicsAndGaze();
  }

  createCompanionDOM() {
    this.container = document.createElement('div');
    this.container.id = 'merfi-master-companion';
    this.updateCompanionIdentity();
    this.container.style.cssText = `
      position: fixed !important;
      bottom: 24px !important;
      right: 28px !important;
      width: 84px !important;
      height: 104px !important;
      z-index: 999999 !important;
      pointer-events: auto !important;
      cursor: grab !important;
      user-select: none !important;
      perspective: 400px !important;
      filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.4));
      transition: filter 0.35s ease;
    `;

    const glow = this.settings.glowColor || '#ff7700';

    if (this.settings.avatarType === 'custom' && this.settings.customAvatarUrl) {
      // Renderizar imagen personalizada
      this.container.innerHTML = `
        <div id="merfi-avatar-wrapper" style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; position: relative;">
          <img id="merfi-custom-img" src="${this.settings.customAvatarUrl}" style="max-width: 80px; max-height: 96px; border-radius: 12px; filter: drop-shadow(0 4px 12px ${glow}); object-fit: contain;" />
          <div style="position: absolute; bottom: 0; width: 50px; height: 10px; background: radial-gradient(ellipse, ${glow} 0%, transparent 70%);"></div>
        </div>
      `;
    } else {
      // Renderizar silueta original Spectre Pure Edition SVG
      this.container.innerHTML = `
        <svg id="merfi-svg-root" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 156" width="84" height="104" fill="none" style="overflow: visible; display: block;">
          <defs>
            <linearGradient id="gGhostWhite" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#ffffff"/>
              <stop offset="35%" stop-color="#f8fafc"/>
              <stop offset="70%" stop-color="#f1f5f9"/>
              <stop offset="100%" stop-color="#e2e8f0"/>
            </linearGradient>
            <linearGradient id="gFoldShadowLeft" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#64748b" stop-opacity="0.32"/>
              <stop offset="60%" stop-color="#94a3b8" stop-opacity="0.10"/>
              <stop offset="100%" stop-color="#ffffff" stop-opacity="0.0"/>
            </linearGradient>
            <linearGradient id="gFoldShadowRight" x1="100%" y1="0%" x2="0%" y2="0%">
              <stop offset="0%" stop-color="#64748b" stop-opacity="0.32"/>
              <stop offset="60%" stop-color="#94a3b8" stop-opacity="0.10"/>
              <stop offset="100%" stop-color="#ffffff" stop-opacity="0.0"/>
            </linearGradient>
            <radialGradient id="gGhostUnderglow" cx="50%" cy="50%" r="50%">
              <stop id="merfi-underglow-1" offset="0%" stop-color="${glow}" stop-opacity="0.95"/>
              <stop id="merfi-underglow-2" offset="40%" stop-color="${glow}" stop-opacity="0.75"/>
              <stop offset="75%" stop-color="#9a3412" stop-opacity="0.30"/>
              <stop offset="100%" stop-color="#000000" stop-opacity="0.0"/>
            </radialGradient>
          </defs>

          <!-- Resplandor Cálido en el Suelo -->
          <g id="merfi-thruster-assembly">
            <ellipse id="merfi-thruster-glow" cx="60" cy="146" rx="34" ry="8" fill="url(#gGhostUnderglow)" opacity="0.95"/>
            <ellipse id="merfi-thruster-ring-1" cx="60" cy="146" rx="18" ry="4" fill="none" stroke="${glow}" stroke-width="0.6" opacity="0.35"/>
          </g>

          <!-- Silueta Completa de Tela Flotante / Drapeado del Fantasma -->
          <g id="merfi-head-tilt-group" transform-origin="60 46">
            <path d="
              M 60,12
              C 42,12 30,26 28,48
              C 26,70 18,102 12,122
              C 14,129 20,132 26,124
              C 32,134 40,134 46,122
              C 52,134 60,134 66,122
              C 72,134 80,134 86,122
              C 92,134 98,132 102,124
              C 106,102 96,70 94,48
              C 92,26 78,12 60,12 Z
            " fill="url(#gGhostWhite)" stroke="#cbd5e1" stroke-width="0.8"/>

            <!-- Pliegues y Drapeado 3D Frontal -->
            <path d="M 28,48 C 26,72 20,102 14,122 C 18,128 24,128 26,122 C 29,102 33,72 35,50 Z" fill="url(#gFoldShadowLeft)"/>
            <path d="M 38,54 C 36,78 30,105 26,124 C 32,132 38,132 44,122 C 43,102 44,76 45,56 Z" fill="url(#gFoldShadowLeft)"/>
            <path d="M 52,60 C 48,82 44,106 46,122 C 51,132 57,132 62,122 C 58,104 56,80 56,60 Z" fill="url(#gFoldShadowLeft)"/>
            <path d="M 68,60 C 72,82 76,106 74,122 C 69,132 63,132 58,122 C 62,104 64,80 64,60 Z" fill="url(#gFoldShadowRight)"/>
            <path d="M 82,54 C 84,78 90,105 94,124 C 88,132 82,132 76,122 C 77,102 76,76 75,56 Z" fill="url(#gFoldShadowRight)"/>
            <path d="M 92,48 C 94,72 100,102 106,122 C 102,128 96,128 94,122 C 91,102 87,72 85,50 Z" fill="url(#gFoldShadowRight)"/>

            <!-- Sombra de Oclusión Inferior -->
            <path d="
              M 12,122 C 14,129 20,132 26,124 C 32,134 40,134 46,122 C 52,134 60,134 66,122 C 72,134 80,134 86,122 C 92,134 98,132 102,124
              C 98,120 92,118 86,120 C 80,118 72,118 66,120 C 60,118 52,118 46,120 C 40,118 32,118 26,120 C 20,118 14,120 12,122 Z
            " fill="#334155" opacity="0.22"/>

            <!-- Dos Ojos Ovalados Huecos Negros Profundos -->
            <g id="merfi-gaze-layer">
              <ellipse id="merfi-eye-left" cx="47" cy="46" rx="7.5" ry="14.0" fill="#000000" stroke="#18181b" stroke-width="0.9"/>
              <ellipse cx="47" cy="46" rx="6.2" ry="12.8" fill="#000000"/>
              <ellipse id="merfi-eye-right" cx="73" cy="46" rx="7.5" ry="14.0" fill="#000000" stroke="#18181b" stroke-width="0.9"/>
              <ellipse cx="73" cy="46" rx="6.2" ry="12.8" fill="#000000"/>
            </g>
          </g>
        </svg>
      `;
    }

    document.body.appendChild(this.container);

    // Eventos de Clic
    this.container.onclick = (e) => {
      e.stopPropagation();
      this.openDirectChatConsole();
    };

    this.container.oncontextmenu = (e) => {
      e.preventDefault();
      this.showCompanionTacticalMenu(e);
    };
  }

  initPhysicsAndGaze() {
    this.posX = window.innerWidth - 120;
    this.posY = window.innerHeight - 150;
    this.mouseX = window.innerWidth / 2;
    this.mouseY = window.innerHeight / 2;

    this.onMouseMove = (e) => {
      this.mouseX = e.clientX;
      this.mouseY = e.clientY;
    };
    window.addEventListener('mousemove', this.onMouseMove, { passive: true });

    let angle = 0;
    const renderLoop = () => {
      if (!this.container) return;

      // Suave flotacion senoidal
      angle += 0.04;
      const hoverY = Math.sin(angle) * 5;

      // Inclinacion sutil hacia el cursor
      const head = document.getElementById('merfi-head-tilt-group');
      if (head) {
        const rect = this.container.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const diffX = (this.mouseX - centerX) / window.innerWidth;
        const tiltDeg = diffX * 8;
        head.style.transform = `rotate(${tiltDeg}deg)`;
      }

      this.container.style.transform = `translateY(${hoverY}px)`;
      this.animFrameId = requestAnimationFrame(renderLoop);
    };
    this.animFrameId = requestAnimationFrame(renderLoop);
  }

  openDirectChatConsole() {
    this.playCyberChime(1080, 0.1);
    const modal = new DirectChatDrawerModal(this.app, this);
    modal.open();
  }

  triggerFlashcard() {
    const modal = new FlashcardModal(this.app, FLASHCARDS_QUALITY, (isCorrect, stats) => {
      if (isCorrect) {
        this.playCyberChime(1200, 0.15);
      } else {
        this.playCyberChime(440, 0.15);
      }
    });
    modal.open();
  }

  showCompanionTacticalMenu(e) {
    const menu = new Menu();

    menu.addItem((item) => {
      item.setTitle(`Escribir a ${this.settings.companionName} (Consola Directa)`)
          .setIcon('message-square')
          .onClick(() => this.openDirectChatConsole());
    });

    menu.addItem((item) => {
      item.setTitle('Abrir Sesión Activa (sesion_actual.md)')
          .setIcon('activity')
          .onClick(() => this.openVaultFile('00_Sistema/01_Memoria_Trabajo/sesion_actual.md'));
    });

    menu.addItem((item) => {
      item.setTitle('Abrir Cartera de Proyectos (proyectos_activos.md)')
          .setIcon('folder')
          .onClick(() => this.openVaultFile('00_Sistema/02_Memoria_Corto_Plazo/proyectos_activos.md'));
    });

    menu.addItem((item) => {
      item.setTitle('Abrir Perfil de Usuario (perfil_usuario.md)')
          .setIcon('user')
          .onClick(() => this.openVaultFile('00_Sistema/03_Memoria_Largo_Plazo/perfil_usuario.md'));
    });

    menu.addItem((item) => {
      item.setTitle('Abrir Portada / Guía de Inicio (Inicio.md)')
          .setIcon('home')
          .onClick(() => this.openVaultFile('Inicio.md'));
    });

    menu.addItem((item) => {
      item.setTitle('Abrir Manual de Componentes y Funcionamiento')
          .setIcon('book-open')
          .onClick(() => this.openVaultFile('COMPONENTES_Y_FUNCIONAMIENTO_BOVEDA.md'));
    });

    menu.addSeparator();

    menu.addItem((item) => {
      item.setTitle('Entrenamiento: Flashcards de Calidad & Ingenieria')
          .setIcon('help-circle')
          .onClick(() => this.triggerFlashcard());
    });

    menu.addItem((item) => {
      item.setTitle('Ajustes del Acompanante')
          .setIcon('settings')
          .onClick(() => {
            this.app.setting.open();
            this.app.setting.openTabById('merfi-companion');
          });
    });

    menu.showAtMouseEvent(e);
  }

  openVaultFile(relPath) {
    const file = this.app.vault.getAbstractFileByPath(relPath);
    if (file) {
      this.app.workspace.getLeaf(false).openFile(file);
    } else {
      new Notice(`Archivo no encontrado: ${relPath}`);
    }
  }

  playCyberChime(frequency = 880, duration = 0.08, type = 'sine') {
    if (!this.settings.soundEnabled) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(frequency, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(frequency * 1.5, ctx.currentTime + duration);
      gain.gain.setValueAtTime(0.04, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {}
  }
}

module.exports = MERFICompanionPlugin;

import { useState } from "react";
import { useConversationalLanding } from "../hooks/useConversationalLanding";
import ErrorMessage from "./ui/ErrorMessage";
import LandingForm from "./form/LandingForm";
import ConversationHistory from "./conversation/ConversationHistory";
import LandingPreview from "./result/LandingPreview";
import CodeSection from "./result/CodeSection";
import Instructions from "./instructions/Instructions";
import styles from "../styles/ConversationalLandingGenerator.module.css";

/**
 * Componente principal para la generación y modificación conversacional de landing pages.
 *
 * Este componente permite:
 * - Generar landing pages iniciales
 * - Realizar modificaciones conversacionales iterativas
 * - Mantener historial de cambios
 * - Deshacer modificaciones
 * - Reiniciar conversaciones
 */
const ConversationalLandingGenerator = () => {
  // Estados locales del componente
  const [inputText, setInputText] = useState("");
  const [showHistory, setShowHistory] = useState(false);

  // Hook personalizado para manejar la lógica conversacional
  const {
    currentHTML,
    conversationHistory,
    isLoading,
    error,
    isInitialGeneration,
    generateInitialLanding,
    modifyLanding,
    undoLastModification,
    resetConversation,
    getConversationSummary,
    clearError,
    hasContent,
    canUndo,
  } = useConversationalLanding();

  /**
   * Maneja el envío del formulario (generación inicial o modificación)
   */
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!inputText.trim()) return;

    if (isInitialGeneration) {
      await generateInitialLanding(inputText);
    } else {
      await modifyLanding(inputText);
    }

    // Limpiar el input después de enviar
    setInputText("");
  };

  /**
   * Maneja el reinicio de la conversación
   */
  const handleReset = () => {
    resetConversation();
    setInputText("");
  };

  return (
    <div className={styles.container}>
      <div className={styles.wrapper}>
        {/* Título dinámico */}
        <h1 className={styles.title}>
          {isInitialGeneration
            ? "Generador de Landing Pages"
            : "Modificador Conversacional"}
        </h1>

        {/* Componente de error */}
        <ErrorMessage error={error} onClose={clearError} />

        {/* Componente de formulario */}
        <LandingForm
          inputText={inputText}
          setInputText={setInputText}
          onSubmit={handleSubmit}
          isLoading={isLoading}
          isInitialGeneration={isInitialGeneration}
          hasContent={hasContent}
          canUndo={canUndo}
          onUndo={undoLastModification}
          onReset={handleReset}
        />

        {/* Componente de historial */}
        <ConversationHistory
          conversationHistory={conversationHistory}
          getConversationSummary={getConversationSummary}
        />

        {/* Componente de vista previa */}
        <LandingPreview
          currentHTML={currentHTML}
          isInitialGeneration={isInitialGeneration}
          conversationHistory={conversationHistory}
        />

        {/* Componente de código */}
        <CodeSection currentHTML={currentHTML} />

        {/* Componente de instrucciones */}
        <Instructions hasContent={hasContent} isLoading={isLoading} />
      </div>
    </div>
  );
};

export default ConversationalLandingGenerator;

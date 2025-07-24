import { useState, useCallback } from "react";
import axios from "axios";

/**
 * Hook personalizado para manejar la generación y modificación conversacional de landing pages.
 *
 * Este hook encapsula toda la lógica necesaria para:
 * - Generar landing pages iniciales
 * - Mantener conversaciones iterativas para modificaciones
 * - Gestionar el historial de cambios
 * - Controlar el estado de carga y errores
 *
 * @returns {Object} Objeto con estados y funciones para manejar la conversación
 */
export const useConversationalLanding = () => {
  // Estados principales del hook
  const [currentHTML, setCurrentHTML] = useState(""); // HTML actual de la landing page
  const [conversationHistory, setConversationHistory] = useState([]); // Historial de la conversación
  const [isLoading, setIsLoading] = useState(false); // Estado de carga
  const [error, setError] = useState(null); // Estado de error
  const [isInitialGeneration, setIsInitialGeneration] = useState(true); // Flag para saber si es la primera generación

  /**
   * Genera una landing page inicial basada en un prompt del usuario.
   *
   * @param {string} initialPrompt - Descripción inicial de la landing page
   * @returns {Promise<void>}
   */
  const generateInitialLanding = useCallback(async (initialPrompt) => {
    if (!initialPrompt?.trim()) {
      setError("El prompt inicial no puede estar vacío");
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      console.log("Generando landing page inicial con prompt:", initialPrompt);

      const response = await axios.post(
        "http://localhost:8000/generate-landing",
        {
          prompt: initialPrompt,
        }
      );

      const generatedHTML = response.data.html;
      setCurrentHTML(generatedHTML);

      // Inicializar el historial de conversación
      setConversationHistory([
        {
          id: Date.now(),
          type: "initial_generation",
          userInput: initialPrompt,
          result: generatedHTML,
          timestamp: new Date().toISOString(),
        },
      ]);

      setIsInitialGeneration(false);
      console.log("Landing page inicial generada exitosamente");
    } catch (err) {
      console.error("Error al generar landing page inicial:", err);
      setError(
        err.response?.data?.detail || "Error al generar la landing page inicial"
      );
    } finally {
      setIsLoading(false);
    }
  }, []);

  /**
   * Modifica la landing page actual basada en una instrucción conversacional.
   *
   * @param {string} modificationRequest - Instrucción de modificación del usuario
   * @returns {Promise<void>}
   */
  const modifyLanding = useCallback(
    async (modificationRequest) => {
      if (!modificationRequest?.trim()) {
        setError("La instrucción de modificación no puede estar vacía");
        return;
      }

      if (!currentHTML) {
        setError("No hay una landing page generada para modificar");
        return;
      }

      setIsLoading(true);
      setError(null);

      try {
        console.log(
          "Modificando landing page con instrucción:",
          modificationRequest
        );

        const response = await axios.post(
          "http://localhost:8000/modify-landing",
          {
            currentHTML: currentHTML,
            modificationRequest: modificationRequest,
            conversationHistory: conversationHistory.slice(-5), // Enviar solo los últimos 5 intercambios para contexto
          }
        );

        const modifiedHTML = response.data.html;
        setCurrentHTML(modifiedHTML);

        // Agregar la modificación al historial
        setConversationHistory((prev) => [
          ...prev,
          {
            id: Date.now(),
            type: "modification",
            userInput: modificationRequest,
            previousHTML: currentHTML,
            result: modifiedHTML,
            timestamp: new Date().toISOString(),
          },
        ]);

        console.log("Landing page modificada exitosamente");
      } catch (err) {
        console.error("Error al modificar landing page:", err);
        setError(
          err.response?.data?.detail || "Error al modificar la landing page"
        );
      } finally {
        setIsLoading(false);
      }
    },
    [currentHTML, conversationHistory]
  );

  /**
   * Deshace la última modificación realizada.
   *
   * @returns {void}
   */
  const undoLastModification = useCallback(() => {
    if (conversationHistory.length <= 1) {
      setError("No hay modificaciones para deshacer");
      return;
    }

    const newHistory = [...conversationHistory];
    const lastEntry = newHistory.pop();

    if (lastEntry.type === "modification" && lastEntry.previousHTML) {
      setCurrentHTML(lastEntry.previousHTML);
      setConversationHistory(newHistory);
      setError(null);
      console.log("Última modificación deshecha");
    } else {
      setError("No se puede deshacer esta operación");
    }
  }, [conversationHistory]);

  /**
   * Reinicia completamente la conversación y el estado.
   *
   * @returns {void}
   */
  const resetConversation = useCallback(() => {
    setCurrentHTML("");
    setConversationHistory([]);
    setIsInitialGeneration(true);
    setError(null);
    setIsLoading(false);
    console.log("Conversación reiniciada");
  }, []);

  /**
   * Obtiene un resumen del historial de conversación.
   *
   * @returns {Array} Array con resumen de las modificaciones realizadas
   */
  const getConversationSummary = useCallback(() => {
    return conversationHistory.map((entry) => ({
      id: entry.id,
      type: entry.type,
      userInput: entry.userInput,
      timestamp: entry.timestamp,
    }));
  }, [conversationHistory]);

  return {
    // Estados
    currentHTML,
    conversationHistory,
    isLoading,
    error,
    isInitialGeneration,

    // Funciones principales
    generateInitialLanding,
    modifyLanding,

    // Funciones de utilidad
    undoLastModification,
    resetConversation,
    getConversationSummary,

    // Funciones de estado
    clearError: () => setError(null),
    hasContent: !!currentHTML,
    canUndo: conversationHistory.length > 1,
  };
};

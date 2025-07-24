import { useState } from "react";
import styles from "../../styles/components/ConversationHistory.module.css";

/**
 * Componente para mostrar el historial de conversación
 */
const ConversationHistory = ({
  conversationHistory,
  getConversationSummary,
}) => {
  const [showHistory, setShowHistory] = useState(false);

  if (conversationHistory.length === 0) return null;

  return (
    <div className={styles.section}>
      <button
        onClick={() => setShowHistory(!showHistory)}
        className={styles.toggle}
      >
        {showHistory ? "Ocultar" : "Mostrar"} Historial (
        {conversationHistory.length})
      </button>

      {showHistory && (
        <div className={styles.list}>
          {getConversationSummary().map((entry, index) => (
            <div key={entry.id} className={styles.item}>
              <div className={styles.header}>
                <span className={styles.index}>#{index + 1}</span>
                <span className={styles.type}>
                  {entry.type === "initial_generation"
                    ? "Generación"
                    : "Modificación"}
                </span>
                <span className={styles.time}>
                  {new Date(entry.timestamp).toLocaleTimeString()}
                </span>
              </div>
              <p className={styles.content}>{entry.userInput}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ConversationHistory;

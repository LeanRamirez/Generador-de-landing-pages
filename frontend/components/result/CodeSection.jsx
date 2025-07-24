import { useState } from "react";
import LoadingButton from "../ui/LoadingButton";
import styles from "../../styles/components/CodeSection.module.css";

/**
 * Componente para mostrar y copiar el código HTML generado
 */
const CodeSection = ({ currentHTML }) => {
  const [copySuccess, setCopySuccess] = useState(false);

  const handleCopyCode = async () => {
    try {
      await navigator.clipboard.writeText(currentHTML);
      setCopySuccess(true);
      setTimeout(() => setCopySuccess(false), 2000);
    } catch (err) {
      console.error("Error al copiar código:", err);
    }
  };

  if (!currentHTML) return null;

  return (
    <div className={styles.section}>
      <div className={styles.header}>
        <h3 className={styles.title}>Código HTML:</h3>
        <LoadingButton
          onClick={handleCopyCode}
          variant="secondary"
          className={styles.copyButton}
        >
          {copySuccess ? "¡Copiado!" : "Copiar Código"}
        </LoadingButton>
      </div>

      <pre className={styles.codeBlock}>
        <code>{currentHTML}</code>
      </pre>
    </div>
  );
};

export default CodeSection;

import styles from "../../styles/components/LandingPreview.module.css";

/**
 * Componente para mostrar la vista previa de la landing page
 */
const LandingPreview = ({
  currentHTML,
  isInitialGeneration,
  conversationHistory,
}) => {
  if (!currentHTML) return null;

  return (
    <div className={styles.section}>
      <div className={styles.header}>
        <h2 className={styles.title}>
          {isInitialGeneration
            ? "Landing Page Generada:"
            : "Landing Page Actualizada:"}
        </h2>

        {/* Indicador de cambios recientes */}
        {!isInitialGeneration && conversationHistory.length > 1 && (
          <span className={styles.updatedIndicator}>✨ Actualizada</span>
        )}
      </div>

      {/* Vista previa */}
      <div className={styles.previewContainer}>
        <iframe
          srcDoc={currentHTML}
          className={styles.preview}
          title="Vista previa de la landing page"
        />
      </div>
    </div>
  );
};

export default LandingPreview;

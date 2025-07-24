import LoadingButton from "../ui/LoadingButton";
import styles from "../../styles/components/LandingForm.module.css";

/**
 * Componente del formulario para generar/modificar landing pages
 */
const LandingForm = ({
  inputText,
  setInputText,
  onSubmit,
  isLoading,
  isInitialGeneration,
  hasContent,
  canUndo,
  onUndo,
  onReset,
}) => {
  const getPlaceholder = () => {
    if (isInitialGeneration) {
      return "Ejemplo: Una landing page para una empresa de marketing digital con colores azules, sección hero, servicios y contacto...";
    }
    return "Ejemplo: Cambia el color del fondo a verde, Agrega un formulario de contacto, Hazlo responsive...";
  };

  const getButtonText = () => {
    if (isLoading) {
      return isInitialGeneration ? "Generando..." : "Modificando...";
    }
    return isInitialGeneration
      ? "Generar Landing Page"
      : "Aplicar Modificación";
  };

  return (
    <form onSubmit={onSubmit} className={styles.section}>
      <label htmlFor="inputText" className={styles.label}>
        {isInitialGeneration
          ? "Describe tu landing page:"
          : "¿Qué quieres modificar?"}
      </label>

      <textarea
        id="inputText"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder={getPlaceholder()}
        className={styles.textarea}
        rows={isInitialGeneration ? 6 : 3}
        disabled={isLoading}
      />

      <div className={styles.buttonGroup}>
        <LoadingButton
          type="submit"
          loading={isLoading}
          disabled={!inputText.trim()}
          variant="primary"
        >
          {getButtonText()}
        </LoadingButton>

        {hasContent && (
          <>
            {canUndo && (
              <LoadingButton
                type="button"
                onClick={onUndo}
                disabled={isLoading}
                variant="secondary"
              >
                Deshacer
              </LoadingButton>
            )}

            <LoadingButton
              type="button"
              onClick={onReset}
              disabled={isLoading}
              variant="danger"
            >
              Reiniciar
            </LoadingButton>
          </>
        )}
      </div>
    </form>
  );
};

export default LandingForm;

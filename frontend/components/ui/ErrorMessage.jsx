import styles from "../../styles/components/ErrorMessage.module.css";

/**
 * Componente para mostrar mensajes de error con opción de cerrar
 */
const ErrorMessage = ({ error, onClose }) => {
  if (!error) return null;

  return (
    <div className={styles.container}>
      <p className={styles.message}>{error}</p>
      <button onClick={onClose} className={styles.closeButton}>
        ×
      </button>
    </div>
  );
};

export default ErrorMessage;

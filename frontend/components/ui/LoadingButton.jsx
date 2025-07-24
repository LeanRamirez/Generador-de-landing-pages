import styles from "../../styles/components/LoadingButton.module.css";

/**
 * Componente de botón con estado de carga
 */
const LoadingButton = ({
  onClick,
  disabled,
  loading,
  children,
  variant = "primary",
  type = "button",
  className = "",
}) => {
  const buttonClass = `${styles.button} ${styles[variant]} ${className}`;

  return (
    <button
      type={type}
      onClick={onClick}
      className={buttonClass}
      disabled={disabled || loading}
    >
      {loading ? (
        <span className={styles.loadingContent}>
          <span className={styles.spinner}></span>
          {children}
        </span>
      ) : (
        children
      )}
    </button>
  );
};

export default LoadingButton;

import styles from "../../styles/components/Instructions.module.css";

/**
 * Componente para mostrar las instrucciones de uso
 */
const Instructions = ({ hasContent, isLoading }) => {
  if (hasContent || isLoading) return null;

  return (
    <div className={styles.section}>
      <h3 className={styles.title}>¿Cómo funciona?</h3>
      <ol className={styles.list}>
        <li>Describe tu landing page inicial en lenguaje natural</li>
        <li>Una vez generada, puedes pedir modificaciones específicas</li>
        <li>
          Ejemplos: "Cambia el color a azul", "Agrega un formulario", "Hazlo
          responsive"
        </li>
        <li>Cada modificación mantiene el contexto de cambios anteriores</li>
        <li>Puedes deshacer cambios o reiniciar completamente</li>
      </ol>
    </div>
  );
};

export default Instructions;

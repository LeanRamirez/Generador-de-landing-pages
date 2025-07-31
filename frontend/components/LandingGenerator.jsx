// Importaciones necesarias para el componente React
import { useState } from "react"; // Hook de React para manejar estado local del componente
import axios from "axios"; // Biblioteca para realizar peticiones HTTP al backend
import styles from "../styles/LandingGenerator.module.css"; // Estilos CSS modulares específicos del componente
import LandingPreview from "./LandingPreview"; // Componente para mostrar vista previa

const LandingGenerator = () => {
  // Estados del componente usando hooks de React
  const [prompt, setPrompt] = useState(""); // Estado para almacenar el texto del prompt del usuario
  const [generatedHTML, setGeneratedHTML] = useState(""); // Estado para almacenar el HTML generado por la IA
  const [isLoading, setIsLoading] = useState(false); // Estado para controlar el indicador de carga
  const [viewMode, setViewMode] = useState("preview"); // Estado para controlar qué vista mostrar: 'preview' o 'code'

  // Función asíncrona que maneja la generación de la landing page
  const handleGenerate = async () => {
    setIsLoading(true); // Activar indicador de carga
    try {
      // Log para debugging - mostrar el prompt que se está enviando
      console.log("Generando landing page con prompt:", prompt);

      // Realizar petición POST al backend con el prompt del usuario
      const response = await axios.post(
        "http://localhost:8001/api/generate-landing", // URL del endpoint del backend
        {
          prompt: prompt, // Datos a enviar: el prompt del usuario
        }
      );

      // Actualizar el estado con el HTML generado recibido del backend
      setGeneratedHTML(response.data.html);
      console.log("Landing page generada exitosamente"); // Log de éxito
    } catch (error) {
      // Manejo de errores durante la petición
      console.error("Error al generar landing page:", error);
      if (error.response) {
        // Si hay respuesta del servidor, mostrar detalles del error
        console.error("Respuesta del servidor:", error.response.data);
      }
    } finally {
      // Siempre ejecutar al final, sin importar si hubo éxito o error
      setIsLoading(false); // Desactivar indicador de carga
    }
  };

  // Renderizado del componente JSX
  return (
    <div className={styles.container}>
      {/* Contenedor principal con estilos CSS modulares */}
      <div className={styles.wrapper}>
        {/* Título principal de la aplicación */}
        <h1 className={styles.title}>Generador de Landing Pages</h1>

        {/* Sección del formulario para ingresar el prompt */}
        <div className={styles.formSection}>
          <label htmlFor="prompt" className={styles.label}>
            Describe tu landing page:
          </label>
          {/* Textarea para que el usuario ingrese la descripción */}
          <textarea
            id="prompt" // ID para asociar con el label
            value={prompt} // Valor controlado por el estado
            onChange={(e) => setPrompt(e.target.value)} // Actualizar estado cuando cambia el texto
            placeholder="Ejemplo: Una landing page para una empresa de marketing digital con colores azules, sección hero, servicios y contacto..." // Texto de ayuda
            className={styles.textarea} // Estilos CSS
            rows={6} // Número de filas visibles del textarea
          />
        </div>

        {/* Botón para generar la landing page */}
        <button
          onClick={handleGenerate} // Función a ejecutar al hacer clic
          className={styles.generateButton} // Estilos CSS del botón
          disabled={!prompt.trim() || isLoading} // Deshabilitar si no hay texto o está cargando
        >
          {/* Texto dinámico del botón basado en el estado de carga */}
          {isLoading ? "Generando..." : "Generar"}
        </button>

        {/* Sección de resultados - solo se muestra si hay HTML generado */}
        {generatedHTML && (
          <div className={styles.resultSection}>
            <div className={styles.resultHeader}>
              <h2 className={styles.resultTitle}>Landing Page Generada:</h2>

              {/* Botones para cambiar entre vista previa y código */}
              <div className={styles.viewToggle}>
                <button
                  className={`${styles.toggleButton} ${
                    viewMode === "preview" ? styles.active : ""
                  }`}
                  onClick={() => setViewMode("preview")}
                >
                  👁️ Ver Vista Previa
                </button>
                <button
                  className={`${styles.toggleButton} ${
                    viewMode === "code" ? styles.active : ""
                  }`}
                  onClick={() => setViewMode("code")}
                >
                  💻 Ver Código
                </button>
              </div>
            </div>

            {/* Mostrar vista previa o código según el modo seleccionado */}
            {viewMode === "preview" ? (
              <LandingPreview htmlContent={generatedHTML} isVisible={true} />
            ) : (
              <div className={styles.codeSection}>
                <h3 className={styles.codeTitle}>Código HTML:</h3>
                {/* Bloque de código preformateado */}
                <pre className={styles.codeBlock}>
                  <code>{generatedHTML}</code>{" "}
                  {/* Mostrar el HTML como texto */}
                </pre>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

// Exportar el componente para uso en otras partes de la aplicación
export default LandingGenerator;

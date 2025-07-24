// Importar el componente principal de generación de landing pages conversacional
import ConversationalLandingGenerator from "../components/ConversationalLandingGenerator";
import { NavBar } from "../components/navbar/navbar";

// Componente de página principal de Next.js
export default function Home() {
  /**
   * Página principal de la aplicación que renderiza el generador de landing pages.
   *
   * En Next.js, los archivos en la carpeta 'pages' se convierten automáticamente
   * en rutas. Este archivo (index.js) corresponde a la ruta raíz ('/').
   *
   * Returns:
   *   JSX.Element: Elemento JSX que contiene el componente LandingGenerator
   */
  return (
    <>
      <NavBar />
      <ConversationalLandingGenerator />
    </>
  );
}

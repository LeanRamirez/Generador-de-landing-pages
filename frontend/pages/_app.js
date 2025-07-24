// Importar estilos globales que se aplicarán a toda la aplicación
import "../styles/globals.css";

// Componente App principal de Next.js
export default function App({ Component, pageProps }) {
  /**
   * Componente raíz de la aplicación Next.js que envuelve todas las páginas.
   *
   * Este archivo especial de Next.js (_app.js) se ejecuta en cada página
   * y permite configurar elementos globales como estilos, providers, layouts, etc.
   *
   * Args:
   *   Component: El componente de página que se está renderizando actualmente
   *   pageProps: Props que se pasan a la página desde getStaticProps, getServerSideProps, etc.
   *
   * Returns:
   *   JSX.Element: El componente de página con sus props aplicadas
   */
  return <Component {...pageProps} />; // Renderizar la página actual con sus props
}

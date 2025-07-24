/** @type {import('next').NextConfig} */
// Configuración de Next.js para optimizar el rendimiento y desarrollo

const nextConfig = {
  reactStrictMode: true, // Habilita el modo estricto de React para detectar problemas potenciales
  swcMinify: true, // Usa SWC (compilador rápido de Rust) para minificar el código en producción
};

// Exportar la configuración para que Next.js la use
module.exports = nextConfig;

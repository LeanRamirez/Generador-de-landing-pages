# Frontend - Generador de Landing Pages

Este es el frontend del proyecto Generador de Landing Pages, construido con Next.js y React.

## Estructura del Proyecto

```
frontend/
├── components/
│   └── LandingGenerator.jsx    # Componente principal del generador
├── pages/
│   ├── _app.js                 # Configuración global de la app
│   └── index.js                # Página principal
├── styles/
│   ├── globals.css             # Estilos globales
│   └── LandingGenerator.module.css  # Estilos del componente
├── package.json                # Dependencias y scripts
├── next.config.js              # Configuración de Next.js
└── .gitignore                  # Archivos ignorados por Git
```

## Componente LandingGenerator

El componente principal incluye:

- **Textarea controlado**: Para que el usuario escriba el prompt
- **Estado con useState**: Maneja el valor del prompt
- **Botón "Generar"**: Ejecuta la función handleGenerate
- **Validación**: El botón se deshabilita cuando el prompt está vacío
- **Estilos básicos**: Diseño atractivo con gradientes y efectos hover
- **Responsive**: Se adapta a diferentes tamaños de pantalla

## Instalación y Uso

1. Navegar a la carpeta frontend:

```bash
cd frontend
```

2. Instalar dependencias:

```bash
npm install
```

3. Ejecutar en modo desarrollo:

```bash
npm run dev
```

4. Abrir en el navegador: http://localhost:3000

## Dependencias Principales

- **Next.js 14.0.4**: Framework de React
- **React 18**: Biblioteca de UI
- **ESLint**: Linting y formateo de código

## Notas

- Requiere Node.js >= 18.17.0
- El componente está listo para conectar con el backend
- La función `handleGenerate` está preparada para implementar la lógica de generación

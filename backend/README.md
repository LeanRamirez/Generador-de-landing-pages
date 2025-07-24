# Backend - Generador de Landing Pages

Este es el backend del proyecto Generador de Landing Pages, construido con FastAPI y Python.

## Estructura del Proyecto

```
backend/
├── routes/
│   └── generate.py             # Rutas de la API
├── schemas/
│   └── prompt_schema.py        # Esquemas de validación
├── services/
│   └── generate_code.py        # Lógica de generación con IA
├── main.py                     # Aplicación principal FastAPI
└── README.md                   # Este archivo
```

## Funcionalidades

- **API REST**: Endpoint para generar landing pages
- **Integración con OpenAI**: Usa GPT para generar código HTML/CSS
- **Validación de datos**: Esquemas con Pydantic
- **CORS habilitado**: Para comunicación con el frontend
- **Manejo de errores**: Respuestas estructuradas

## Endpoints

### POST /generate

Genera una landing page basada en un prompt.

**Request Body:**

```json
{
  "prompt": "Una landing page para una empresa de marketing digital..."
}
```

**Response:**

```json
{
  "html_code": "<html>...</html>",
  "message": "Landing page generada exitosamente"
}
```

## Instalación y Uso

1. Navegar a la carpeta raíz del proyecto:

```bash
cd ..
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:

```bash
# Crear archivo .env en la raíz del proyecto
OPENAI_API_KEY=tu_api_key_aqui
```

4. Ejecutar el servidor:

```bash
python run_server.py
```

5. La API estará disponible en: http://localhost:8000

## Dependencias Principales

- **FastAPI**: Framework web moderno y rápido
- **OpenAI**: Cliente para la API de OpenAI
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI

## Archivos de Prueba

- `test_api.py`: Prueba la funcionalidad de la API
- `demo_landing.py`: Genera una landing page de demostración

## Notas

- Requiere una API key válida de OpenAI
- El servidor se ejecuta en el puerto 8000 por defecto
- Incluye manejo de errores para cuota excedida de OpenAI

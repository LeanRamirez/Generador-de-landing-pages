# Generador de Landing Pages con IA

Un generador automático de landing pages usando inteligencia artificial (OpenAI GPT) que crea páginas web completas basadas en descripciones de texto.

## 🚀 Características

- **Generación automática**: Crea landing pages completas con solo una descripción
- **IA avanzada**: Utiliza OpenAI GPT para generar código HTML y CSS optimizado
- **API REST**: Backend con FastAPI para fácil integración
- **Interfaz moderna**: Frontend con Next.js y React
- **Responsive**: Las páginas generadas se adaptan a todos los dispositivos
- **Personalizable**: Modifica fácilmente los prompts para diferentes estilos

## 📋 Requisitos

- Python 3.8+
- Node.js 18.17.0+
- API Key de OpenAI
- Git

## 📁 Estructura del Proyecto

```
generador-de-landing-pages/
├── backend/                    # API con FastAPI
│   ├── routes/
│   │   └── generate.py
│   ├── schemas/
│   │   └── prompt_schema.py
│   ├── services/
│   │   └── generate_code.py
│   ├── main.py
│   └── README.md
├── frontend/                   # Aplicación Next.js
│   ├── components/
│   │   └── LandingGenerator.jsx
│   ├── pages/
│   │   ├── _app.js
│   │   └── index.js
│   ├── styles/
│   │   ├── globals.css
│   │   └── LandingGenerator.module.css
│   ├── package.json
│   ├── next.config.js
│   └── README.md
├── .env                        # Variables de entorno
├── requirements.txt            # Dependencias Python
├── run_server.py              # Script para ejecutar backend
├── test_api.py                # Pruebas de la API
├── demo_landing.py            # Demo sin API
├── test-component.html        # Prueba del componente
└── README.md                  # Este archivo
```

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd generador-de-landing-pages
```

### 2. Configurar el Backend

```bash
# Instalar dependencias de Python
pip install -r requirements.txt

# Configurar variables de entorno
# Crear archivo .env y agregar tu OPENAI_API_KEY
echo "OPENAI_API_KEY=tu_api_key_aqui" > .env
```

### 3. Configurar el Frontend

```bash
# Navegar a la carpeta frontend
cd frontend

# Instalar dependencias de Node.js
npm install

# Volver a la raíz
cd ..
```

## 🚀 Uso

### Ejecutar el Backend

```bash
python run_server.py
```

El servidor estará disponible en: http://localhost:8000

### Ejecutar el Frontend

```bash
cd frontend
npm run dev
```

La aplicación estará disponible en: http://localhost:3000

### Probar la API directamente

```bash
python test_api.py
```

### Generar una landing page de demostración

```bash
python demo_landing.py
```

### Probar el componente sin servidor

Abrir `test-component.html` en el navegador para ver el componente funcionando.

## 🔧 API Endpoints

### POST /generate

Genera una landing page basada en un prompt de texto.

**Request:**

```json
{
  "prompt": "Una landing page para una empresa de marketing digital con colores azules, sección hero, servicios y contacto"
}
```

**Response:**

```json
{
  "html_code": "<html>...</html>",
  "message": "Landing page generada exitosamente"
}
```

## 🎨 Ejemplos de Prompts

- "Una landing page minimalista para una startup de tecnología con colores oscuros"
- "Página de venta para un curso online de cocina con testimonios y precios"
- "Landing page corporativa para una consultora con secciones de servicios y equipo"
- "Página promocional para una app móvil con screenshots y botones de descarga"

## 🛠️ Tecnologías Utilizadas

### Backend

- **FastAPI**: Framework web moderno y rápido
- **OpenAI**: API de inteligencia artificial
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI

### Frontend

- **Next.js**: Framework de React
- **React**: Biblioteca de interfaz de usuario
- **CSS Modules**: Estilos modulares

## 📝 Configuración

### Variables de Entorno (.env)

```env
OPENAI_API_KEY=tu_api_key_de_openai_aqui
```

### Obtener API Key de OpenAI

1. Visita https://platform.openai.com/
2. Crea una cuenta o inicia sesión
3. Ve a "API Keys" en tu dashboard
4. Crea una nueva API key
5. Cópiala al archivo .env

## 🧪 Testing

### Probar el Backend

```bash
python test_api.py
```

### Generar Landing de Prueba

```bash
python demo_landing.py
```

### Probar el Frontend

```bash
# Abrir en navegador
start test-component.html
```

## 📚 Documentación Adicional

- [Backend README](./backend/README.md) - Documentación detallada del API
- [Frontend README](./frontend/README.md) - Documentación del componente React

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 🆘 Solución de Problemas

### Backend

- **Error de API Key**: Verifica que `OPENAI_API_KEY` esté en el archivo `.env`
- **Error de cuota**: Agrega créditos a tu cuenta de OpenAI
- **Puerto ocupado**: Cambia el puerto en `run_server.py`

### Frontend

- **Error de Node.js**: Requiere versión >= 18.17.0
- **Error de dependencias**: Ejecuta `npm install` en la carpeta `frontend/`
- **Error de conexión**: Verifica que el backend esté ejecutándose en puerto 8000

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🔮 Roadmap

- [ ] Más plantillas predefinidas
- [ ] Editor visual de componentes
- [ ] Integración con más proveedores de IA
- [ ] Sistema de usuarios y guardado
- [ ] Exportación a diferentes formatos
- [ ] Optimización SEO automática

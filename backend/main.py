# Importaciones necesarias para crear la aplicación FastAPI
from fastapi import FastAPI  # Framework web principal para crear la API REST
from fastapi.middleware.cors import CORSMiddleware  # Middleware para manejar CORS (Cross-Origin Resource Sharing)
from routes.generate import router as generar_router  # Importa el router que contiene las rutas de generación
from routes.modify import router as modificar_router  # Importa el router que contiene las rutas de modificación conversacional

# Crear la instancia principal de la aplicación FastAPI con un título descriptivo
app = FastAPI(title="Generador IA de Landing Pages")

# Configurar middleware CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen (en producción usar dominios específicos)
    allow_credentials=True,  # Permite el envío de cookies y credenciales
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los headers en las peticiones
)

# Incluir el router de generación que contiene los endpoints para generar landing pages
app.include_router(generar_router)

# Incluir el router de modificación que contiene los endpoints para modificaciones conversacionales
app.include_router(modificar_router)

# Endpoint raíz que sirve como health check para verificar que la API está funcionando
@app.get("/")
def read_root():
    """
    Endpoint de prueba que confirma que la API está funcionando correctamente.
    
    Returns:
        dict: Mensaje de confirmación del estado de la API
    """
    return {"message": "Generador IA de Landing Pages - API funcionando correctamente"}

# Punto de entrada principal cuando se ejecuta el archivo directamente
if __name__ == "__main__":
    import uvicorn  # Servidor ASGI para ejecutar aplicaciones FastAPI
    # Ejecutar la aplicación en todas las interfaces (0.0.0.0) en el puerto 8001
    uvicorn.run(app, host="0.0.0.0", port=8001)

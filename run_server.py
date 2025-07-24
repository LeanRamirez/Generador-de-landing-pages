# Importar uvicorn, el servidor ASGI para ejecutar aplicaciones FastAPI
import uvicorn

# Script principal para ejecutar el servidor del backend
if __name__ == "__main__":
    # Mostrar información útil al usuario sobre el servidor
    print("Iniciando servidor del Generador IA de Landing Pages...")
    print("Servidor disponible en: http://localhost:8000")  # URL principal de la API
    print("Documentación API en: http://localhost:8000/docs")  # Documentación automática de FastAPI
    print("Para detener el servidor, presiona Ctrl+C")  # Instrucciones para detener
    
    # Ejecutar el servidor uvicorn con la aplicación FastAPI
    uvicorn.run(
        "backend.main:app",  # Ruta al objeto app en el módulo backend.main
        host="0.0.0.0",      # Escuchar en todas las interfaces de red
        port=8000,           # Puerto donde se ejecutará el servidor
        reload=True          # Reiniciar automáticamente cuando se detecten cambios en el código
    )

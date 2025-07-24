# Importaciones necesarias para realizar pruebas de la API
import requests  # Biblioteca para realizar peticiones HTTP
import json      # Biblioteca para manejar datos JSON (aunque no se usa directamente aquí)

def test_api():
    """
    Script de pruebas para verificar que la API del generador funciona correctamente.
    
    Esta función realiza dos pruebas principales:
    1. Verificar que el servidor esté funcionando (health check)
    2. Probar la generación de una landing page con un prompt de ejemplo
    
    No requiere parámetros y muestra los resultados en la consola.
    """
    
    # URL base del servidor donde se ejecuta la API
    base_url = "http://localhost:8000"
    
    # Mostrar encabezado de las pruebas
    print("🧪 Probando el Generador IA de Landing Pages...")
    print("=" * 50)
    
    # Test 1: Verificar que el servidor esté funcionando (health check)
    try:
        # Realizar petición GET al endpoint raíz
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            # Servidor responde correctamente
            print("✅ Servidor funcionando correctamente")
            print(f"   Respuesta: {response.json()}")  # Mostrar mensaje de respuesta
        else:
            # Servidor responde pero con error
            print("❌ Error en el servidor")
            return  # Terminar las pruebas si el servidor no funciona
    except requests.exceptions.ConnectionError:
        # No se puede conectar al servidor
        print("❌ No se puede conectar al servidor. ¿Está ejecutándose?")
        print("   Ejecuta: python run_server.py")
        return  # Terminar las pruebas si no hay conexión
    
    # Test 2: Probar la generación de landing page
    print("\n🚀 Probando generación de landing page...")
    
    # Prompt de prueba para generar una landing page
    test_prompt = "Crea una landing page para una empresa de tecnología con colores azules y un diseño moderno"
    
    # Preparar los datos a enviar en formato JSON
    payload = {
        "prompt": test_prompt
    }
    
    try:
        # Realizar petición POST al endpoint de generación
        response = requests.post(
            f"{base_url}/generate-landing",  # URL del endpoint
            json=payload,                    # Datos en formato JSON
            headers={"Content-Type": "application/json"}  # Header para indicar tipo de contenido
        )
        
        if response.status_code == 200:
            # Generación exitosa
            result = response.json()  # Parsear respuesta JSON
            print("✅ Landing page generada exitosamente")
            print(f"   Status: {result.get('status', 'N/A')}")  # Mostrar estado
            
            # Guardar el HTML generado en un archivo para revisión manual
            if 'html' in result:
                with open('test_landing.html', 'w', encoding='utf-8') as f:
                    f.write(result['html'])  # Escribir HTML al archivo
                print("   📄 HTML guardado en: test_landing.html")
            
        else:
            # Error en la generación
            print(f"❌ Error al generar landing page: {response.status_code}")
            print(f"   Respuesta: {response.text}")  # Mostrar detalles del error
            
    except Exception as e:
        # Capturar cualquier excepción durante la prueba
        print(f"❌ Error durante la prueba: {str(e)}")
    
    # Mostrar mensaje de finalización
    print("\n" + "=" * 50)
    print("🏁 Pruebas completadas")

# Punto de entrada del script
if __name__ == "__main__":
    test_api()  # Ejecutar las pruebas cuando se ejecuta el archivo directamente

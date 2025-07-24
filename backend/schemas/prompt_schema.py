# Importación de BaseModel de Pydantic para validación de datos
from pydantic import BaseModel  # Clase base para crear modelos de validación de datos

class PromptRequest(BaseModel):
    """
    Modelo de validación para las peticiones de generación de landing pages.
    
    Este modelo define la estructura y validación de los datos que debe enviar
    el cliente cuando solicita la generación de una landing page.
    
    Attributes:
        prompt (str): Texto descriptivo que el usuario proporciona para generar
                     la landing page. Debe ser una cadena de texto que describa
                     las características deseadas de la página web.
    """
    prompt: str  # Campo obligatorio que contiene la descripción de la landing page a generar

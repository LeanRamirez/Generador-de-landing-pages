"""
Cliente configurado de OpenAI para la aplicación.

Este módulo proporciona una instancia configurada del cliente de OpenAI
y funciones helper para interactuar con la API.
"""

import os
import httpx
from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional

# Cargar variables de entorno
load_dotenv()


class OpenAIClientManager:
    """
    Gestor del cliente de OpenAI con configuración optimizada.
    """
    
    def __init__(self):
        self._client: Optional[OpenAI] = None
        self._http_client: Optional[httpx.Client] = None
    
    def get_client(self) -> OpenAI:
        """
        Obtiene una instancia configurada del cliente de OpenAI.
        
        Returns:
            OpenAI: Cliente configurado
            
        Raises:
            ValueError: Si la API key no está configurada
        """
        if self._client is None:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError("OPENAI_API_KEY no está configurada en el archivo .env")
            
            # Crear cliente HTTP personalizado
            self._http_client = httpx.Client(
                timeout=60.0,
                follow_redirects=True
            )
            
            # Crear cliente de OpenAI
            self._client = OpenAI(
                api_key=api_key,
                http_client=self._http_client,
                timeout=60.0
            )
        
        return self._client
    
    def close(self):
        """
        Cierra las conexiones del cliente.
        """
        if self._http_client:
            self._http_client.close()
            self._http_client = None
        self._client = None


# Instancia global del gestor
_client_manager = OpenAIClientManager()


def get_openai_client() -> OpenAI:
    """
    Función helper para obtener el cliente de OpenAI.
    
    Returns:
        OpenAI: Cliente configurado
    """
    return _client_manager.get_client()


def close_openai_client():
    """
    Función helper para cerrar el cliente de OpenAI.
    """
    _client_manager.close()


def create_chat_completion(
    messages: list,
    model: str = "gpt-3.5-turbo",
    temperature: float = 0.3,
    max_tokens: int = 4000
) -> str:
    """
    Crea una completion de chat con parámetros optimizados.
    
    Args:
        messages (list): Lista de mensajes para la conversación
        model (str): Modelo a utilizar
        temperature (float): Temperatura para la generación
        max_tokens (int): Máximo número de tokens
        
    Returns:
        str: Respuesta generada por el modelo
        
    Raises:
        Exception: Si hay errores en la API de OpenAI
    """
    client = get_openai_client()
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        # Re-lanzar la excepción para que sea manejada por el caller
        raise e
    
    finally:
        # No cerrar el cliente aquí para reutilización
        pass


def build_system_message(role_description: str) -> dict:
    """
    Construye un mensaje de sistema estandarizado.
    
    Args:
        role_description (str): Descripción del rol del asistente
        
    Returns:
        dict: Mensaje de sistema formateado
    """
    return {
        "role": "system",
        "content": role_description
    }


def build_user_message(content: str) -> dict:
    """
    Construye un mensaje de usuario estandarizado.
    
    Args:
        content (str): Contenido del mensaje
        
    Returns:
        dict: Mensaje de usuario formateado
    """
    return {
        "role": "user",
        "content": content
    }

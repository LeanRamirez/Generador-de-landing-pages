"""
Servicio para la generación de landing pages usando OpenAI.

Este módulo contiene la lógica para generar código HTML/CSS completo
de landing pages basado en descripciones en lenguaje natural.
"""

from ..utils.openai_client import create_chat_completion, build_system_message, build_user_message
from ..utils.error_handlers import handle_openai_error, validate_required_fields


def generar_landing(prompt_usuario: str) -> str:
    """
    Genera una landing page completa usando la API de OpenAI GPT-3.5-turbo.
    
    Esta función toma un prompt del usuario y utiliza inteligencia artificial
    para generar código HTML y CSS completo de una landing page moderna.
    
    Args:
        prompt_usuario (str): Descripción de la landing page que el usuario desea generar
        
    Returns:
        str: Código HTML completo con CSS embebido listo para usar
        
    Raises:
        HTTPException: Para errores de validación o de la API de OpenAI
    """
    
    # Validar que el prompt no esté vacío
    validate_required_fields({"prompt": prompt_usuario}, ["prompt"])
    
    # Construir el prompt completo con instrucciones específicas
    prompt_completo = _build_generation_prompt(prompt_usuario)
    
    # Construir mensajes para la API
    messages = [
        build_system_message(_get_system_role()),
        build_user_message(prompt_completo)
    ]
    
    try:
        # Generar contenido usando el cliente modular
        return create_chat_completion(
            messages=messages,
            model="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=4000
        )
        
    except Exception as e:
        # Manejar errores usando el handler modular
        raise handle_openai_error(str(e))


def _get_system_role() -> str:
    """
    Obtiene la descripción del rol del sistema para la generación.
    
    Returns:
        str: Descripción del rol del asistente
    """
    return """Eres un experto desarrollador web que crea landing pages modernas y atractivas.
    
    Características de tu trabajo:
    - Diseños modernos y responsivos
    - Código HTML limpio y semántico
    - CSS embebido optimizado
    - Colores atractivos y tipografía legible
    - Compatibilidad cross-browser
    - Accesibilidad básica implementada"""


def _build_generation_prompt(prompt_usuario: str) -> str:
    """
    Construye el prompt completo para la generación de landing pages.
    
    Args:
        prompt_usuario (str): Descripción del usuario
        
    Returns:
        str: Prompt completo con instrucciones
    """
    return f"""
    Generá una landing page completa y moderna en HTML + CSS.
    Requisitos del usuario: {prompt_usuario}
    
    Instrucciones técnicas:
    - Incluí todo el CSS dentro de etiquetas <style> en el <head>
    - Usá un diseño moderno y responsivo (mobile-first)
    - Incluí colores atractivos y tipografía legible
    - Implementá hover effects y transiciones suaves
    - Asegurate de que sea accesible (alt texts, semantic HTML)
    - Optimizá para velocidad de carga
    - No expliques nada, solo devolvé el código HTML completo
    - El código debe estar listo para usar directamente en un navegador
    
    Estructura recomendada:
    - Header con navegación
    - Sección hero principal
    - Secciones de contenido según los requisitos
    - Footer con información de contacto
    """


def validate_generation_request(prompt: str) -> None:
    """
    Valida una petición de generación de landing page.
    
    Args:
        prompt (str): Prompt del usuario a validar
        
    Raises:
        HTTPException: Si la validación falla
    """
    # Validar longitud mínima
    if len(prompt.strip()) < 10:
        from ..utils.error_handlers import handle_validation_error
        raise handle_validation_error(
            "prompt", 
            "Debe tener al menos 10 caracteres para generar una landing page útil"
        )
    
    # Validar longitud máxima
    if len(prompt.strip()) > 1000:
        from ..utils.error_handlers import handle_validation_error
        raise handle_validation_error(
            "prompt", 
            "Debe tener menos de 1000 caracteres para evitar timeouts"
        )


def get_generation_examples() -> list:
    """
    Obtiene ejemplos de prompts para la generación.
    
    Returns:
        list: Lista de ejemplos de prompts
    """
    return [
        "Una landing page para una empresa de marketing digital con colores azules, sección hero, servicios y contacto",
        "Landing page para un restaurante italiano con galería de platos, menú y reservas online",
        "Página de producto para una app móvil de fitness con testimonios y descarga",
        "Landing page para un curso online de programación con precios y testimonios",
        "Página corporativa para una consultora con equipo, servicios y casos de éxito"
    ]

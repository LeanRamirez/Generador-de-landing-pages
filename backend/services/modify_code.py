"""
Servicio para la modificación conversacional de landing pages usando OpenAI.

Este módulo contiene la lógica para modificar código HTML/CSS existente
basado en instrucciones conversacionales del usuario.
"""

from typing import List
from ..schemas.modification_schema import ConversationEntry
from ..utils.openai_client import create_chat_completion, build_system_message, build_user_message
from ..utils.error_handlers import handle_openai_error, validate_required_fields


def modificar_landing_conversacional(
    codigo_actual: str,
    instruccion_modificacion: str,
    historial_conversacion: List[ConversationEntry]
) -> tuple[str, str]:
    """
    Modifica una landing page existente basándose en instrucciones conversacionales.
    
    Args:
        codigo_actual (str): Código HTML actual de la landing page
        instruccion_modificacion (str): Instrucción de modificación del usuario
        historial_conversacion (List[ConversationEntry]): Historial de la conversación
        
    Returns:
        tuple[str, str]: (código_modificado, análisis_de_cambios)
        
    Raises:
        HTTPException: Para errores de validación o de la API de OpenAI
    """
    
    # Validar inputs requeridos
    validate_required_fields({
        "codigo_actual": codigo_actual,
        "instruccion_modificacion": instruccion_modificacion
    }, ["codigo_actual", "instruccion_modificacion"])
    
    # Construir contexto conversacional
    contexto_conversacion = _build_conversation_context(historial_conversacion)
    
    # Construir prompt de modificación
    prompt_modificacion = _build_modification_prompt(
        codigo_actual, 
        instruccion_modificacion, 
        contexto_conversacion
    )
    
    # Construir mensajes para la API
    messages = [
        build_system_message(_get_modification_system_role()),
        build_user_message(prompt_modificacion)
    ]
    
    try:
        # Generar modificación usando el cliente modular
        respuesta_completa = create_chat_completion(
            messages=messages,
            model="gpt-3.5-turbo",
            temperature=0.3,  # Temperatura baja para modificaciones precisas
            max_tokens=4000
        )
        
        # Separar código y análisis
        return _parse_modification_response(respuesta_completa)
        
    except Exception as e:
        # Manejar errores usando el handler modular
        raise handle_openai_error(str(e))


def _get_modification_system_role() -> str:
    """
    Obtiene la descripción del rol del sistema para modificaciones.
    
    Returns:
        str: Descripción del rol del asistente para modificaciones
    """
    return """Eres un experto desarrollador web especializado en modificaciones precisas de landing pages.

    Tu trabajo es:
    - Analizar código HTML/CSS existente
    - Aplicar modificaciones específicas manteniendo la estructura
    - Conservar elementos que no necesitan cambios
    - Mantener la funcionalidad y responsividad
    - Proporcionar análisis claro de los cambios realizados
    
    Principios importantes:
    - Modificar solo lo necesario según la instrucción
    - Mantener la coherencia visual y funcional
    - Preservar la accesibilidad y responsividad
    - Aplicar mejores prácticas de desarrollo web"""


def _build_conversation_context(historial: List[ConversationEntry]) -> str:
    """
    Construye el contexto conversacional para mantener coherencia.
    
    Args:
        historial (List[ConversationEntry]): Historial de conversación
        
    Returns:
        str: Contexto conversacional formateado
    """
    if not historial:
        return "Esta es la primera modificación de la landing page."
    
    # Tomar las últimas 5 entradas para mantener contexto relevante
    entradas_recientes = historial[-5:]
    
    contexto_lines = ["Contexto de modificaciones anteriores:"]
    
    for i, entrada in enumerate(entradas_recientes, 1):
        tipo = "Generación inicial" if entrada.type == "initial_generation" else "Modificación"
        contexto_lines.append(f"{i}. {tipo}: {entrada.userInput}")
    
    return "\n".join(contexto_lines)


def _build_modification_prompt(
    codigo_actual: str, 
    instruccion: str, 
    contexto: str
) -> str:
    """
    Construye el prompt completo para la modificación.
    
    Args:
        codigo_actual (str): Código HTML actual
        instruccion (str): Instrucción de modificación
        contexto (str): Contexto conversacional
        
    Returns:
        str: Prompt completo para la modificación
    """
    return f"""
    {contexto}

    CÓDIGO ACTUAL:
    {codigo_actual}

    INSTRUCCIÓN DE MODIFICACIÓN:
    {instruccion}

    INSTRUCCIONES PARA LA MODIFICACIÓN:
    1. Analiza el código actual y la instrucción de modificación
    2. Aplica ÚNICAMENTE los cambios solicitados
    3. Mantén todo el resto del código intacto
    4. Conserva la estructura, funcionalidad y responsividad
    5. Asegúrate de que el resultado sea válido y funcional

    FORMATO DE RESPUESTA REQUERIDO:
    CÓDIGO_MODIFICADO:
    [Aquí el código HTML completo modificado]

    ANÁLISIS_DE_CAMBIOS:
    [Aquí una explicación breve de los cambios realizados]

    IMPORTANTE: 
    - Devuelve el código HTML COMPLETO, no solo las partes modificadas
    - Mantén toda la funcionalidad existente
    - Solo modifica lo específicamente solicitado
    """


def _parse_modification_response(respuesta: str) -> tuple[str, str]:
    """
    Parsea la respuesta de modificación separando código y análisis.
    
    Args:
        respuesta (str): Respuesta completa de la API
        
    Returns:
        tuple[str, str]: (código_modificado, análisis_de_cambios)
    """
    try:
        # Buscar los marcadores en la respuesta
        if "CÓDIGO_MODIFICADO:" in respuesta and "ANÁLISIS_DE_CAMBIOS:" in respuesta:
            partes = respuesta.split("CÓDIGO_MODIFICADO:")
            if len(partes) > 1:
                resto = partes[1]
                if "ANÁLISIS_DE_CAMBIOS:" in resto:
                    codigo_y_analisis = resto.split("ANÁLISIS_DE_CAMBIOS:")
                    codigo = codigo_y_analisis[0].strip()
                    analisis = codigo_y_analisis[1].strip() if len(codigo_y_analisis) > 1 else "Modificación aplicada"
                    return codigo, analisis
        
        # Fallback: si no se encuentran los marcadores, usar toda la respuesta como código
        return respuesta.strip(), "Modificación aplicada según instrucciones"
        
    except Exception:
        # En caso de error en el parsing, devolver la respuesta completa
        return respuesta.strip(), "Modificación aplicada"


def validate_modification_request(
    codigo_actual: str, 
    instruccion: str
) -> None:
    """
    Valida una petición de modificación.
    
    Args:
        codigo_actual (str): Código actual a validar
        instruccion (str): Instrucción de modificación a validar
        
    Raises:
        HTTPException: Si la validación falla
    """
    # Validar longitud mínima del código
    if len(codigo_actual.strip()) < 100:
        from ..utils.error_handlers import handle_validation_error
        raise handle_validation_error(
            "codigo_actual", 
            "El código actual debe tener al menos 100 caracteres"
        )
    
    # Validar que sea HTML válido básico
    if not ("<html" in codigo_actual.lower() or "<!doctype" in codigo_actual.lower()):
        from ..utils.error_handlers import handle_validation_error
        raise handle_validation_error(
            "codigo_actual", 
            "El código debe ser HTML válido"
        )
    
    # Validar longitud de la instrucción
    if len(instruccion.strip()) < 5:
        from ..utils.error_handlers import handle_validation_error
        raise handle_validation_error(
            "instruccion", 
            "La instrucción debe tener al menos 5 caracteres"
        )
    
    if len(instruccion.strip()) > 500:
        from ..utils.error_handlers import handle_validation_error
        raise handle_validation_error(
            "instruccion", 
            "La instrucción debe tener menos de 500 caracteres"
        )


def get_modification_examples() -> list:
    """
    Obtiene ejemplos de instrucciones de modificación.
    
    Returns:
        list: Lista de ejemplos de modificaciones
    """
    return [
        "Cambia el color del fondo a azul",
        "Agrega un formulario de contacto en la sección hero",
        "Modifica el título principal por 'Bienvenidos a nuestra empresa'",
        "Hazlo responsive para dispositivos móviles",
        "Agrega una sección de testimonios después del hero",
        "Cambia la tipografía a una más moderna",
        "Incluye botones de redes sociales en el footer",
        "Modifica los colores para que sean más profesionales"
    ]

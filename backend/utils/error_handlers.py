"""
Utilidades para el manejo de errores en la aplicación.

Este módulo contiene funciones helper para manejar diferentes tipos de errores
de manera consistente en toda la aplicación.
"""

from fastapi import HTTPException
from typing import Dict, Any


def handle_openai_error(error_message: str) -> HTTPException:
    """
    Maneja errores específicos de OpenAI y retorna HTTPException apropiada.
    
    Args:
        error_message (str): Mensaje de error original
        
    Returns:
        HTTPException: Excepción HTTP con código y mensaje apropiados
    """
    error_lower = error_message.lower()
    
    if "insufficient_quota" in error_lower:
        return HTTPException(
            status_code=500,
            detail="Error: Has excedido tu cuota de OpenAI. Verifica tu plan y detalles de facturación."
        )
    elif "invalid_api_key" in error_lower:
        return HTTPException(
            status_code=500,
            detail="Error: API key de OpenAI inválida. Verifica tu configuración."
        )
    elif "rate_limit" in error_lower:
        return HTTPException(
            status_code=429,
            detail="Error: Límite de velocidad excedido. Intenta nuevamente en unos momentos."
        )
    elif "model_not_found" in error_lower:
        return HTTPException(
            status_code=500,
            detail="Error: Modelo no encontrado. Verifica que el modelo esté disponible."
        )
    else:
        return HTTPException(
            status_code=500,
            detail=f"Error en el servicio de IA: {error_message}"
        )


def handle_validation_error(field_name: str, message: str = None) -> HTTPException:
    """
    Maneja errores de validación de campos.
    
    Args:
        field_name (str): Nombre del campo que falló la validación
        message (str, optional): Mensaje personalizado de error
        
    Returns:
        HTTPException: Excepción HTTP 400 con mensaje descriptivo
    """
    if message:
        detail = f"Error de validación en {field_name}: {message}"
    else:
        detail = f"El campo {field_name} no puede estar vacío"
    
    return HTTPException(status_code=400, detail=detail)


def handle_generic_error(error: Exception, context: str = "operación") -> HTTPException:
    """
    Maneja errores genéricos no específicos.
    
    Args:
        error (Exception): Excepción original
        context (str): Contexto donde ocurrió el error
        
    Returns:
        HTTPException: Excepción HTTP 500 con mensaje descriptivo
    """
    return HTTPException(
        status_code=500,
        detail=f"Error interno durante {context}: {str(error)}"
    )


def create_success_response(data: Any, message: str = "Operación exitosa") -> Dict[str, Any]:
    """
    Crea una respuesta de éxito estandarizada.
    
    Args:
        data (Any): Datos a incluir en la respuesta
        message (str): Mensaje de éxito
        
    Returns:
        Dict[str, Any]: Respuesta estructurada
    """
    return {
        "status": "success",
        "message": message,
        "data": data
    }


def validate_required_fields(data: Dict[str, Any], required_fields: list) -> None:
    """
    Valida que los campos requeridos estén presentes y no vacíos.
    
    Args:
        data (Dict[str, Any]): Datos a validar
        required_fields (list): Lista de campos requeridos
        
    Raises:
        HTTPException: Si algún campo requerido falta o está vacío
    """
    for field in required_fields:
        if field not in data or not data[field] or str(data[field]).strip() == "":
            raise handle_validation_error(field)

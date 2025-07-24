"""
Rutas para la modificación conversacional de landing pages.

Este módulo contiene los endpoints relacionados con la modificación
iterativa de landing pages usando inteligencia artificial.
"""

from fastapi import APIRouter
from typing import List
from ..schemas.modification_schema import ModificationRequest, ModificationResponse, ConversationEntry
from ..services.modify_code import (
    modificar_landing_conversacional, 
    validate_modification_request,
    get_modification_examples
)
from ..utils.error_handlers import handle_generic_error, create_success_response


# Crear router para las rutas de modificación
router = APIRouter(
    prefix="/api",
    tags=["modification"],
    responses={
        400: {"description": "Error de validación"},
        500: {"description": "Error interno del servidor"}
    }
)


@router.post("/modify-landing", response_model=ModificationResponse)
async def modificar_landing_route(data: ModificationRequest):
    """
    Endpoint para modificar una landing page existente de forma conversacional.
    
    Args:
        data (ModificationRequest): Datos de la petición de modificación
        
    Returns:
        ModificationResponse: Respuesta con el código modificado y análisis
        
    Raises:
        HTTPException: Para errores de validación o modificación
    """
    try:
        # Validar la petición usando el validador modular
        validate_modification_request(
            data.current_html, 
            data.modification_instruction
        )
        
        # Realizar la modificación usando el servicio modular
        codigo_modificado, analisis_cambios = modificar_landing_conversacional(
            codigo_actual=data.current_html,
            instruccion_modificacion=data.modification_instruction,
            historial_conversacion=data.conversation_history or []
        )
        
        # Crear respuesta estructurada
        response = ModificationResponse(
            modified_html=codigo_modificado,
            changes_analysis=analisis_cambios,
            success=True,
            message="Modificación aplicada exitosamente"
        )
        
        return response
        
    except Exception as e:
        # Manejar errores usando el handler modular
        if hasattr(e, 'status_code'):
            # Si ya es una HTTPException, re-lanzarla
            raise e
        else:
            # Convertir a HTTPException usando el handler
            raise handle_generic_error(e, "modificación de landing page")


@router.get("/modify-examples")
async def get_modification_examples():
    """
    Endpoint para obtener ejemplos de instrucciones de modificación.
    
    Returns:
        dict: Lista de ejemplos de modificaciones
    """
    try:
        examples = get_modification_examples()
        
        return create_success_response(
            data={"examples": examples},
            message="Ejemplos de modificación obtenidos exitosamente"
        )
        
    except Exception as e:
        raise handle_generic_error(e, "obtención de ejemplos de modificación")


@router.post("/validate-modification")
async def validate_modification_route(data: ModificationRequest):
    """
    Endpoint para validar una petición de modificación sin ejecutarla.
    
    Args:
        data (ModificationRequest): Datos a validar
        
    Returns:
        dict: Resultado de la validación
    """
    try:
        # Validar usando el validador modular
        validate_modification_request(
            data.current_html, 
            data.modification_instruction
        )
        
        return create_success_response(
            data={"valid": True},
            message="Petición de modificación válida"
        )
        
    except Exception as e:
        if hasattr(e, 'status_code'):
            raise e
        else:
            raise handle_generic_error(e, "validación de modificación")


# Endpoints preparados para funcionalidades futuras
@router.get("/conversation-history/{conversation_id}")
async def get_conversation_history(conversation_id: str):
    """
    Endpoint para obtener el historial de una conversación específica.
    
    Args:
        conversation_id (str): ID de la conversación
        
    Returns:
        dict: Historial de la conversación
        
    Note:
        Este endpoint está preparado para implementación futura con base de datos.
    """
    # TODO: Implementar cuando se agregue persistencia
    return create_success_response(
        data={"conversation_id": conversation_id, "history": []},
        message="Funcionalidad en desarrollo - historial persistente"
    )


@router.delete("/conversation-history/{conversation_id}")
async def delete_conversation_history(conversation_id: str):
    """
    Endpoint para eliminar el historial de una conversación.
    
    Args:
        conversation_id (str): ID de la conversación a eliminar
        
    Returns:
        dict: Confirmación de eliminación
        
    Note:
        Este endpoint está preparado para implementación futura con base de datos.
    """
    # TODO: Implementar cuando se agregue persistencia
    return create_success_response(
        data={"conversation_id": conversation_id, "deleted": True},
        message="Funcionalidad en desarrollo - eliminación de historial"
    )


@router.get("/health")
async def health_check():
    """
    Endpoint de verificación de salud del servicio de modificación.
    
    Returns:
        dict: Estado del servicio
    """
    return create_success_response(
        data={"service": "modification", "status": "healthy"},
        message="Servicio de modificación funcionando correctamente"
    )

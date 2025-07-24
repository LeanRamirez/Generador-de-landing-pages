"""
Rutas para la generación de landing pages.

Este módulo contiene los endpoints relacionados con la generación inicial
de landing pages usando inteligencia artificial.
"""

from fastapi import APIRouter
from ..schemas.prompt_schema import PromptRequest
from ..services.generate_code import generar_landing, validate_generation_request
from ..utils.error_handlers import handle_generic_error, create_success_response


# Crear router para las rutas de generación
router = APIRouter(
    prefix="/api",
    tags=["generation"],
    responses={
        400: {"description": "Error de validación"},
        500: {"description": "Error interno del servidor"}
    }
)


@router.post("/generate-landing")
async def generar_landing_route(data: PromptRequest):
    """
    Endpoint para generar una landing page basada en un prompt de texto.
    
    Args:
        data (PromptRequest): Objeto que contiene el prompt del usuario
        
    Returns:
        dict: Respuesta con el código HTML generado y estado de éxito
        
    Raises:
        HTTPException: Para errores de validación o generación
    """
    try:
        # Validar la petición usando el validador modular
        validate_generation_request(data.prompt)
        
        # Generar la landing page usando el servicio modular
        html_code = generar_landing(data.prompt)
        
        # Retornar respuesta estandarizada
        return create_success_response(
            data={"html": html_code},
            message="Landing page generada exitosamente"
        )
        
    except Exception as e:
        # Manejar errores usando el handler modular
        if hasattr(e, 'status_code'):
            # Si ya es una HTTPException, re-lanzarla
            raise e
        else:
            # Convertir a HTTPException usando el handler
            raise handle_generic_error(e, "generación de landing page")


@router.get("/generate-examples")
async def get_generation_examples():
    """
    Endpoint para obtener ejemplos de prompts de generación.
    
    Returns:
        dict: Lista de ejemplos de prompts
    """
    try:
        from ..services.generate_code import get_generation_examples
        
        examples = get_generation_examples()
        
        return create_success_response(
            data={"examples": examples},
            message="Ejemplos obtenidos exitosamente"
        )
        
    except Exception as e:
        raise handle_generic_error(e, "obtención de ejemplos")


@router.get("/health")
async def health_check():
    """
    Endpoint de verificación de salud del servicio de generación.
    
    Returns:
        dict: Estado del servicio
    """
    return create_success_response(
        data={"service": "generation", "status": "healthy"},
        message="Servicio de generación funcionando correctamente"
    )

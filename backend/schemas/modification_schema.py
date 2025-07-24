# Importación de BaseModel y Field de Pydantic para validación de datos
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ConversationEntry(BaseModel):
    """
    Modelo que representa una entrada individual en el historial de conversación.
    
    Attributes:
        id (int): Identificador único de la entrada
        type (str): Tipo de entrada ('initial_generation' o 'modification')
        userInput (str): Input del usuario para esta entrada
        timestamp (str): Timestamp ISO de cuando se creó la entrada
        result (Optional[str]): HTML resultante de esta operación
        previousHTML (Optional[str]): HTML previo antes de la modificación (solo para modificaciones)
    """
    id: int = Field(..., description="Identificador único de la entrada")
    type: str = Field(..., description="Tipo de entrada: 'initial_generation' o 'modification'")
    userInput: str = Field(..., description="Input del usuario para esta entrada")
    timestamp: str = Field(..., description="Timestamp ISO de la entrada")
    result: Optional[str] = Field(None, description="HTML resultante de esta operación")
    previousHTML: Optional[str] = Field(None, description="HTML previo antes de la modificación")

class ModificationRequest(BaseModel):
    """
    Modelo de validación para las peticiones de modificación conversacional de landing pages.
    
    Este modelo define la estructura y validación de los datos que debe enviar
    el cliente cuando solicita modificaciones iterativas a una landing page existente.
    
    Attributes:
        currentHTML (str): Código HTML actual de la landing page que se va a modificar
        modificationRequest (str): Instrucción en lenguaje natural del usuario sobre qué modificar
        conversationHistory (List[ConversationEntry]): Historial de la conversación para mantener contexto
    """
    currentHTML: str = Field(
        ..., 
        description="Código HTML actual de la landing page",
        min_length=1
    )
    modificationRequest: str = Field(
        ..., 
        description="Instrucción de modificación en lenguaje natural",
        min_length=1,
        max_length=1000
    )
    conversationHistory: List[ConversationEntry] = Field(
        default=[],
        description="Historial de conversación para mantener contexto",
        max_items=10  # Limitar a máximo 10 entradas para evitar payloads muy grandes
    )

class ModificationResponse(BaseModel):
    """
    Modelo de respuesta para las modificaciones conversacionales.
    
    Attributes:
        html (str): Código HTML modificado
        status (str): Estado de la operación
        changes_applied (List[str]): Lista de cambios aplicados (opcional)
        warnings (List[str]): Lista de advertencias o notas (opcional)
    """
    html: str = Field(..., description="Código HTML modificado")
    status: str = Field(default="success", description="Estado de la operación")
    changes_applied: Optional[List[str]] = Field(
        default=None, 
        description="Lista descriptiva de los cambios aplicados"
    )
    warnings: Optional[List[str]] = Field(
        default=None, 
        description="Lista de advertencias o notas sobre la modificación"
    )

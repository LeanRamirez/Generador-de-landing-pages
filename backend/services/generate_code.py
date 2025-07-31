"""
Servicio para la generación de landing pages usando OpenAI.

Este módulo contiene la lógica para generar código HTML/CSS completo
de landing pages basado en descripciones en lenguaje natural.
"""

from utils.openai_client import create_chat_completion, build_system_message, build_user_message
from utils.error_handlers import handle_openai_error, validate_required_fields


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
        generated_html = create_chat_completion(
            messages=messages,
            model="gpt-3.5-turbo",
            temperature=0.7,
            max_tokens=4000
        )
        
        # Limpiar y asegurar estructura HTML completa
        clean_html = _clean_html_code(generated_html)
        complete_html = _ensure_complete_html_structure(clean_html)
        
        return complete_html
        
    except Exception as e:
        # Manejar errores usando el handler modular y retornar HTML de error
        error_html = _generate_error_html(str(e))
        return error_html


def generate_landing_code(prompt: str) -> str:
    """
    Alias para generar_landing para compatibilidad con el frontend.
    
    Args:
        prompt (str): Descripción de la landing page deseada
        
    Returns:
        str: Código HTML completo de la landing page con estructura completa
    """
    return generar_landing(prompt)


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
    - Accesibilidad básica implementada
    
    IMPORTANTE: SIEMPRE genera código HTML completo con estructura:
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[título]</title>
        <style>[estilos CSS]</style>
    </head>
    <body>
        [contenido HTML]
    </body>
    </html>
    
    Tu respuesta debe comenzar con <!DOCTYPE html> y terminar con </html>."""


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
    
    ESTRUCTURA OBLIGATORIA - Tu respuesta debe comenzar exactamente con:
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[título apropiado]</title>
        <style>
            [todo el CSS aquí]
        </style>
    </head>
    <body>
        [todo el contenido HTML aquí]
    </body>
    </html>
    
    Instrucciones técnicas:
    - SIEMPRE incluí la estructura HTML completa (DOCTYPE, html, head, body)
    - Incluí todo el CSS dentro de etiquetas <style> en el <head>
    - Usá un diseño moderno y responsivo (mobile-first)
    - Incluí colores atractivos y tipografía legible
    - Implementá hover effects y transiciones suaves
    - Asegurate de que sea accesible (alt texts, semantic HTML)
    - Optimizá para velocidad de carga
    - No expliques nada, solo devolvé el código HTML completo
    - El código debe estar listo para usar directamente en un navegador
    - NO uses enlaces externos a CSS, JS o imágenes
    - Tu respuesta debe terminar exactamente con </html>
    
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
        from utils.error_handlers import handle_validation_error
        raise handle_validation_error(
            "prompt", 
            "Debe tener al menos 10 caracteres para generar una landing page útil"
        )
    
    # Validar longitud máxima
    if len(prompt.strip()) > 1000:
        from utils.error_handlers import handle_validation_error
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


def _clean_html_code(html_code: str) -> str:
    """
    Limpia el código HTML de caracteres no deseados y formato incorrecto.
    
    Args:
        html_code (str): Código HTML a limpiar
        
    Returns:
        str: Código HTML limpio
    """
    # Remover posibles bloques de código markdown
    if html_code.startswith('```html'):
        html_code = html_code.replace('```html', '').replace('```', '').strip()
    elif html_code.startswith('```'):
        html_code = html_code.replace('```', '').strip()
    
    # Remover espacios en blanco excesivos al inicio y final
    html_code = html_code.strip()
    
    return html_code


def _ensure_complete_html_structure(html_code: str) -> str:
    """
    Asegura que el código HTML tenga una estructura completa.
    
    Args:
        html_code (str): Código HTML a validar
        
    Returns:
        str: Código HTML con estructura completa garantizada
    """
    import re
    
    # Verificar si ya tiene estructura completa
    has_doctype = html_code.lower().startswith('<!doctype html>')
    has_html_tag = '<html' in html_code.lower()
    has_head_tag = '<head>' in html_code.lower() or '<head ' in html_code.lower()
    has_body_tag = '<body>' in html_code.lower() or '<body ' in html_code.lower()
    
    if has_doctype and has_html_tag and has_head_tag and has_body_tag:
        return html_code
    
    # Si no tiene estructura completa, envolverlo en estructura básica
    if not has_doctype or not has_html_tag:
        # Extraer título si existe
        title = "Landing Page"
        if '<title>' in html_code:
            title_match = re.search(r'<title>(.*?)</title>', html_code, re.IGNORECASE)
            if title_match:
                title = title_match.group(1)
        
        # Extraer estilos si existen
        styles = """
        body {
            margin: 0;
            padding: 20px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        * {
            box-sizing: border-box;
        }
        """
        
        if '<style>' in html_code:
            style_match = re.search(r'<style>(.*?)</style>', html_code, re.DOTALL | re.IGNORECASE)
            if style_match:
                styles = style_match.group(1)
        
        # Limpiar el contenido del body (remover tags de estructura si existen)
        body_content = html_code
        # Remover tags de estructura existentes si los hay
        body_content = re.sub(r'<!DOCTYPE[^>]*>', '', body_content, flags=re.IGNORECASE)
        body_content = re.sub(r'</?html[^>]*>', '', body_content, flags=re.IGNORECASE)
        body_content = re.sub(r'<head>.*?</head>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = re.sub(r'</?body[^>]*>', '', body_content, flags=re.IGNORECASE)
        body_content = re.sub(r'<style>.*?</style>', '', body_content, flags=re.DOTALL | re.IGNORECASE)
        body_content = body_content.strip()
        
        # Construir HTML completo
        complete_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{styles}</style>
</head>
<body>
    {body_content}
</body>
</html>"""
        
        return complete_html
    
    return html_code


def _generate_error_html(error_message: str) -> str:
    """
    Genera HTML de error cuando falla la generación.
    
    Args:
        error_message (str): Mensaje de error
        
    Returns:
        str: HTML completo con mensaje de error
    """
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error - Generador de Landing Pages</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .error-container {{
            max-width: 600px;
            margin: 20px;
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }}
        .error-icon {{
            font-size: 64px;
            color: #dc3545;
            margin-bottom: 20px;
        }}
        h1 {{
            color: #dc3545;
            margin-bottom: 20px;
            font-size: 28px;
        }}
        p {{
            color: #666;
            line-height: 1.6;
            margin-bottom: 15px;
        }}
        .error-details {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #dc3545;
            margin-top: 20px;
            text-align: left;
        }}
        .retry-button {{
            display: inline-block;
            margin-top: 20px;
            padding: 12px 24px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            transition: background 0.3s;
        }}
        .retry-button:hover {{
            background: #0056b3;
        }}
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-icon">⚠️</div>
        <h1>Error al generar la landing page</h1>
        <p>Ocurrió un problema al procesar tu solicitud. Por favor, intenta nuevamente con una descripción diferente o más específica.</p>
        <div class="error-details">
            <strong>Detalles del error:</strong><br>
            {error_message}
        </div>
        <p><strong>Sugerencias:</strong></p>
        <ul style="text-align: left; color: #666;">
            <li>Verifica que tu descripción sea clara y específica</li>
            <li>Intenta con una descripción más corta</li>
            <li>Asegúrate de tener conexión a internet</li>
        </ul>
    </div>
</body>
</html>"""

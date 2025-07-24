"""
Script de demostración que crea una landing page de ejemplo
sin usar la API de OpenAI (para cuando no hay créditos disponibles)
"""

def crear_landing_demo(prompt_usuario: str) -> str:
    """
    Crea una landing page de demostración basada en el prompt del usuario.
    
    Esta función analiza el prompt del usuario para determinar el tema y colores,
    luego genera una landing page HTML completa con CSS embebido.
    Es útil para demostrar la funcionalidad sin consumir créditos de OpenAI.
    
    Args:
        prompt_usuario (str): Descripción de la landing page deseada por el usuario
        
    Returns:
        str: Código HTML completo con CSS embebido de la landing page
    """
    
    # Analizar el prompt para personalizar la demo según palabras clave
    tema = "tecnología"  # Tema por defecto
    color_principal = "#007bff"  # Color azul por defecto
    
    # Detectar tema basado en palabras clave en el prompt
    if "restaurante" in prompt_usuario.lower() or "comida" in prompt_usuario.lower():
        tema = "restaurante"
        color_principal = "#ff6b35"  # Color naranja para restaurantes
    elif "salud" in prompt_usuario.lower() or "médico" in prompt_usuario.lower():
        tema = "salud"
        color_principal = "#28a745"  # Color verde para salud
    elif "educación" in prompt_usuario.lower() or "curso" in prompt_usuario.lower():
        tema = "educación"
        color_principal = "#6f42c1"  # Color púrpura para educación
    elif "azul" in prompt_usuario.lower():
        color_principal = "#007bff"  # Azul específico
    elif "verde" in prompt_usuario.lower():
        color_principal = "#28a745"  # Verde específico
    elif "rojo" in prompt_usuario.lower():
        color_principal = "#dc3545"  # Rojo específico
    
    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page - {tema.title()}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        header {{
            background: {color_principal};
            color: white;
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        nav {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-size: 1.5rem;
            font-weight: bold;
        }}
        
        .nav-links {{
            display: flex;
            list-style: none;
            gap: 2rem;
        }}
        
        .nav-links a {{
            color: white;
            text-decoration: none;
            transition: opacity 0.3s;
        }}
        
        .nav-links a:hover {{
            opacity: 0.8;
        }}
        
        .hero {{
            background: linear-gradient(135deg, {color_principal}, {color_principal}dd);
            color: white;
            padding: 120px 0 80px;
            text-align: center;
        }}
        
        .hero h1 {{
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: fadeInUp 1s ease;
        }}
        
        .hero p {{
            font-size: 1.2rem;
            margin-bottom: 2rem;
            animation: fadeInUp 1s ease 0.2s both;
        }}
        
        .btn {{
            display: inline-block;
            background: white;
            color: {color_principal};
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: transform 0.3s, box-shadow 0.3s;
            animation: fadeInUp 1s ease 0.4s both;
        }}
        
        .btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        
        .features {{
            padding: 80px 0;
            background: #f8f9fa;
        }}
        
        .features-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }}
        
        .feature-card {{
            background: white;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }}
        
        .feature-card:hover {{
            transform: translateY(-5px);
        }}
        
        .feature-icon {{
            width: 60px;
            height: 60px;
            background: {color_principal};
            border-radius: 50%;
            margin: 0 auto 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: white;
        }}
        
        .cta {{
            background: {color_principal};
            color: white;
            padding: 80px 0;
            text-align: center;
        }}
        
        .cta h2 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }}
        
        .cta p {{
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }}
        
        .btn-secondary {{
            background: white;
            color: {color_principal};
            padding: 15px 40px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: all 0.3s;
        }}
        
        .btn-secondary:hover {{
            background: #f8f9fa;
            transform: translateY(-2px);
        }}
        
        footer {{
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem 0;
        }}
        
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 2rem;
            }}
            
            .nav-links {{
                display: none;
            }}
            
            .features-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <nav class="container">
            <div class="logo">Mi Empresa</div>
            <ul class="nav-links">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#servicios">Servicios</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <section class="hero" id="inicio">
        <div class="container">
            <h1>Soluciones Innovadoras de {tema.title()}</h1>
            <p>Transformamos tus ideas en realidad con tecnología de vanguardia y un equipo experto</p>
            <a href="#contacto" class="btn">Comenzar Ahora</a>
        </div>
    </section>

    <section class="features" id="servicios">
        <div class="container">
            <h2 style="text-align: center; font-size: 2.5rem; margin-bottom: 1rem;">Nuestros Servicios</h2>
            <p style="text-align: center; font-size: 1.1rem; color: #666;">Ofrecemos soluciones completas para tu negocio</p>
            
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">🚀</div>
                    <h3>Desarrollo Rápido</h3>
                    <p>Implementamos soluciones eficientes con las últimas tecnologías del mercado.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">💡</div>
                    <h3>Ideas Innovadoras</h3>
                    <p>Creamos estrategias únicas que destacan tu marca en el mercado competitivo.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3>Resultados Garantizados</h3>
                    <p>Nos comprometemos a entregar resultados que superen tus expectativas.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="cta" id="contacto">
        <div class="container">
            <h2>¿Listo para Comenzar?</h2>
            <p>Contáctanos hoy y descubre cómo podemos ayudarte a alcanzar tus objetivos</p>
            <a href="mailto:contacto@miempresa.com" class="btn-secondary">Contactar Ahora</a>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Mi Empresa. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>"""
    
    # Retornar el HTML completo generado con las personalizaciones aplicadas
    return html_template

# Punto de entrada del script cuando se ejecuta directamente
if __name__ == "__main__":
    # Crear una landing page de demo con un prompt de ejemplo
    prompt = "Crea una landing page para una empresa de tecnología con colores azules"
    html = crear_landing_demo(prompt)  # Generar el HTML usando la función de demo
    
    # Guardar el archivo HTML generado en el sistema de archivos
    with open("demo_landing_page.html", "w", encoding="utf-8") as f:
        f.write(html)  # Escribir el contenido HTML al archivo
    
    # Mostrar mensajes de confirmación al usuario
    print("✅ Landing page de demostración creada: demo_landing_page.html")
    print("🌐 Abre el archivo en tu navegador para verla")

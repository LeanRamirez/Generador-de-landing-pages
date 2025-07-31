#!/usr/bin/env python3
"""
Script de prueba para verificar que el backend funciona correctamente
"""

import sys
import os

# Agregar el directorio backend al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

try:
    from services.generate_code import generate_landing_code
    
    print("✅ Importación exitosa de generate_landing_code")
    
    # Probar la función
    test_prompt = "Una landing page simple para una empresa de tecnología"
    result = generate_landing_code(test_prompt)
    
    print(f"✅ Función ejecutada exitosamente")
    print(f"📄 HTML generado (primeros 200 caracteres):")
    print(result[:200] + "..." if len(result) > 200 else result)
    
    # Verificar que el HTML tiene la estructura correcta
    if "<!DOCTYPE html>" in result and "<html" in result and "<body" in result:
        print("✅ HTML tiene estructura completa")
    else:
        print("❌ HTML no tiene estructura completa")
        
except ImportError as e:
    print(f"❌ Error de importación: {e}")
except Exception as e:
    print(f"❌ Error al ejecutar la función: {e}")

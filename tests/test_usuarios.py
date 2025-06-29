from src.Usuario import Usuario

def test_actualizar_peso_baja():
    """Prueba que el peso se actualiza correctamente cuando baja"""
    # Configuración
    usuario = Usuario("Usuario1", 100.0)
    nuevo_peso = 90.5  # Peso menor al inicial
    
    # Acción
    usuario.actualizar_peso(nuevo_peso)
    
    # Verificación
    assert usuario.peso == nuevo_peso, f"El peso debería ser {nuevo_peso} kg, pero es {usuario.peso} kg"

def test_actualizar_peso_sube():
    """Prueba que el peso se actualiza correctamente cuando sube"""
    # Configuración
    usuario = Usuario("Usuario2", 100.0)
    nuevo_peso = 105.5  # Peso mayor al inicial
    
    # Acción
    usuario.actualizar_peso(nuevo_peso)
    
    # Verificación
    assert usuario.peso == nuevo_peso, f"El peso debería ser {nuevo_peso} kg, pero es {usuario.peso} kg"
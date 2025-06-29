import pytest
from src.Usuario import Usuario

def test_creacion_usuario():
    """Prueba la creación básica de un usuario"""
    usuario = Usuario("Usuario1", 50.5)
    
    assert usuario.nombre == "Usuario1"
    assert usuario.peso == 50.5

def test_actualizacion_peso():
    """Prueba la actualización correcta del peso"""
    usuario = Usuario("Usuario2", 100.5)
    usuario.actualizar_peso(50.5)
    
    assert usuario.peso == 50.5

def test_mostrar_informacion(capsys):
    """Prueba el método mostrar_informacion"""
    usuario = Usuario("Usuario3", 77.7)
    usuario.mostrar_informacion()
    
    captured = capsys.readouterr()
    assert "Usuario: Usuario3, Peso Actual: 77.7 kg" in captured.out

import pytest
from src.api import app as flask_app
from src.Usuario import Usuario

@pytest.fixture
def app():
    flask_app.config['TESTING'] = True
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def limpiar_usuarios():
    from src.api import usuarios
    usuarios.clear()
    yield
    usuarios.clear()

def test_creacion_usuario():
    usuario = Usuario("Test", 70.5)
    assert usuario.nombre == "Test"
    assert usuario.peso == 70.5
    
    usuario.actualizar_peso(71.0)   
    assert usuario.peso == 71.0

def test_formulario_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Sistema: Ingreso de Peso' in response.data  # título en HTML

def test_agregar_usuario(client):
    response = client.post('/', data={
        'nombre': 'TestUser',
        'peso': '75.5'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'TestUser' in response.data
    assert b'75.5' in response.data

def test_obtener_usuarios_html(client):
    # Agregar usuario
    client.post('/', data={'nombre': 'ApiUser', 'peso': '80.0'}, follow_redirects=True)
    
    # Obtener HTML con lista de usuarios
    response = client.get('/')
    assert response.status_code == 200
    assert b'ApiUser' in response.data
    assert b'80.0' in response.data

def test_buscar_usuario_en_html(client):
    # Agrega usuarios
    client.post('/', data={'nombre': 'Usuario1', 'peso': '70.0'}, follow_redirects=True)
    client.post('/', data={'nombre': 'Usuario2', 'peso': '80.0'}, follow_redirects=True)
    
    # Solo verifica que están en el HTML (no hay API para buscar por nombre)
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode()
    assert 'Usuario1' in html
    assert 'Usuario2' in html
    
    # Para un usuario no agregado, asegúrate que no aparece
    assert 'NoExiste' not in html

def test_usuario_no_encontrado_case_sensitive_html(client):
    client.post('/', data={'nombre': 'CaseUser', 'peso': '90.0'}, follow_redirects=True)
    
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode()
    # El nombre se muestra tal cual, la búsqueda exacta no está implementada
    assert 'CaseUser' in html
    assert 'caseuser' not in html  # porque no está agregado exactamente en minúsculas

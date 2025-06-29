import pytest
from src.api import app as flask_app
from src.Usuario import Usuario
import json

@pytest.fixture
def app():
    # Configuración realizar las pruebas
    flask_app.config['TESTING'] = True
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def limpiar_usuarios():
    # Fixture para borrado de los usuarios antes de cada prueba
    from src.api import usuarios
    usuarios.clear()
    yield
    usuarios.clear()

def test_creacion_usuario():
    """Test para la clase Usuario"""
    usuario = Usuario("Test", 70.5)
    assert usuario.nombre == "Test"
    assert usuario.peso == 70.5
    
    usuario.actualizar_peso(71.0)   
    assert usuario.peso == 71.0

def test_formulario_get(client):
    """Test para la ruta principal (GET)"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Sistema: Ingreso de Peso' in response.data  # Título de la página

def test_agregar_usuario(client):
    """Test para agregar usuario mediante POST"""
    response = client.post('/', data={
        'nombre': 'TestUser',
        'peso': '75.5'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'TestUser' in response.data
    assert b'75.5' in response.data

def test_obtener_usuarios_api(client):
    """Test para la API de usuarios"""
    # Primero agregamos un usuario
    client.post('/', data={'nombre': 'ApiUser', 'peso': '80.0'})
    
    response = client.get('/api/usuarios')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['nombre'] == 'ApiUser'
    assert data[0]['peso'] == 80.0

def test_obtener_usuario_por_nombre(client):
    """Test para obtener usuario por nombre"""
    # Agregamos varios usuarios
    client.post('/', data={'nombre': 'Usuario1', 'peso': '70.0'})
    client.post('/', data={'nombre': 'Usuario2', 'peso': '80.0'})
    
    # Probamos obtener un usuario existente
    response = client.get('/api/usuarios/Usuario1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['nombre'] == 'Usuario1'
    assert data['peso'] == 70.0
    
    # Probamos obtener un usuario que no existe
    response = client.get('/api/usuarios/NoExiste')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error'] == 'Usuario no encontrado'

def test_usuario_no_encontrado_case_sensitive(client):
    """Test que verifica que la búsqueda no es case sensitive"""
    client.post('/', data={'nombre': 'CaseUser', 'peso': '90.0'})
    
    response = client.get('/api/usuarios/caseuser')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['nombre'] == 'CaseUser'
from flask import Flask, render_template, request, redirect, url_for
from Usuario import Usuario  # ← Importación agregada

app = Flask(__name__)

usuarios = []

@app.route('/', methods=['GET', 'POST'])
def formulario_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        peso = float(request.form['peso'])

        usuario = Usuario(nombre, peso)
        usuario.actualizar_peso(peso)  # ← Aplica la lógica de restar 1 kg

        usuarios.append(usuario)

        return redirect(url_for('formulario_usuario'))

    # Convierte los objetos Usuario a diccionarios para pasarlos al HTML
    usuarios_info = [{'nombre': u.nombre, 'peso': u.peso} for u in usuarios]

    return render_template('formulario.html', usuarios=usuarios_info)

"""
import json

@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return json.dumps(usuarios), 200, {'Content-Type': 'application/json'}

@app.route('/api/usuarios/<string:nombre>', methods=['GET'])
def obtener_usuario_por_nombre(nombre):
    usuario = next((u for u in usuarios if u['nombre'].lower() == nombre.lower()), None)
    if usuario:
        return json.dumps(usuario), 200, {'Content-Type': 'application/json'}
    return json.dumps({"error": "Usuario no encontrado"}), 404"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #Orginal
    # app.run(debug=True)
    
    #app.run(debug=True, host='0.0.0.0', port=5000)
    #para probar api ejecutar: python -m app.api

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

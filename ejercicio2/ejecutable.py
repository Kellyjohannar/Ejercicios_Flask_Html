#2) Login básico (sin BD): formulario POST, validación contra un diccionario en memoria y página protegida.
# Se importa la clase Flask (para crear la app), render_template (para mostrar HTML) y request (para leer datos del usuario).
from flask import Flask, render_template, request

# Se crea la instancia de la aplicación Flask.
# template_folder='plantilla': Se le dice explícitamente que busque los archivos HTML en la carpeta 'plantilla', el
# static_folder es para poder implementar el CSS.
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla', static_url_path='')

# --- BASE DE DATOS SIMULADA ---
# Se crea un diccionario en memoria para guardar usuarios y contraseñas.
# Dato (izquierdo) = Usuario, Dato(derecho) = Contraseña.
usuarios_registrados = {
    "Mary": "admin123",
    "Alex": "clave456",
    "Kelly": "1234"
}

# --- RUTA 1: PÁGINA DE INICIO ---
# Se define la ruta raíz '/'. Cuando se netra a la web, esto es lo primero que se ejecuta.
@app.route('/')
def inicio():
    # Se busca el archivo 'validacion.html' dentro de la carpeta 'plantilla' y se le envia al navegador.
    return render_template('validacion.html')

# --- RUTA 2: PROCESAR EL LOGIN ---
# Se define la ruta '/login'. ES IMPORTANTE: methods=['POST'] permite recibir datos ocultos del formulario.
@app.route('/login', methods=['POST'])
def login():
    #request.form.get('...'): Se extrae lo que el usuario escribió en el input llamado 'nombre_usuario'.
    usuario_recibido = request.form.get('nombre_usuario')
    #Se extrae lo que el usuario escribió en el input llamado 'password_usuario'.
    password_recibido = request.form.get('password_usuario')

    # --- VALIDACIÓN ---
    # Se valida si el usuario existe Y tambien se valida si la contraseña coincide con la guardada
    if usuario_recibido in usuarios_registrados and usuarios_registrados[usuario_recibido] == password_recibido:
        # Si todo es correcto, se muestra la página protegida.
        # user=usuario_recibido: Se envia el nombre del usuario al HTML para poder saludarlo.
        return render_template('pagina_protegida.html', user=usuario_recibido)
    else:
        # Si falla, se devuelve un mensaje de error simple con un enlace para volver.
        return render_template('error.html')

# --- ARRANCAR SERVIDOR ---
# Se verifica si el archivo se está ejecutando directamente.
if __name__ == '__main__':
    # Se arranca la aplicación en modo debug para ver errores en tiempo real.
    app.run(debug=True)
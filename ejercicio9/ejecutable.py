# Se importan las herramientas necesarias de Flask.
# Se incluye 'flash' para la gestión de mensajes temporales de respuesta.
from flask import Flask, render_template, request, redirect, url_for, flash

# --- CONFIGURACIÓN DE LA APP ---
# Se inicializa la aplicación Flask vinculada a la carpeta 'plantilla'.
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# --- CONFIGURACIÓN DE SEGURIDAD ---
# Se define una clave secreta (secret_key), requisito indispensable para el uso de 'flash' y sesiones.
# Esta cadena de texto se utiliza para cifrar la información enviada al navegador.
app.secret_key = 'mi_clave_super_secreta_y_morada'

# --- RUTA 1: VISUALIZACIÓN DEL FORMULARIO (GET) ---
@app.route("/")
def index():
    # Se renderiza el archivo HTML. Los mensajes almacenados en la sesión se envían automáticamente al template.
    return render_template("formulario.html")

# --- RUTA DE PROCESAMIENTO Y VALIDACIÓN (POST) ---
# Se activa esta ruta tras el envío del formulario.
@app.route("/validar", methods=["POST"])
def validar_datos():
    # 1. Se capturan los datos enviados por el usuario desde el objeto 'request.form'.
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    correo = request.form.get("correo")

    # Se inicia el proceso de validación mediante una bandera de control.
    hay_error = False

    # --- VALIDACIÓN NOMBRE ---
    # Se comprueba si el campo está vacío.
    if not nombre:
        # Se genera un mensaje de alerta bajo la categoría 'error'.
        flash("¡El nombre es obligatorio!", "error")
        hay_error = True

    # --- VALIDACIÓN EDAD ---
    # Se verifica la presencia del dato y que este se componga únicamente de dígitos.
    if not edad or not edad.isdigit():
        flash("Debes ingresar una edad válida (solo números).", "error")
        hay_error = True
    else:
        # Si el dato es numérico, se valida que sea igual o superior a 18.
        if int(edad) < 18:
            flash("Lo siento, debes ser mayor de 18 años.", "error")
            hay_error = True

    # --- VALIDACIÓN CORREO ---
    # Se realiza una comprobación básica de formato buscando el carácter '@'.
    if not correo or "@" not in correo:
        flash("El correo electrónico no parece válido.", "error")
        hay_error = True

    # Se determina el flujo de redirección según el estado de la validación.
    if hay_error:
        # Ante la presencia de errores, se redirige a la página inicial para mostrar los avisos.
        return redirect(url_for("index"))
    else:
        # Si los datos son correctos, se registra un mensaje de éxito con la categoría 'exito'.
        flash(f"¡Todo correcto! Usuario {nombre} registrado.", "exito")
        # Se recarga la página principal tras procesar el registro con éxito.
        return redirect(url_for("index"))

# --- ARRANQUE DEL SERVIDOR ---
if __name__ == "__main__":
    # Se inicia la ejecución del servidor web con el modo de depuración activado.
    app.run(debug=True)
# Se importan las dependencias de Flask para la gestión de rutas, plantillas, datos de solicitud y sesiones de usuario.
from flask import Flask, render_template, request, redirect, url_for, session

# --- CONFIGURACIÓN DE LA APP ---
# Se establece la configuración de Flask para localizar recursos en la carpeta 'plantilla'.
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# --- CONFIGURACIÓN DE SEGURIDAD (SESIONES) ---
# Se define la clave secreta requerida para el cifrado de las cookies de sesión.
# Este parámetro es obligatorio para el funcionamiento del sistema de inicio de sesión (login).
app.secret_key = 'clave_secreta_para_el_proyecto'

# --- ESTRUCTURAS DE DATOS TEMPORALES (MEMORIA) ---
# Se inicializa la lista de autores disponibles en el sistema.
lista_autores = ["Alexandra Neymar", "Gabriel Garcia Marquez", "Mario Mendoza"]

# Se inicializa el registro de libros mediante una lista de diccionarios.
lista_libros = [
    {"titulo": "Mirame y Dispara", "autor": "Alexandra Neymar"},
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel Garcia Marquez"}
]


# --- RUTA ACCESO AL SISTEMA (LOGIN) ---
# Se gestiona tanto la carga del formulario (GET) como la validación de credenciales (POST).
@app.route("/", methods=["GET", "POST"])
def login():
    # Se verifica si el método de la solicitud es POST (envío de formulario).
    if request.method == "POST":
        # Se capturan el identificador de usuario y la contraseña desde el formulario.
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")

        # Se procede a la validación de los datos frente a las credenciales predefinidas.
        if usuario == "admin" and contrasena == "1234":
            # Ante una validación exitosa, se registra el identificador en el objeto session.
            session["usuario_logueado"] = usuario
            # Se redirige al usuario hacia el panel de control principal.
            return redirect(url_for("dashboard"))
        else:
            # En caso de error en los datos, se vuelve a renderizar el login con un mensaje informativo.
            return render_template("login.html", error="Datos incorrectos")

    # Ante una petición inicial (GET), se muestra la interfaz de inicio de sesión.
    return render_template("login.html")


# --- RUTA FINALIZACIÓN DE SESIÓN (LOGOUT) ---
@app.route("/logout")
def logout():
    # Se elimina la clave del usuario de la sesión activa para cerrar el acceso.
    session.pop("usuario_logueado", None)
    # Se ejecuta la redirección automática hacia la pantalla de login.
    return redirect(url_for("login"))


# --- RUTA PANEL DE CONTROL (DASHBOARD) ---
@app.route("/panel")
def dashboard():
    # PROTOCOLO DE SEGURIDAD: Se comprueba la existencia de una sesión activa.
    if "usuario_logueado" not in session:
        # Ante la ausencia de sesión, se fuerza el retorno al área de login.
        return redirect(url_for("login"))

    # Se renderiza la interfaz principal enviando el nombre del usuario logueado.
    return render_template("dashboard.html", usuario=session["usuario_logueado"])


# --- RUTA GESTIÓN DE AUTORES ---
@app.route("/autores", methods=["GET", "POST"])
def autores():
    # PROTOCOLO DE SEGURIDAD: Se verifica la autenticación antes de permitir el acceso.
    if "usuario_logueado" not in session:
        return redirect(url_for("login"))

    # Se procesa la incorporación de nuevos datos si la petición es de tipo POST.
    if request.method == "POST":
        nuevo_autor = request.form.get("nombre_autor")
        # Se añade el nuevo registro a la lista si el campo contiene información válida.
        if nuevo_autor:
            lista_autores.append(nuevo_autor)

    # Se muestra la interfaz de autores con la colección de datos actualizada.
    return render_template("autores.html", autores=lista_autores)


# --- RUTA GESTIÓN DE LIBROS ---
@app.route("/libros", methods=["GET", "POST"])
def libros():
    # PROTOCOLO DE SEGURIDAD: Se restringe el acceso a usuarios no identificados.
    if "usuario_logueado" not in session:
        return redirect(url_for("login"))

    # Se gestiona la creación de nuevos registros de libros mediante POST.
    if request.method == "POST":
        titulo = request.form.get("titulo_libro")
        autor_seleccionado = request.form.get("autor_libro")

        # Se valida la presencia de ambos campos antes de actualizar la lista en memoria.
        if titulo and autor_seleccionado:
            lista_libros.append({"titulo": titulo, "autor": autor_seleccionado})

    # Se renderiza la interfaz de libros suministrando ambas listas para la gestión de datos.
    return render_template("libros.html", libros=lista_libros, autores=lista_autores)


# --- EJECUCIÓN DEL SERVIDOR ---
if __name__ == "__main__":
    # Se inicia la aplicación con el modo de depuración habilitado.
    app.run(debug=True)
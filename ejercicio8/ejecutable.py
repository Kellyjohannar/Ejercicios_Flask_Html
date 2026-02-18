# Se importan Flask para la gestión del servidor y render_template para el procesamiento de archivos HTML.
from flask import Flask, render_template

# --- CONFIGURACIÓN DE LA APP ---
# Se inicializa la aplicación Flask especificando la ubicación de recursos.
# Se define 'plantilla' como la carpeta contenedora para archivos HTML (templates) y estáticos (CSS/JS).
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# ---  INICIO (HOME) ---
# Se establece el punto de acceso para la raíz del sitio web ("/").
@app.route("/")
def pagina_inicio():
    # Se renderiza y devuelve el archivo 'home.html'.
    return render_template("home.html")

# ---  SOBRE NOSOTROS (ABOUT) ---
# Se define la ruta para la sección informativa "/about".
@app.route("/about")
def pagina_about():
    # Se procesa la plantilla 'about.html' para su visualización.
    return render_template("about.html")

# --- CONTACTO ---
# Se habilita el acceso a la sección de contacto mediante la URL "/contacto".
@app.route("/contacto")
def pagina_contacto():
    # Se genera la respuesta basada en el archivo 'contacto.html'.
    return render_template("contacto.html")

# --- ARRANQUE DEL SERVIDOR ---
if __name__ == "__main__":
    # Se inicia la ejecución de la aplicación en modo de depuración (debug).
    # Este modo permite visualizar errores y recargar el servidor tras cambios en el código.
    app.run(debug=True)
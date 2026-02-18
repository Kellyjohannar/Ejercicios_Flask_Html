# --- LIBRERÍAS ---
# Se importan las herramientas de Flask. 'request' es vital para recibir archivos.
from flask import Flask, render_template, request, redirect, url_for
# Se importa 'os', librería que permite gestionar rutas de carpetas en el sistema.
import os

# --- CONFIGURACIÓN DE LA APP ---
# Se inicializa la aplicación Flask.
# Se configura para buscar los HTML y CSS dentro de la carpeta 'plantilla'.
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# --- CONFIGURACIÓN DE LA CARPETA DE SUBIDAS ---
# Se define la ruta donde se guardarán físicamente los archivos subidos.
# Se ubica dentro de 'plantilla' para facilitar el acceso posterior.
CARPETA_SUBIDAS = 'plantilla/archivos_subidos'

# Se verifica si la carpeta de destino existe en el sistema.
# Si no existe, se crea automáticamente mediante el módulo os.
if not os.path.exists(CARPETA_SUBIDAS):
    os.makedirs(CARPETA_SUBIDAS)


# --- RUTA PRINCIPAL (VISUALIZACIÓN) ---
@app.route("/")
def index():
    # Se utiliza os.listdir() para leer el contenido de la carpeta de subidas.
    # Se genera una lista con los nombres de todos los archivos almacenados.
    lista_archivos = os.listdir(CARPETA_SUBIDAS)

    # Se renderiza el HTML y se envía la lista de archivos para su visualización.
    return render_template("subida.html", archivos=lista_archivos)


# --- RUTA PARA PROCESAR LA SUBIDA ---
# Se activa esta ruta al enviar el formulario. Solo se admite el método POST.
@app.route("/subir", methods=["POST"])
def subir_archivo():
    # 1. Se comprueba si el envío contiene el campo 'archivo_usuario'.
    # Nota: Para archivos se emplea 'request.files' en lugar de 'request.form'.
    if 'archivo_usuario' in request.files:

        # 2. Se captura el objeto del archivo enviado por el usuario.
        fichero = request.files['archivo_usuario']

        # 3. Se valida que el nombre del archivo no esté vacío.
        if fichero.filename != '':
            # 4. Se construye la ruta final uniendo la carpeta con el nombre del archivo.
            # Se utiliza 'os.path.join' para asegurar la compatibilidad entre sistemas.
            ruta_guardado = os.path.join(CARPETA_SUBIDAS, fichero.filename)

            # 5. Se procede al guardado físico del archivo en el servidor.
            fichero.save(ruta_guardado)

    # 6. Se redirecciona a la página principal para refrescar la lista.
    return redirect(url_for("index"))


# --- ARRANQUE DEL SERVIDOR ---
if __name__ == "__main__":
    # Se inicia la ejecución del servidor en modo depuración (debug).
    app.run(debug=True)
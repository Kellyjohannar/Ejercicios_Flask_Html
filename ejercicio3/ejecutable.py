# Se importa Flask para crear la aplicación web,
# render_template para mostrar archivos HTML,
# y request para leer los datos que el usuario envía.
from flask import Flask, render_template, request

# Se crea la aplicación Flask.
# template_folder='plantilla': busca los HTML en la carpeta 'plantilla'.
# static_folder='plantilla': busca el CSS dentro de la carpeta 'plantilla'.
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# --- LISTA GLOBAL DE TAREAS ---
# Esta lista vive en la memoria del servidor mientras la app esté corriendo.
# LIMITACIÓN: si reinicias el servidor, las tareas se borran porque no hay base de datos.
tareas = []

# --- RUTA PRINCIPAL ---
# Cuando el usuario entra a '/', se ejecuta esta función.
# methods=["GET", "POST"]: acepta GET (ver página) y POST (enviar datos).
@app.route("/", methods=["GET", "POST"])
def index():

    # Se verifica si el usuario envió un formulario (POST).
    if request.method == "POST":

        # Se verifica si el usuario hizo clic en el botón de agregar.
        if request.form.get("accion") == "agregar":

            # Se lee el texto que el usuario escribió en el campo "tarea".
            tarea_nueva = request.form.get("tarea")

            # Se verifica que el campo no esté vacío.
            # .strip() elimina los espacios en blanco al inicio y al final.
            if tarea_nueva and tarea_nueva.strip():

                # Se agrega la tarea nueva a la lista global.
                tareas.append(tarea_nueva.strip())

        # Se verifica si el usuario hizo clic en el botón de eliminar.
        elif request.form.get("accion") == "eliminar":

            # Se lee la posición de la tarea que se quiere eliminar.
            # int() convierte el texto a número entero.
            indice = int(request.form.get("indice"))

            # Se verifica que la posición sea válida dentro de la lista.
            if 0 <= indice < len(tareas):

                # Se elimina la tarea en esa posición.
                tareas.pop(indice)

    # Se muestra el HTML y se le envía la lista de tareas actualizada.
    return render_template("lista_de_tareas.html", tareas=tareas)

# --- ARRANCAR SERVIDOR ---
# Se verifica si este archivo se está ejecutando directamente.
if __name__ == "__main__":

    # Se arranca el servidor en modo debug para ver errores en tiempo real.
    app.run(debug=True)
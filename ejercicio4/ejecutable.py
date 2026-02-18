from flask import Flask, render_template, request, redirect, url_for
import json
import os

# template_folder='plantilla': Busca el HTML dentro de la carpeta 'plantilla'
# static_folder='plantilla': Busca el CSS también dentro de la carpeta 'plantilla'
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

ARCHIVO_TAREAS = "tareas.json"


# --- FUNCIÓN: CARGAR TAREAS ---
def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                return []
    return []


# --- FUNCIÓN: GUARDAR TAREAS ---
def guardar_tareas(lista_tareas):
    with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as archivo:
        json.dump(lista_tareas, archivo, indent=2, ensure_ascii=False)


# --- RUTA PRINCIPAL ---
@app.route("/", methods=["GET"])
def index():
    mis_tareas = cargar_tareas()

    # AQUI ESTÁ EL CAMBIO CLAVE:
    # Se usa "tareas.html" porque ese es el nombre de tu archivo real.
    return render_template("tareas.html", tareas=mis_tareas)


# --- RUTA AGREGAR ---
@app.route("/agregar", methods=["POST"])
def agregar():
    tarea_nueva = request.form.get("tarea_nueva")

    if tarea_nueva:
        tareas_actuales = cargar_tareas()
        tareas_actuales.append(tarea_nueva)
        guardar_tareas(tareas_actuales)

    # Se redirecciona a 'index', que volverá a cargar tareas.html
    return redirect(url_for("index"))


# --- RUTA ELIMINAR ---
@app.route("/eliminar", methods=["POST"])
def eliminar():
    try:
        indice = int(request.form.get("indice_tarea"))
        tareas_actuales = cargar_tareas()

        if 0 <= indice < len(tareas_actuales):
            tareas_actuales.pop(indice)
            guardar_tareas(tareas_actuales)

    except (ValueError, TypeError):
        pass

    return redirect(url_for("index"))


# --- ¡ESTO ME AYUDA SOLUCIONA EL "EXIT CODE 0"! ---
# Este bloque mantiene el programa encendido.
if __name__ == "__main__":
    app.run(debug=True)
# Se importa el Flask y las herramientas para la web.
from flask import Flask, render_template, request, redirect, url_for
# Se importa json para guardar los contactos en el archivo.
import json
# Se importa para comprobar si el archivo existe.
import os

# Aquí se le dice al Flask: "Busca el HTML en 'plantilla' y los archivos estáticos (CSS) TAMBIÉN en 'plantilla'".
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# Nombre del archivo donde guardaremos los contactos.
ARCHIVO_DB = "contactos.json"

# ESTA ES LA FUNCIÓN DE LEER CONTACTOS ---
def cargar_contactos():
    # Se comprueba si el archivo existe.
    if os.path.exists(ARCHIVO_DB):
        # Se abre en modo lectura.
        with open(ARCHIVO_DB, 'r', encoding='utf-8') as archivo:
            # Se intenta leer el contenido.
            try:
                # Se convierte el JSON a una lista de Python.
                return json.load(archivo)
            # Si hay error (archivo vacío), se devuelve una lista vacía.
            except json.JSONDecodeError:
                return []
    # Si no existe, se devuelve una lista vacía.
    return []

# --- FUNCIÓN DE GUARDAR CONTACTOS ---
def guardar_contactos(lista):
    # Se abre el archivo en modo escritura.
    with open(ARCHIVO_DB, 'w', encoding='utf-8') as archivo:
        # Se guarda la lista en el archivo.
        json.dump(lista, archivo, indent=4, ensure_ascii=False)

# --- RUTA PRINCIPAL PARA VER AGENDA ---
@app.route("/")
def index():
    # Se cargan los contactos.
    agenda = cargar_contactos()
    # Se muestra tu archivo HTML.
    return render_template("agenda.html", contactos=agenda)

# --- RUTA AGREGAR PARA GUARDAR DATOS ---
@app.route("/agregar", methods=["POST"])
def agregar():
    # Se recibe el nombre del formulario.
    nombre = request.form.get("nombre")
    # Se recibe el teléfono del formulario.
    telefono = request.form.get("telefono")

    # Si ambos campos tienen texto...
    if nombre and telefono:
        # Se carga la lista actual.
        contactos = cargar_contactos()
        # Se crea el nuevo contacto (Diccionario).
        nuevo = {"nombre": nombre, "telefono": telefono}
        # Se añade a la lista.
        contactos.append(nuevo)
        # Se guarda en el archivo.
        guardar_contactos(contactos)

    # Se recarga la página principal.
    return redirect(url_for("index"))

# --- RUTA ELIMINAR ---
@app.route("/eliminar", methods=["POST"])
def eliminar():
    # Se recibe la posición a borrar.
    indice = int(request.form.get("indice"))
    # Se carga la lista.
    contactos = cargar_contactos()

    # Si el índice es válido...
    if 0 <= indice < len(contactos):
        # Se borra  el contacto.
        contactos.pop(indice)
        # Se guardan los cambios.
        guardar_contactos(contactos)

    # Se recarga  la página.
    return redirect(url_for("index"))

# --- ARRANQUE DEL SERVIDOR ---
if __name__ == "__main__":
    # Se enciende la web.
    app.run(debug=True)
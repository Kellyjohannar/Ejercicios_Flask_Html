from flask import Flask, render_template, request, redirect, url_for
import json
import os

aplicacionTareas = Flask(__name__, template_folder='plantilla', static_folder='plantilla')
nombreArchivo = "datos.json"

def obtenerTareas():
    listaTareas = []
    if os.path.exists(nombreArchivo):
        archivo = open(nombreArchivo, 'r', encoding='utf-8')
        try:
            listaTareas = json.load(archivo)
        except json.JSONDecodeError:
            listaTareas = []
        archivo.close()
    return listaTareas

def guardarTareas(tareasNuevas):
    archivo = open(nombreArchivo, 'w', encoding='utf-8')
    json.dump(tareasNuevas, archivo, indent=4, ensure_ascii=False)
    archivo.close()

@aplicacionTareas.route("/", methods=["GET"])
def inicio():
    tareasExistentes = obtenerTareas()
    return render_template("listado.html", tareas=tareasExistentes)

@aplicacionTareas.route("/registrarTarea", methods=["POST"])
def registrarTarea():
    textoTarea = request.form.get("textoTarea")
    if textoTarea:
        tareasActuales = obtenerTareas()
        tareasActuales.append(textoTarea)
        guardarTareas(tareasActuales)
    return redirect(url_for("inicio"))

@aplicacionTareas.route("/quitarTarea", methods=["POST"])
def quitarTarea():
    posicion = request.form.get("posicion")
    if posicion is not None:
        indice = int(posicion)
        tareasActuales = obtenerTareas()
        if 0 <= indice < len(tareasActuales):
            tareasActuales.pop(indice)
            guardarTareas(tareasActuales)
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    aplicacionTareas.run(debug=True)
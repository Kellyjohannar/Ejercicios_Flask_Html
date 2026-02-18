from flask import Flask, render_template, request, redirect, url_for
import json
import os

aplicacionAgenda = Flask(__name__, template_folder='plantilla', static_folder='plantilla')
rutaArchivoJson = "contactos.json"


def leerBaseDatos():
    datosObtenidos = []
    if os.path.exists(rutaArchivoJson):
        archivoLectura = open(rutaArchivoJson, 'r', encoding='utf-8')
        try:
            datosObtenidos = json.load(archivoLectura)
        except json.JSONDecodeError:
            datosObtenidos = []
        archivoLectura.close()
    return datosObtenidos


def escribirBaseDatos(datosNuevos):
    archivoEscritura = open(rutaArchivoJson, 'w', encoding='utf-8')
    json.dump(datosNuevos, archivoEscritura, indent=4, ensure_ascii=False)
    archivoEscritura.close()


@aplicacionAgenda.route("/", methods=["GET"])
def mostrarInicio():
    listaContactos = leerBaseDatos()
    return render_template("agenda.html", contactos=listaContactos)


@aplicacionAgenda.route("/guardarContacto", methods=["POST"])
def guardarContacto():
    nombreRecibido = request.form.get("nombreContacto")
    telefonoRecibido = request.form.get("telefonoContacto")

    if nombreRecibido and telefonoRecibido:
        contactosActuales = leerBaseDatos()
        nuevoRegistro = {
            "nombre": nombreRecibido,
            "telefono": telefonoRecibido
        }
        contactosActuales.append(nuevoRegistro)
        escribirBaseDatos(contactosActuales)

    return redirect(url_for("mostrarInicio"))


@aplicacionAgenda.route("/borrarContacto", methods=["POST"])
def borrarContacto():
    indiceRecibido = request.form.get("indice")
    if indiceRecibido is not None:
        posicion = int(indiceRecibido)
        contactosActuales = leerBaseDatos()
        if 0 <= posicion < len(contactosActuales):
            contactosActuales.pop(posicion)
            escribirBaseDatos(contactosActuales)

    return redirect(url_for("mostrarInicio"))


if __name__ == "__main__":
    aplicacionAgenda.run(debug=True)
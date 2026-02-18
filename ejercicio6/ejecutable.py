from flask import Flask, render_template, request, redirect, url_for
import os

aplicacionGaleria = Flask(__name__, template_folder='plantilla', static_folder='plantilla')
rutaAlmacenamiento = os.path.join('plantilla', 'archivosSubidos')

if not os.path.exists(rutaAlmacenamiento):
    os.makedirs(rutaAlmacenamiento)


@aplicacionGaleria.route("/", methods=["GET"])
def mostrarGaleria():
    listaImagenes = os.listdir(rutaAlmacenamiento)
    return render_template("subida.html", imagenes=listaImagenes)


@aplicacionGaleria.route("/subirArchivo", methods=["POST"])
def subirArchivo():
    archivoRecibido = request.files.get("archivoImagen")

    if archivoRecibido and archivoRecibido.filename != "":
        nombreArchivo = archivoRecibido.filename
        rutaDestino = os.path.join(rutaAlmacenamiento, nombreArchivo)
        archivoRecibido.save(rutaDestino)

    return redirect(url_for("mostrarGaleria"))


if __name__ == "__main__":
    aplicacionGaleria.run(debug=True)
from flask import Flask, render_template, request

aplicacionTareas = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

listaDeTareas = []


@aplicacionTareas.route("/", methods=["GET", "POST"])
def gestionarListado():
    mensajeInformativo = ""

    if request.method == "POST":
        accionSolicitada = request.form.get("tipoAccion")

        if accionSolicitada == "agregarTarea":
            nuevaTarea = request.form.get("descripcionTarea")
            if nuevaTarea and nuevaTarea.strip():
                listaDeTareas.append(nuevaTarea.strip())

        elif accionSolicitada == "eliminarTarea":
            indiceRecibido = request.form.get("posicionTarea")
            if indiceRecibido is not None:
                indiceNumerico = int(indiceRecibido)
                if 0 <= indiceNumerico < len(listaDeTareas):
                    listaDeTareas.pop(indiceNumerico)

    return render_template("listadoTareas.html", tareas=listaDeTareas)


if __name__ == "__main__":
    aplicacionTareas.run(debug=True)
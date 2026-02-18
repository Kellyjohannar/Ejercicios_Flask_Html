from flask import Flask, render_template, request

aplicacionRegistro = Flask(__name__, template_folder='plantilla', static_folder='plantilla')


@aplicacionRegistro.route("/", methods=["GET", "POST"])
def gestionarRegistro():
    datosRecibidos = None

    if request.method == "POST":
        nombreCompleto = request.form.get("nombreUsuario")
        correoElectronico = request.form.get("correoUsuario")
        ciudadResidencia = request.form.get("ciudadUsuario")

        datosRecibidos = {
            "nombre": nombreCompleto,
            "correo": correoElectronico,
            "ciudad": ciudadResidencia,
            "autor": "Alexander"
        }

    return render_template("registro.html", informacion=datosRecibidos)


if __name__ == "__main__":
    aplicacionRegistro.run(debug=True)
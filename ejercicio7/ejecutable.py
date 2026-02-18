from flask import Flask, render_template
import requests

aplicacionConsulta = Flask(__name__, template_folder='plantilla', static_folder='plantilla')


@aplicacionConsulta.route("/", methods=["GET"])
def mostrarDatosExternos():
    urlServicioExterno = "https://jsonplaceholder.typicode.com/users"
    respuestaServidor = requests.get(urlServicioExterno)

    listaUsuariosApi = []

    if respuestaServidor.status_code == 200:
        listaUsuariosApi = respuestaServidor.json()

    return render_template("clienteApi.html", usuarios=listaUsuariosApi, nombreAutor="Alexander")


if __name__ == "__main__":
    aplicacionConsulta.run(debug=True)
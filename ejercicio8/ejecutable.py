from flask import Flask, render_template

aplicacionNavegacion = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

@aplicacionNavegacion.route("/")
def rutaInicio():
    return render_template("inicio.html")

@aplicacionNavegacion.route("/sobreMi")
def rutaSobreMi():
    return render_template("sobreMi.html")

@aplicacionNavegacion.route("/contacto")
def rutaContacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    aplicacionNavegacion.run(debug=True)
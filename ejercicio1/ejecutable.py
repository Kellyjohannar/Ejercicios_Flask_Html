#1) Conversor de unidades: formulario con selección (km<-->millas, ºC<-->ºF) y página de resultado.

# Se traen las herramientas necesarias de la librería flask
from flask import Flask, render_template, request

# Se crea la aplicación.
# Como la carpeta se llama plantilla y no templates, se le debe avisar a Flask esto se hace con template_folder
# El staric_folder se coloca para poderle poner estilos por medio de un CSS a la pagina.
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')


# Esta es la ruta principal. Cuando se entra a la web, se ve el formulario, con el @app.route se esta llamando aplicación.
@app.route("/", methods=["GET"])
def inicio():
    # 'render_template' busca el archivo dentro de la carpeta 'plantilla'
    return render_template("conversor.html")


# Esta ruta recibe los datos cuando se pulsa el botón de "Convertir"
@app.route("/convertir", methods=["POST"])
def convertir():
    try:
        # 1. Se obtiene el número que se escribio en el cuadro de texto
        valor = float(request.form.get("valor", "0"))

        # 2. Se obtiene la opción que se elegio en el menú desplegable
        operacion = request.form.get("opcion_conversion")

        # 3. Se hacen las cuentas según lo elegido
        if operacion == "km_a_millas":
            resultado = valor * 0.621371
            texto_final = f"{valor} Kilómetros son {resultado:.2f} Millas"

        elif operacion == "millas_a_km":
            resultado = valor / 0.621371
            texto_final = f"{valor} Millas son {resultado:.2f} Kilómetros"

        elif operacion == "c_a_f":
            resultado = (valor * 9 / 5) + 32
            texto_final = f"{valor} ºC son {resultado:.2f} ºF"

        elif operacion == "f_a_c":
            resultado = (valor - 32) * 5 / 9
            texto_final = f"{valor} ºF son {resultado:.2f} ºC"

        # 4. Enviamos el texto con el resultado a la página de resultado
        return render_template("resultado.html", res=texto_final)

    except ValueError:
        # Si el usuario escribe letras en lugar de números
        return render_template("resultado.html", res="Error: Ingresa un número válido")


# Se inicia el servidor en modo prueba
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

aplicacionConversor = Flask(__name__, template_folder='plantilla', static_folder='plantilla')


@aplicacionConversor.route("/", methods=["GET"])
def mostrarFormulario():
    return render_template("conversor.html")


@aplicacionConversor.route("/procesarConversion", methods=["POST"])
def procesarConversion():
    valorRecibido = request.form.get("valorEntrada", "0")
    tipoConversion = request.form.get("tipoSeleccionado")

    # Inicializamos variables para evitar retornos extraños dentro de los condicionales
    resultadoFinal = 0.0
    mensajeResultado = ""

    try:
        numeroAConvertir = float(valorRecibido)

        if tipoConversion == "kilometroAMilla":
            resultadoFinal = numeroAConvertir * 0.621371
            mensajeResultado = f"{numeroAConvertir} kilómetros equivalen a {resultadoFinal:.2f} millas."

        elif tipoConversion == "millaAKilometro":
            resultadoFinal = numeroAConvertir / 0.621371
            mensajeResultado = f"{numeroAConvertir} millas equivalen a {resultadoFinal:.2f} kilómetros."

        elif tipoConversion == "celsiusAFahrenheit":
            resultadoFinal = (numeroAConvertir * 9 / 5) + 32
            mensajeResultado = f"{numeroAConvertir} °C equivalen a {resultadoFinal:.2f} °F."

        elif tipoConversion == "fahrenheitACelsius":
            resultadoFinal = (numeroAConvertir - 32) * 5 / 9
            mensajeResultado = f"{numeroAConvertir} °F equivalen a {resultadoFinal:.2f} °C."

    except ValueError:
        mensajeResultado = "Error: Por favor, ingrese un número válido."

    return render_template("resultado.html", textoInformativo=mensajeResultado)


if __name__ == "__main__":
    aplicacionConversor.run(debug=True)
from flask import Flask, render_template, request

# Configuración de la aplicación con carpetas personalizadas
aplicacionSeguridad = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# Base de datos simulada en memoria
usuariosPermitidos = {
    "Alexander": "admin123",
    "Invitado": "1234"
}


@aplicacionSeguridad.route('/')
def mostrarInicio():
    return render_template('acceso.html')


@aplicacionSeguridad.route('/validarAcceso', methods=['POST'])
def validarAcceso():
    # Obtener datos del formulario con nombres descriptivos
    usuarioIngresado = request.form.get('nombreUsuario')
    contrasenaIngresada = request.form.get('claveUsuario')

    # Validación lógica sin uso de breaks ni retornos extraños
    mensajeRespuesta = ""
    esValido = False

    if usuarioIngresado in usuariosPermitidos:
        if usuariosPermitidos[usuarioIngresado] == contrasenaIngresada:
            esValido = True

    if esValido:
        # Si es correcto, mostramos bienvenida enviando el nombre completo
        return render_template('bienvenida.html', nombreCompleto=usuarioIngresado)

    # Si falla, mostramos la página de error
    return render_template('error.html')


if __name__ == '__main__':
    aplicacionSeguridad.run(debug=True)
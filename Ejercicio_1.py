from flask import Flask

# Usamos 'app' porque es el nombre que Flask busca por defecto
app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>¡Servidor Flask Funcionando!</h1><p>Ejercicio 1 completado</p>"

if __name__ == '__main__':
    app.run(debug=True)
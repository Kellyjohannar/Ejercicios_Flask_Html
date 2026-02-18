# Se importan Flask para el servidor, render_template para la web,
# request para la captura de datos y jsonify para la respuesta en formato JSON.
from flask import Flask, render_template, request, jsonify

# --- CONFIGURACIÓN DE LA APP ---
# Se inicializa la aplicación Flask.
# Se configura el acceso a HTML y CSS dentro de la carpeta 'plantilla'.
app = Flask(__name__, template_folder='plantilla', static_folder='plantilla')

# --- ALMACENAMIENTO TEMPORAL (MEMORIA) ---
# Se utiliza una lista de diccionarios para gestionar los elementos.
# Nota: Los datos son volátiles y se reinician al detener el servidor.
lista_items = [
    {"id": 1, "nombre": "Aprendiendo Flask"    },
    {"id": 2, "nombre": "Diseñando con CSS"}
]


# --- RUTA 1: INTERFAZ DE USUARIO  ---
# Se define la ruta raíz para la visualización de la interfaz gráfica.
@app.route("/")
def index():
    # Se renderiza el archivo HTML correspondiente al cliente de la API.
    return render_template("cliente_api.html")


# --- RUTA 2: CONSULTA DE DATOS ---
# Se establece el punto de acceso para la obtención de información.
# El método 'GET' se utiliza exclusivamente para la lectura de recursos.
@app.route("/api/items", methods=["GET"])
def obtener_items():
    # Se transforma la lista de Python al formato estándar JSON.
    # Se envía el resultado como respuesta al cliente.
    return jsonify(lista_items)


# --- RUTA 3: CREACIÓN DE RECURSOS ---
# Se define el punto de recepción para el registro de nuevos datos.
# El método 'POST' permite el envío de información desde el cliente al servidor.
@app.route("/api/items", methods=["POST"])
def crear_item():
    # Se extrae el cuerpo de la solicitud en formato JSON.
    datos_recibidos = request.json

    # Se obtiene el valor asociado a la clave "item" dentro de los datos.
    nuevo_texto = datos_recibidos.get("item")

    # Se genera una nueva estructura de datos (diccionario) con ID autoincremental.
    nuevo_item = {
        "id": len(lista_items) + 1,
        "nombre": nuevo_texto
    }

    # Se incorpora el nuevo registro a la lista principal en memoria.
    lista_items.append(nuevo_item)

    # Se devuelve un objeto JSON de confirmación tras procesar la solicitud con éxito.
    return jsonify({"mensaje": "Item agregado exitosamente", "item": nuevo_item})


# --- ARRANQUE DEL SISTEMA ---
if __name__ == "__main__":
    # Se inicia la ejecución del servidor web con el modo depurador activo.
    app.run(debug=True)
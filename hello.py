from flask import Flask

app = Flask(__name__)

# Lo primero es definir los puntos de entrada / ruta.

@app.route('/hello') # <-- Esto es un decorador.
def hello_world():
    return 'Hola, mundo'






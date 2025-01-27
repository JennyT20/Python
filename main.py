#Importar librerias
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

#Configuración de proyecto
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

#Métodos de llamada
@app.route("/api/")
def indice_contenidos():
    return "Hola, API"




#@app.route('/')
#def root():
#    return "root"  
#if __name__ == "_main_":
#    app.run(debug=True)


#FLASK_APP=Transaciones_rest.py flask run
#python3 Transaciones_rest.py  flask run
import os

from flask import Flask
from flask import request
from flask import Response
import requests

from bson import json_util
import json

from Transaciones import Transaciones
from Portatiles import Portatiles
from MongoDM import MongoDM
import Portatiles_rest

app = Flask(__name__)

data_manager = MongoDM(os.environ['URI_BD_T'],os.environ['BD_T'],os.environ['CO_T'])
transaciones = Transaciones(data_manager)


#DE PRESENTACION
@app.route('/transaciones/')
def index():
    return Response(json_util.dumps("REST DE TRANSACIONES"), status=200, mimetype="application/json")

#Funcion que añade la transacion de compra/venta
#Cuando alguien compra un portatil, ese alguien añadira una transacion de tipo compra (1)
#El dueño del portatil (su DNI) añadira una trasacion de tipo venta (2)
#Para esto interactua con el otro microservicio, es decir, Portatiles
@app.route('/transaciones/venderPortatil/<id_portatil>/<DNIcomprador>', methods=['POST'])
@app.route('/transaciones/venderPortatil/<id_portatil>/<DNIcomprador>/<comentario>', methods=['POST'])
def venderPortatil(id_portatil, DNIcomprador, comentario=""):
    _id = False
    cadena = "http://" + os.environ['HOST'] + ":" + os.environ['PORT'] + "/portatiles/seleccionarPortatil/" + id_portatil
    respuesta = requests.get(url = cadena)
    respuesta = json_util.loads(respuesta.content)
    if respuesta != False:
        cadena = "http://" + os.environ['HOST'] + ":" + os.environ['PORT'] + "/portatiles/cambiarStockPortatil/" + id_portatil + "/1"
        respuesta2 = requests.put(url = cadena)
        _id1 = transaciones.agregarTransacion(id_portatil, DNIcomprador, 1, comentario)
        _id2 = transaciones.agregarTransacion(id_portatil, respuesta.get("DNIvendedor"), 2, comentario)
        ids = []
        ids.append(_id1)
        ids.append(_id2)
    return Response(json_util.dumps(ids), status=200, mimetype="application/json")


@app.route('/transaciones/devolverPortatil/<id_portatil>/<DNIcomprador>', methods=['POST'])
@app.route('/transaciones/devolverPortatil/<id_portatil>/<DNIcomprador>/<comentario>', methods=['POST'])
def devolverPortatil(id_portatil, DNIcomprador, comentario=""):
    _id = False
    cadena = "http://" + os.environ['HOST'] + ":" + os.environ['PORT'] + "/portatiles/seleccionarPortatil/" + id_portatil
    respuesta = requests.get(url = cadena)
    respuesta = json_util.loads(respuesta.content)
    if respuesta != False:
        cadena = "http://" + os.environ['HOST'] + ":" + os.environ['PORT'] + "/portatiles/cambiarStockPortatil/" + id_portatil + "/0"
        respuesta2 = requests.put(url = cadena)
        _id = transaciones.agregarTransacion(id_portatil, DNIcomprador, 3, comentario)
    return Response(json_util.dumps(_id), status=200, mimetype="application/json")

@app.route('/transaciones/verEstadisticas/<DNIusuario>', methods=['GET'])
@app.route('/transaciones/verEstadisticas/<DNIusuario>/<int:tipo>', methods=['GET'])
def verEstadisticas(DNIusuario, tipo=0):
    if tipo != 0:
        mis_transaciones = transaciones.verEstadisticasFiltradasTipo(DNIusuario,tipo)
        return Response(json_util.dumps(mis_transaciones), status=200, mimetype="application/json")
    else:
        mis_transaciones = transaciones.verEstadisticas(DNIusuario)
        return Response(json_util.dumps(mis_transaciones), status=200, mimetype="application/json")

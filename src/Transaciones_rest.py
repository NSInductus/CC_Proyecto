#FLASK_APP=Transaciones_rest.py flask run
#python3 Transaciones_rest.py  flask run
import os

from flask import Flask
from flask import request
from flask import Response

from bson import json_util
import json

from Transaciones import Transaciones
from Portatiles import Portatiles
from MongoDM import MongoDM
import Portatiles_rest

app = Flask(__name__)

#data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BDT_ENVIRON'],os.environ['COT_ENVIRON'])
#transaciones = Transaciones(data_manager)

#data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BD_ENVIRON'],os.environ['CO_ENVIRON'])
#portatiles = Portatiles(data_manager)

data_manager = MongoDM('localhost:27017','PruebaT','ColeccionT')
transaciones = Transaciones(data_manager)

#data_manager = MongoDM('localhost:27017','PruebaP','ColeccionP')
#portatiles = Portatiles(data_manager)


#DE PRESENTACION
@app.route('/transaciones/')
def index():
    return Response(json_util.dumps("REST DE TRANSACIONES"), status=200, mimetype="application/json")

#PARA COMPROBAR
@app.route('/transaciones/numeroTransaciones', methods=['GET'])
def numeroTransaciones():
    return Response(json_util.dumps(transaciones.numeroTransaciones()), status=200, mimetype="application/json")


#PARA COMPROBAR
@app.route('/transaciones/seleccionarTransacion/<_id>', methods=['GET'])
def seleccionarTransacion(_id):
    transacion = transaciones.seleccionarTransacion(_id)
    return Response(json_util.dumps(transacion), status=200, mimetype="application/json")

@app.route('/transaciones/agregarTransacion/<id_portatil>/<DNIusuario>/<int:tipo>', methods=['POST'])
@app.route('/transaciones/agregarTransacion/<id_portatil>/<DNIusuario>/<int:tipo>/<comentario>', methods=['POST'])
def agregarTransacion(id_portatil, DNIusuario, tipo, comentario=""):
    _id = transaciones.agregarTransacion(id_portatil, DNIusuario, tipo, comentario)
    return Response(json_util.dumps(_id), status=200, mimetype="application/json")

##3
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>', methods=['POST'])
@app.route('/transaciones/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>/<SO>', methods=['POST'])
def agregarPortatil(marca, modelo, DNIvendedor, precio, comentario="", pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
    cliente_test = Portatiles_rest.app.test_client()
    respuesta = cliente_test.post('/portatiles/agregarPortatil/msi/gl62/333X/600')
    _id = json_util.loads(respuesta.data)
    return Response(json_util.dumps(_id), status=200, mimetype="application/json")

@app.route('/transaciones/seleccionarPortatil/<id_portatil>', methods=['GET'])
def seleccionarPortatil(id_portatil):
    cliente_test = Portatiles_rest.app.test_client()
    cadena = '/portatiles/seleccionarPortatil/' + id_portatil
    respuesta = cliente_test.get(cadena)
    respuesta = json_util.loads(respuesta.data)
    return Response(json_util.dumps(respuesta), status=200, mimetype="application/json")


@app.route('/transaciones/venderPortatil/<id_portatil>/<DNIcomprador>', methods=['POST'])
@app.route('/transaciones/venderPortatil/<id_portatil>/<DNIcomprador>/<comentario>', methods=['POST'])
def venderPortatil(id_portatil, DNIcomprador, comentario=""):
    _id = False
    cliente_test = Portatiles_rest.app.test_client()
    #Portatiles_rest.app.config['TESTING'] = test_prueba
    cadena = '/portatiles/seleccionarPortatil/' + id_portatil
    respuesta = cliente_test.get(cadena)

    respuesta = json.loads(respuesta.data)
    if respuesta != False:
        cadena = '/portatiles/cambiarStockPortatil/' + id_portatil + '/1'
        respuesta2 = cliente_test.put(cadena)
        _id = transaciones.agregarTransacion(id_portatil, DNIcomprador, 1, comentario)
        _id = transaciones.agregarTransacion(id_portatil, respuesta.get("DNIvendedor"), 2, comentario)
    return Response(json_util.dumps(_id), status=200, mimetype="application/json")


@app.route('/transaciones/devolverPortatil/<id_portatil>/<DNIcomprador>', methods=['POST'])
@app.route('/transaciones/devolverPortatil/<id_portatil>/<DNIcomprador>/<comentario>', methods=['POST'])
def devolverPortatil(id_portatil, DNIcomprador, comentario=""):
    _id = False
    cliente_test = Portatiles_rest.app.test_client()
    #Portatiles_rest.app.config['TESTING'] = test_prueba
    cadena = '/portatiles/seleccionarPortatil/' + id_portatil
    respuesta = cliente_test.get(cadena)
    if respuesta != False:
        cadena = '/portatiles/cambiarStockPortatil/' + id_portatil + '/0'
        respuesta = cliente_test.put(cadena)
        _id = transaciones.agregarTransacion(id_portatil, DNIcomprador, 3, comentario)
    return Response(json_util.dumps(_id), status=200, mimetype="application/json")

@app.route('/transaciones/verEstadisticas/<DNIusuario>', methods=['GET'])
@app.route('/transaciones/verEstadisticas/<DNIusuario>/<int:tipo>', methods=['GET'])
def verEstadisticas(DNIusuario, tipo=0):
    if tipo == 0:
        mis_transaciones = transaciones.verEstadisticasFiltradasTipo(DNIusuario,tipo)
        return Response(json_util.dumps(mis_transaciones), status=200, mimetype="application/json")
    else:
        mis_transaciones = transaciones.verEstadisticas(DNIusuario)
        return Response(json_util.dumps(mis_transaciones), status=200, mimetype="application/json")

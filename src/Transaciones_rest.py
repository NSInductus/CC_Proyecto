#FLASK_APP=Transaciones_rest.py flask run
#python3 Transaciones_rest.py  flask run
import os

from flask import Flask
from flask import request
from flask import Response

from bson import json_util

from Transaciones import Transaciones
from Portatiles import Portatiles
from MongoDM import MongoDM

app = Flask(__name__)

#data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BDT_ENVIRON'],os.environ['COT_ENVIRON'])
#transaciones = Transaciones(data_manager)

#data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BD_ENVIRON'],os.environ['CO_ENVIRON'])
#portatiles = Portatiles(data_manager)

data_manager = MongoDM('localhost:27017','PruebaT','ColeccionT')
transaciones = Transaciones(data_manager)

data_manager = MongoDM('localhost:28017','PruebaP','ColeccionP')
portatiles = Portatiles(data_manager)


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

@app.route('/transaciones/agregarTransacion/<id_portatil>/<DNIvendedor>/<int:tipo>', methods=['POST'])
@app.route('/transaciones/agregarTransacion/<id_portatil>/<DNIvendedor>/<int:tipo>/<comentario>', methods=['POST'])
def agregarTransacion(id_portatil, DNIvendedor, tipo, comentario=""):
    _id = transaciones.agregarTransacion(id_portatil, DNIvendedor, tipo, comentario)
    return Response(json_util.dumps(_id), status=200, mimetype="application/json")

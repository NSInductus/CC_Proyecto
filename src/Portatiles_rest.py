#FLASK_APP=Portatiles_rest.py flask run
#python3 Portatiles_rest.py  flask run
import os

from flask import Flask
from flask import request
from flask import Response

from bson import json_util

from Portatiles import Portatiles
from MongoDM import MongoDM

app = Flask(__name__)

#data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BD_ENVIRON'],os.environ['CO_ENVIRON'])
#portatiles = Portatiles(data_manager)

data_manager = MongoDM('localhost:27017','PruebaP','ColeccionP')
portatiles = Portatiles(data_manager)

#DE PRESENTACION
@app.route('/portatiles/')
def index():
    return Response(json_util.dumps("REST DE PORTATILES"), status=200, mimetype="application/json")

#PARA COMPROBAR
@app.route('/portatiles/numeroPortatilesEnBD', methods=['GET'])
def numeroPortatilesEnVenta():
    return Response(json_util.dumps(portatiles.numeroPortatilesEnBD()), status=200, mimetype="application/json")

#PARA COMPROBAR
@app.route('/portatiles/seleccionarPortatil/<_id>', methods=['GET'])
def seleccionarPortatil(_id):
    portatil = portatiles.seleccionarPortatil(_id)
    return Response(json_util.dumps(portatil), status=200, mimetype="application/json")

@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>', methods=['POST'])
@app.route('/portatiles/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>/<SO>', methods=['POST'])
def agregarPortatil(marca, modelo, DNIvendedor, precio, comentario="", pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
    _id = portatiles.agregarPortatil(marca, modelo, DNIvendedor, precio, comentario, pantalla, procesador, RAM, almacenamiento, grafica, bateria, SO)
    return Response(json_util.dumps(_id), status=200, mimetype="application/json")

@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>', methods=['PUT'])
@app.route('/portatiles/modificarPortatil/<_id>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>/<SO>', methods=['PUT'])
def modificarPortatil(_id, precio="", modelo="", marca="",comentario="",  pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
    modificado = portatiles.modificarPortatil(_id, precio, modelo, marca,comentario,  pantalla, procesador, RAM, almacenamiento, grafica, bateria, SO)
    return Response(json_util.dumps(modificado), status=200, mimetype="application/json")

@app.route('/portatiles/cambiarStockPortatil/<_id>/<int:vendido_nuevo>', methods=['PUT'])
def modificarStockPortatil(_id, vendido_nuevo):
    modificado = portatiles.cambiarStockPortatil(_id, vendido_nuevo)
    return Response(json_util.dumps(modificado), status=200, mimetype="application/json")


@app.route('/portatiles/eliminarPortatilPorIdVenta/<_id>', methods=['DELETE'])
def eliminarPortatilPorIdVenta(_id):
    eliminado = portatiles.eliminarPortatilPorIdVenta(_id)
    return Response(json_util.dumps(eliminado), status=200, mimetype="application/json")

@app.route('/portatiles/verPortatilesEnVentaDeUsuario/<DNIusuario>', methods=['GET'])
def verPortatilesEnVentaDeUsuario(DNIusuario):
    mis_portatiles = portatiles.buscarPortatilesEnVentaUsuario(DNIusuario)
    return Response(json_util.dumps(mis_portatiles), status=200, mimetype="application/json")

@app.route('/portatiles/buscarPortatilPorPrecio/<int:limite_inferior>/<int:limite_superior>', methods=['GET'])
def buscarPortatilPorPrecio(limite_inferior, limite_superior):
    buscados = portatiles.buscarPortatilPorPrecio(limite_inferior, limite_superior)
    return Response(json_util.dumps(buscados), status=200, mimetype="application/json")

@app.route('/portatiles/buscarPortatilPorModeloMarca/<modelo>/<marca>', methods=['GET'])
def buscarPortatilPorModeloMarca(modelo, marca):
    buscados = portatiles.buscarPortatilPorModeloMarca(modelo, marca)
    return Response(json_util.dumps(buscados), status=200, mimetype="application/json")

@app.route('/portatiles/compararPotatiles/<modelo>/<marca>', methods=['GET'])
def compararPotatiles(modelo, marca):
    iguales = portatiles.compararPotatiles(modelo, marca)
    return Response(json_util.dumps(iguales), status=200, mimetype="application/json")

#if __name__ == '__main__':
#    app.debug = True
#    app.run()

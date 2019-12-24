#FLASK_APP=Portatiles_rest.py flask run
#python3 Portatiles_rest.py  flask run

from flask import Flask
from flask import request
from flask import Response

import json

import Portatiles

app = Flask(__name__)

portatiles = Portatiles.Portatiles()

#DE PRESENTACION
@app.route('/')
def index():
    return Response(json.dumps("REST"), status=200, mimetype="application/json")

#Para comprobar
#http://127.0.0.1:5000/numeroPortatilesEnVenta
@app.route('/numeroPortatilesEnVenta', methods=['GET'])
def numeroPortatilesEnVenta():
    #return Response(str(portatiles.numeroPortatilesEnVenta()))
    return Response(json.dumps(portatiles.numeroPortatilesEnVenta()), status=200, mimetype="application/json")

#Para comprobar
#http://127.0.0.1:5000/seleccionarPortatil/1
@app.route('/seleccionarPortatil/<int:id_venta>', methods=['GET'])
def seleccionarPortatil(id_venta):
    portatil = portatiles.seleccionarPortatil(id_venta)
    #return Response(str(id_venta))
    return Response(json.dumps(portatil), status=200, mimetype="application/json")

#http://127.0.0.1:5000/agregarPortatil/msi/gl62/333X/600
#http://127.0.0.1:5000/agregarPortatil/msi/gl62/333X/600/Muy%20bueno/15/i7/GB%20DDR4/1gb/GTX/2H/Linux
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>', methods=['GET', 'POST'])
@app.route('/agregarPortatil/<marca>/<modelo>/<DNIvendedor>/<int:precio>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>/<SO>', methods=['GET', 'POST'])
def agregarPortatil(marca, modelo, DNIvendedor, precio, comentario="", pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
    id_venta = portatiles.agregarPortatil(marca, modelo, DNIvendedor, precio, comentario, pantalla, procesador, RAM, almacenamiento, grafica, bateria, SO)
    #return Response(str(id_venta))
    return Response(json.dumps(id_venta), status=200, mimetype="application/json")


#http://127.0.0.1:5000/modificarPortatil/1/800000
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>', methods=['GET', 'UPDATE'])
@app.route('/modificarPortatil/<int:id_venta>/<int:precio>/<modelo>/<marca>/<comentario>/<pantalla>/<procesador>/<RAM>/<almacenamiento>/<grafica>/<bateria>/<SO>', methods=['GET', 'UPDATE'])
def modificarPortatil(id_venta, precio="", modelo="", marca="",comentario="",  pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
    modificado = portatiles.modificarPortatil(id_venta, precio, modelo, marca,comentario,  pantalla, procesador, RAM, almacenamiento, grafica, bateria, SO)
    #return Response(str(id_venta))
    return Response(json.dumps(modificado), status=200, mimetype="application/json")

#http://127.0.0.1:5000/eliminarPortatilPorIdVenta/1/80000
@app.route('/eliminarPortatilPorIdVenta/<int:id_venta>', methods=['GET','DELETE'])
def eliminarPortatilPorIdVenta(id_venta):
    eliminado = portatiles.eliminarPortatilPorIdVenta(id_venta)
    #return Response(str(id_venta))
    return Response(json.dumps(eliminado), status=200, mimetype="application/json")


#http://127.0.0.1:5000/verPortatilesEnVentaDeUsuario/333X
@app.route('/verPortatilesEnVentaDeUsuario/<DNIusuario>', methods=['GET'])
def verPortatilesEnVentaDeUsuario(DNIusuario):
    mis_portatiles = portatiles.portatiles_en_venta_de_usuario(DNIusuario)
    #return Response(str(id_venta))
    return Response(json.dumps(mis_portatiles), status=200, mimetype="application/json")


#http://127.0.0.1:5000/buscarPortatilPorPrecio/500/1000
@app.route('/buscarPortatilPorPrecio/<int:limite_inferior>/<int:limite_superior>', methods=['GET'])
def buscarPortatilPorPrecio(limite_inferior, limite_superior):
    buscados = portatiles.buscar_portatil_por_precio(limite_inferior, limite_superior)
    #return Response(str(id_venta))
    return Response(json.dumps(buscados), status=200, mimetype="application/json")


#http://127.0.0.1:5000/buscarPortatilPorModeloMarca/gl62/msi
@app.route('/buscarPortatilPorModeloMarca/<modelo>/<marca>', methods=['GET'])
def buscarPortatilPorModeloMarca(modelo, marca):
    buscados = portatiles.buscar_portatil_por_modelo_marca(modelo, marca)
    #return Response(str(id_venta))
    return Response(json.dumps(buscados), status=200, mimetype="application/json")



#http://127.0.0.1:5000/compararPotatiles/gl62/msi
@app.route('/compararPotatiles/<modelo>/<marca>', methods=['GET'])
def compararPotatiles(modelo, marca):
    iguales = portatiles.comparar_portatiles(modelo, marca)
    #return Response(str(id_venta))
    return Response(json.dumps(iguales), status=200, mimetype="application/json")

if __name__ == '__main__':
    app.debug = True
    app.run()

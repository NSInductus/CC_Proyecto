import pytest
import sys
import os

sys.path.append('src')

import bson

from Transaciones import Transaciones
#from Portatiles import Portatiles
from MongoDM import MongoDM

#data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BD_ENVIRON'],os.environ['CO_ENVIRON'])
#nueva_lista_p = Portatiles(data_manager)

data_manager = MongoDM(os.environ['URI_ENVIRON'],'Nueva','COTransaciones')
nueva_lista = Transaciones(data_manager)



def funcion_inicio():
    data_manager = MongoDM(os.environ['URI_ENVIRON'],'Nueva','COTransaciones')
    nueva_lista = Transaciones(data_manager)
    nueva_lista.limpiarLista()

def funcion_fin():
    data_manager = MongoDM(os.environ['URI_ENVIRON'],'Nueva','COTransaciones')
    nueva_lista = Transaciones(data_manager)
    nueva_lista.limpiarLista()

@pytest.fixture
def cliente_test():
    funcion_inicio()
    yield cliente_test
    funcion_fin()


def test_lista_transaciones_vacia(cliente_test):
    #nueva_lista.limpiarLista()
    assert nueva_lista.numeroTransaciones() == 0
    assert nueva_lista.seleccionarTransacion("1") == False

def test_agregar_y_seleccionar_nueva_transacion(cliente_test):
    #nueva_lista.limpiarLista()
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    assert nueva_lista.numeroTransaciones() == 1
    #portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    transacion = {"_id":bson.ObjectId(indice), "id_portatil": "e23rewr2wqe43242t", "DNIvendedor": "333X", "tipo":1, "comentario":""}
    assert nueva_lista.seleccionarTransacion(indice) == transacion

#def test_agregar_nuevo_portatil():
#    nueva_lista.limpiarLista()
#    nueva_lista_p.limpiarLista()
#    i = nueva_lista_p.agregarPortatil("MSI","GL62M","333X",2000)
#    indice = nueva_lista.agregarTransacion(i, "333X", 1)
#    assert nueva_lista.numeroTransaciones() == 1
    #portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
#    transacion = {"_id":bson.ObjectId(indice), "id_portatil": i, "DNIvendedor": "333X", "tipo":1, "comentario":""}
#    assert nueva_lista.seleccionarTransacion(indice) == transacion


def test_agregar_y_seleccionar_nuevo_transacion_con_comentario(cliente_test):
    #nueva_lista.limpiarLista()
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    assert nueva_lista.numeroTransaciones() == 1
    #portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    transacion = {"_id":bson.ObjectId(indice), "id_portatil": "e23rewr2wqe43242t", "DNIvendedor": "333X", "tipo":1, "comentario":"Soy un comentario"}
    assert nueva_lista.seleccionarTransacion(indice) == transacion

def test_eliminar_portatil(cliente_test):
    #nueva_lista.limpiarLista()
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    assert nueva_lista.numeroTransaciones() == 1
    assert nueva_lista.eliminarTransacion("90") == False
    assert nueva_lista.numeroTransaciones() == 1
    assert nueva_lista.eliminarTransacion(indice) == True
    assert nueva_lista.numeroTransaciones() == 0
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    indice2 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    assert nueva_lista.eliminarTransacion(indice) == True
    assert nueva_lista.numeroTransaciones() == 1



def test_estadisticas(cliente_test):
    nueva_lista.limpiarLista()
    mis_transaciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transaciones) == 0
    indice1 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    indice2 = nueva_lista.agregarTransacion("e23rqweqq4q3242t", "334X", 1)
    indice3 = nueva_lista.agregarTransacion("e12312442ed2d322t", "333X", 1)
    mis_transaciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transaciones) == 2
    transacion1 = {"_id":bson.ObjectId(indice1), "id_portatil": "e23rewr2wqe43242t", "DNIvendedor": "333X", "tipo":1, "comentario":""}
    transacion3 = {"_id":bson.ObjectId(indice3), "id_portatil": "e12312442ed2d322t", "DNIvendedor": "333X", "tipo":1, "comentario":""}
    assert mis_transaciones[0] == transacion1
    assert mis_transaciones[1] == transacion3
    assert nueva_lista.eliminarTransacion(indice1) == True
    mis_transaciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transaciones) == 1
    assert mis_transaciones[0] == transacion3



def test_imprimir_comparacion(cliente_test):
    nueva_lista.limpiarLista()
    indice1 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    indice2 = nueva_lista.agregarTransacion("e23rqweqq4q3242t", "333X", 1)
    indice3 = nueva_lista.agregarTransacion("e12312442ed2d322t", "333X", 1)
    mis_transaciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transaciones) == 3
    nueva_lista.imprimirComparacion(mis_transaciones, "transaciones.pdf")

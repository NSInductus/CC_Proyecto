import pytest
import sys
import os

sys.path.append('src')

import bson

from Transacciones import Transacciones
from MongoDM import MongoDM

data_manager = MongoDM(os.environ['URI_BD_T'], os.environ['BD_T'], os.environ['CO_T'])
nueva_lista = Transacciones(data_manager)

def funcion_inicio():
    data_manager = MongoDM(os.environ['URI_BD_T'], os.environ['BD_T'], os.environ['CO_T'])
    nueva_lista = Transacciones(data_manager)
    nueva_lista.limpiarLista()

@pytest.fixture
def cliente_test():
    funcion_inicio()
    yield cliente_test

def test_lista_transacciones_vacia(cliente_test):
    assert nueva_lista.numeroTransacciones() == 0
    assert nueva_lista.seleccionarTransacion("1") == False

def test_agregar_y_seleccionar_nueva_transacion(cliente_test):
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    assert nueva_lista.numeroTransacciones() == 1
    transacion = {"_id":bson.ObjectId(indice), "id_portatil": "e23rewr2wqe43242t", "DNIusuario": "333X", "tipo":1, "comentario":""}
    assert nueva_lista.seleccionarTransacion(indice) == transacion

def test_agregar_y_seleccionar_nuevo_transacion_con_comentario(cliente_test):
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    assert nueva_lista.numeroTransacciones() == 1
    #portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIusuario":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    transacion = {"_id":bson.ObjectId(indice), "id_portatil": "e23rewr2wqe43242t", "DNIusuario": "333X", "tipo":1, "comentario":"Soy un comentario"}
    assert nueva_lista.seleccionarTransacion(indice) == transacion

def test_agregar_varias_transacciones(cliente_test):
    indice1 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    indice2 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    indice3 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    indice4 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    assert nueva_lista.numeroTransacciones() == 4
    transacion1 = {"_id":bson.ObjectId(indice1), "id_portatil": "e23rewr2wqe43242t", "DNIusuario": "333X", "tipo":1, "comentario":""}
    transacion2 = {"_id":bson.ObjectId(indice2), "id_portatil": "e23rewr2wqe43242t", "DNIusuario": "333X", "tipo":1, "comentario":""}
    transacion3 = {"_id":bson.ObjectId(indice3), "id_portatil": "e23rewr2wqe43242t", "DNIusuario": "333X", "tipo":1, "comentario":""}
    transacion4 = {"_id":bson.ObjectId(indice4), "id_portatil": "e23rewr2wqe43242t", "DNIusuario": "333X", "tipo":1, "comentario":""}
    assert nueva_lista.seleccionarTransacion(indice1) == transacion1
    assert nueva_lista.seleccionarTransacion(indice2) == transacion2
    assert nueva_lista.seleccionarTransacion(indice3) == transacion3
    assert nueva_lista.seleccionarTransacion(indice4) == transacion4

def test_eliminar_portatil(cliente_test):
    #nueva_lista.limpiarLista()
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    assert nueva_lista.numeroTransacciones() == 1
    assert nueva_lista.eliminarTransacion("90") == False
    assert nueva_lista.numeroTransacciones() == 1
    assert nueva_lista.eliminarTransacion(indice) == True
    assert nueva_lista.numeroTransacciones() == 0
    indice = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    indice2 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1, "Soy un comentario")
    assert nueva_lista.eliminarTransacion(indice) == True
    assert nueva_lista.numeroTransacciones() == 1

def test_estadisticas(cliente_test):
    nueva_lista.limpiarLista()
    mis_transacciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transacciones) == 0
    indice1 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    indice2 = nueva_lista.agregarTransacion("e23rqweqq4q3242t", "334X", 1)
    indice3 = nueva_lista.agregarTransacion("e12312442ed2d322t", "333X", 1)
    mis_transacciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transacciones) == 2
    transacion1 = {"_id":bson.ObjectId(indice1), "id_portatil": "e23rewr2wqe43242t", "DNIusuario": "333X", "tipo":1, "comentario":""}
    transacion3 = {"_id":bson.ObjectId(indice3), "id_portatil": "e12312442ed2d322t", "DNIusuario": "333X", "tipo":1, "comentario":""}
    assert mis_transacciones[0] == transacion1
    assert mis_transacciones[1] == transacion3
    assert nueva_lista.eliminarTransacion(indice1) == True
    mis_transacciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transacciones) == 1
    assert mis_transacciones[0] == transacion3

#Realmente lo que es el resultado del PFD no se puede testear
def test_imprimir_comparacion(cliente_test):
    nueva_lista.limpiarLista()
    indice1 = nueva_lista.agregarTransacion("e23rewr2wqe43242t", "333X", 1)
    indice2 = nueva_lista.agregarTransacion("e23rqweqq4q3242t", "333X", 1)
    indice3 = nueva_lista.agregarTransacion("e12312442ed2d322t", "333X", 1)
    mis_transacciones = nueva_lista.verEstadisticas("333X")
    assert len(mis_transacciones) == 3
    nueva_lista.imprimirComparacion(mis_transacciones, "transacciones.pdf")

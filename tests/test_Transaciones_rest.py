import pytest
import sys
import os

sys.path.append('src')

import json
from bson import json_util

import Transaciones_rest
import Portatiles_rest
from Transaciones import Transaciones
from Portatiles import Portatiles
from MongoDM import MongoDM

def funcion_inicio():

    data_manager = MongoDM(os.environ['URI_BD_T'],os.environ['BD_T'],os.environ['CO_T'])
    transaciones = Transaciones(data_manager)
    transaciones.limpiarLista()

@pytest.fixture
def cliente_test():
    funcion_inicio()
    cliente_test = Transaciones_rest.app.test_client()
    cliente_test_portatil = Portatiles_rest.app.test_client()
    yield cliente_test, cliente_test_portatil


def test_transaciones_rest_prueba(cliente_test):
    respuesta = cliente_test[0].get('/transaciones/')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == "REST DE TRANSACIONES"
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_transaciones_rest_ruta_desconocida(cliente_test):
    respuesta = cliente_test[0].get('/transaciones/kokoko')
    if (respuesta.status_code == 204):
        assert (respuesta.status_code == 204)

def test_transaciones_rest_prueba_vender_portatil(cliente_test):
    #Seleccionar portatil
    cadena = '/portatiles/agregarPortatil/msi/gl62/333X/600'
    respuesta = cliente_test[1].post(cadena)
    indice = json.loads(respuesta.data)
    #Utilizamos $oid en lugar de ObjectId porque es como se obtiene al realizar el json.loads
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #
    cadena = 'portatiles/seleccionarPortatil/' + indice
    respuesta = cliente_test[1].get(cadena)
    portatil = {"_id":{"$oid": indice}, "marca":"msi", "modelo":"gl62", "DNIvendedor":"333X", "precio":600, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    DNIvendedor = 0
    respuesta_copia_data = json.loads(respuesta.data)
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json.loads(respuesta.data) == portatil
        DNIvendedor = respuesta_copia_data.get("DNIvendedor")
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    DNIcomprador = "555X"
    cadena = '/transaciones/venderPortatil/' + indice + '/' + DNIcomprador
    respuesta = cliente_test[0].post(cadena)

def test_transaciones_rest_prueba_devolver_portatil(cliente_test):
    #Seleccionar portatil
    cadena = '/portatiles/agregarPortatil/msi/gl62/333X/600'
    respuesta = cliente_test[1].post(cadena)
    indice = json.loads(respuesta.data)
    #Utilizamos $oid en lugar de ObjectId porque es como se obtiene al realizar el json.loads
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #
    cadena = 'portatiles/seleccionarPortatil/' + indice
    respuesta = cliente_test[1].get(cadena)
    portatil = {"_id":{"$oid": indice}, "marca":"msi", "modelo":"gl62", "DNIvendedor":"333X", "precio":600, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    DNIvendedor = 0
    respuesta_copia_data = json.loads(respuesta.data)
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json.loads(respuesta.data) == portatil
        DNIvendedor = respuesta_copia_data.get("DNIvendedor")
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    DNIcomprador = "555X"
    cadena = '/transaciones/devolverPortatil/' + indice + '/' + DNIcomprador
    respuesta = cliente_test[0].post(cadena)

#Funciones de ver estadisticas del API
def test_transaciones_rest_ver_estadisticas(cliente_test):
    lista = []
    respuesta = cliente_test[0].get('/transaciones/verEstadisticas/666X')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json.loads(respuesta.data) == lista
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_transaciones_rest_ver_estadisticas_tipo(cliente_test):
    lista = []
    respuesta = cliente_test[0].get('/transaciones/verEstadisticas/666X/1')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json.loads(respuesta.data) == lista
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

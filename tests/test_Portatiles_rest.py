import pytest
import sys
import os

sys.path.append('src')

from bson import json_util

import Portatiles_rest
from Portatiles import Portatiles
from MongoDM import MongoDM

#app = Portatiles_rest.app.test_client()

def funcion_inicio():
    data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BD_ENVIRON'],os.environ['CO_ENVIRON'])
    portatiles = Portatiles(data_manager)

def funcion_fin():
    data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BD_ENVIRON'],os.environ['CO_ENVIRON'])
    portatiles = Portatiles(data_manager)
    portatiles.limpiarLista()

@pytest.fixture
def cliente_test():
    funcion_inicio()
    cliente_test = Portatiles_rest.app.test_client()
    Portatiles_rest.app.config['TESTING'] = test_prueba
    yield cliente_test
    funcion_fin()

def test_prueba(cliente_test):
    respuesta = cliente_test.get('/portatiles/')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == "REST DE PORTATILES"
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_rest_ruta_desconocida(cliente_test):
    respuesta = cliente_test.get('/portatiles/kokoko')
    if (respuesta.status_code == 204):
        assert (respuesta.status_code == 204)

#modificar
def test_rest_numero_portatiles(cliente_test):
    respuesta = cliente_test.get('/portatiles/numeroPortatilesEnBD')
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


def est_rest_agregar_portatil_y_seleccionar_version_corta(cliente_test):
    #Agregar portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/msi/gl62/333X/600')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Seleccionar portatil
    cadena = '/portatiles/seleccionarPortatil/' + indice
    respuesta = cliente_test.get(cadena)
    #Utilizamos $oid en lugar de ObjectId porque es como se obtiene al realizar el json.loads
    portatil = {"_id":{"$oid": indice}, "marca":"msi", "modelo":"gl62", "DNIvendedor":"333X", "precio":600, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == portatil
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_rest_agregar_portatil_y_seleccionar_version_larga(cliente_test):
    #Agregar portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/msi/gl62/333X/600/Muy%20bueno/15/i7/GB%20DDR4/1gb/GTX/2H/Linux')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Seleccionar portatil
    cadena = '/portatiles/seleccionarPortatil/' + indice
    respuesta = cliente_test.get(cadena)
    #Utilizamos $oid en lugar de ObjectId porque es como se obtiene al realizar el json.loads
    portatil = {"_id":{"$oid": indice}, "marca":"msi", "modelo":"gl62", "DNIvendedor":"333X", "precio":600, "pantalla":"15", "procesador":"i7", "RAM":"GB DDR4", "almacenamiento":"1gb", "grafica":"GTX", "bateria":"2H", "SO":"Linux",  "comentario":"Muy bueno", "vendido":0}
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == portatil
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_rest_modificar_portatil_solo_precio_y_seleccionar(cliente_test):
    #Agregar Portatil para posteriormente modificarlo
    respuesta = cliente_test.post('/portatiles/agregarPortatil/msi/gl62/333X/600')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Modificar portatil
    cadena = '/portatiles/modificarPortatil/' + indice + '/5555'
    respuesta = cliente_test.put(cadena)
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
    #Seleccionar portatil modificado
    portatil = {"_id":{"$oid": indice}, "marca":"msi", "modelo":"gl62", "DNIvendedor":"333X", "precio":5555, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    cadena = '/portatiles/seleccionarPortatil/' + indice
    respuesta = cliente_test.get(cadena)
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == portatil
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_rest_eliminar_portatil(cliente_test):
    respuesta = cliente_test.post('/portatiles/agregarPortatil/msi/gl62/333X/600')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Eliminar portatil
    cadena = '/portatiles/eliminarPortatilPorIdVenta/' + indice
    respuesta = cliente_test.delete(cadena)
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
    #Seleccionar portatil
    cadena = '/portatiles/seleccionarPortatil/' + indice
    respuesta = cliente_test.get(cadena)
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        #Utilizamos None porque es lo que devuelve
        assert json_util.loads(respuesta.data) == None
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_rest_buscar_portatil_dnivendedor(cliente_test):
    respuesta = cliente_test.get('/portatiles/verPortatilesEnVentaDeUsuario/666X')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice1 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Agregar otro portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/lg/gram/666X/1100')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice2 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Buscar por ID venta
    #Portatiles agregados
    portatil1 = {"_id":{"$oid": indice1}, "marca":"msi", "modelo":"gl62", "DNIvendedor":"666X", "precio":600, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    portatil2 = {"_id":{"$oid": indice2}, "marca":"lg", "modelo":"gram", "DNIvendedor":"666X", "precio":1100, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    #Agregan a lista para comparar
    lista = [portatil1, portatil2]
    respuesta = cliente_test.get('/portatiles/verPortatilesEnBDDeUsuario/666X')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == lista
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_rest_buscar_portatil_precio(cliente_test):
    #Agregar portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/msi/gl62/333X/100000')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice1 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Agregar otro portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/lg/gram/333X/100000')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice2 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Buscar por ID venta
    #Portatiles agregados
    portatil1 = {"_id":{"$oid": indice1}, "marca":"msi", "modelo":"gl62", "DNIvendedor":"333X", "precio":100000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    portatil2 = {"_id":{"$oid": indice2}, "marca":"lg", "modelo":"gram", "DNIvendedor":"333X", "precio":100000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    #Agregan a lista para comparar
    lista = [portatil1, portatil2]
    respuesta = cliente_test.get('/portatiles/buscarPortatilPorPrecio/99999/120000')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == lista
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)


def test_rest_buscar_portatil_modelo_marca(cliente_test):
    #Agregar portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/marca_especial/modelo_especial/333X/600')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice1 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Agregar otro portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/marca_especial/modelo_especial/333X/1100')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice2 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Buscar por ID venta
    #Portatiles agregados
    portatil1 = {"_id":{"$oid": indice1}, "marca":"marca_especial", "modelo":"modelo_especial", "DNIvendedor":"333X", "precio":600, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    portatil2 = {"_id":{"$oid": indice2}, "marca":"marca_especial", "modelo":"modelo_especial", "DNIvendedor":"333X", "precio":1100, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    #Agregan a lista para comparar
    lista = [portatil1, portatil2]
    respuesta = cliente_test.get('/portatiles/buscarPortatilPorModeloMarca/modelo_especial/marca_especial')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == lista
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

def test_rest_comparar_portatiles(cliente_test):
    #Diferencia con el test anterior es el orden de los elementos puesto que los ordena por precio
    #Agregar portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/marca_especial_com/modelo_especial_com/333X/6000')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice1 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Agregar otro portatil
    respuesta = cliente_test.post('/portatiles/agregarPortatil/marca_especial_com/modelo_especial_com/333X/1100')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        indice2 = json_util.loads(respuesta.data)
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)
    #Buscar por ID venta
    #Portatiles agregados
    portatil1 = {"_id":{"$oid": indice1}, "marca":"marca_especial_com", "modelo":"modelo_especial_com", "DNIvendedor":"333X", "precio":6000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    portatil2 = {"_id":{"$oid": indice2}, "marca":"marca_especial_com", "modelo":"modelo_especial_com", "DNIvendedor":"333X", "precio":1100, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":"", "vendido":0}
    #Agregan a lista para comparar
    lista = [portatil1, portatil2]
    respuesta = cliente_test.get('/portatiles/buscarPortatilPorModeloMarca/modelo_especial_com/marca_especial_com')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
        assert json_util.loads(respuesta.data) == lista
    elif (respuesta.status_code == 413):
        assert (respuesta.status_code == 413)
    elif (respuesta.status_code == 414):
        assert (respuesta.status_code == 414)
    elif (respuesta.status_code == 429):
        assert (respuesta.status_code == 429)
    else:
        assert (respuesta.status_code == 412)

#Borra todos los registros introducidos durante las pruebas, puesto que => DNIvendedor XXXPRUEBAX
def test_limpiar_bd_y_comprobar_vacia(cliente_test):
    respuesta = cliente_test.get('/portatiles/verPortatilesEnBDDeUsuario/666X')
    lista1 = json_util.loads(respuesta.data)
    print(lista1)
    respuesta = cliente_test.get('/portatiles/verPortatilesEnBDDeUsuario/333X')
    lista2 = json_util.loads(respuesta.data)
    lista = lista1 + lista2
    print(lista2)
    for portatil in lista:
        id = portatil.get("_id")
        id = id.get("$oid")
        print(id)
        cadena = '/portatiles/eliminarPortatilPorIdVenta/' + id
        respuesta = cliente.delete(cadena)

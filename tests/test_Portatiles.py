import pytest
import sys
import os

sys.path.append('src')

import bson

from Portatiles import Portatiles
from MongoDM import MongoDM

data_manager = MongoDM(os.environ['URI_ENVIRON'],os.environ['BD_ENVIRON'],os.environ['CO_ENVIRON'])
nueva_lista = Portatiles(data_manager)

def test_lista_portatiles_vacia():
    nueva_lista.limpiar_lista()
    assert nueva_lista.numeroPortatilesEnBD() == 0
    assert nueva_lista.seleccionarPortatil("1") == False

def test_agregar_nuevo_portatil():
    nueva_lista.limpiar_lista()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnBD() == 1
    portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice) == portatil

def test_agregar_nuevo_portatil_version_larga():
    nueva_lista.limpiar_lista()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000, "Muy bueno", "16", "intel core i7", "8GB DDR4", "1 TB", "nvidia geforce GTX 1050", "3 H", "Ninguno")
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"16", "procesador":"intel core i7", "RAM":"8GB DDR4", "almacenamiento":"1 TB", "grafica":"nvidia geforce GTX 1050", "bateria":"3 H", "SO":"Ninguno",  "comentario":"Muy bueno"}
    assert nueva_lista.seleccionarPortatil(indice) == portatil

def test_agregar_varios_portatiles():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    indice4 = nueva_lista.agregarPortatil("MSI","GL62M","555X",2002)
    indice5 = nueva_lista.agregarPortatil("MSI","GL90","888X",1208)
    assert nueva_lista.numeroPortatilesEnVenta() == 5
    portatil1 = {"_id":bson.ObjectId(indice1), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice1) == portatil1
    portatil2 = {"_id":bson.ObjectId(indice2), "marca":"ASUN", "modelo":"TUF", "DNIvendedor":"333X", "precio":1500, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice2) == portatil2
    portatil3 = {"_id":bson.ObjectId(indice3), "marca":"ACER", "modelo":"Aspire 3", "DNIvendedor":"333X", "precio":957, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice3) == portatil3
    portatil4 = {"_id":bson.ObjectId(indice4), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"555X", "precio":2002, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice4) == portatil4
    portatil5 = {"_id":bson.ObjectId(indice5), "marca":"MSI", "modelo":"GL90", "DNIvendedor":"888X", "precio":1208, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice5) == portatil5

def test_eliminar_portatil():
    nueva_lista.limpiar_lista()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    assert nueva_lista.eliminarPortatilPorIdVenta("90") == False
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    assert nueva_lista.indiceEnListaIDventa(indice) == 0
    assert nueva_lista.eliminarPortatilPorIdVenta(indice) == True
    assert nueva_lista.numeroPortatilesEnBD() == 0
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    assert nueva_lista.eliminarPortatilPorIdVenta(indice) == True
    assert nueva_lista.numeroPortatilesEnBD() == 1

def test_modificar_portatil():
    nueva_lista.limpiar_lista()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnBD() == 1
    portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice) == portatil
    assert nueva_lista.modificarPortatil(indice, 1500,"GL82M","MSI-PLUS") == True
    portatil_modificado = {"_id":bson.ObjectId(indice), "marca":"MSI-PLUS", "modelo":"GL82M", "DNIvendedor":"333X", "precio":1500, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice) == portatil_modificado

def test_modificar_portatil_version_larga():
    nueva_lista.limpiar_lista()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000, "Muy bueno", "16", "intel core i7", "8GB DDR4", "1 TB", "nvidia geforce GTX 1050", "3 H", "Ninguno")
    assert nueva_lista.numeroPortatilesEnBD() == 1
    portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"16", "procesador":"intel core i7", "RAM":"8GB DDR4", "almacenamiento":"1 TB", "grafica":"nvidia geforce GTX 1050", "bateria":"3 H", "SO":"Ninguno",  "comentario":"Muy bueno"}
    assert nueva_lista.seleccionarPortatil(indice) == portatil
    assert nueva_lista.modificarPortatil(indice, 1500,"GL82M","MSI-PLUS", "Oferta, bajada de precio y aumento RAM", "16", "intel core i7", "16GB DDR4" ) == True
    portatil_modificado = {"_id":bson.ObjectId(indice), "marca":"MSI-PLUS", "modelo":"GL82M", "DNIvendedor":"333X", "precio":1500, "pantalla":"16", "procesador":"intel core i7", "RAM":"16GB DDR4", "almacenamiento":"1 TB", "grafica":"nvidia geforce GTX 1050", "bateria":"3 H", "SO":"Ninguno",  "comentario":"Oferta, bajada de precio y aumento RAM"}
    assert nueva_lista.seleccionarPortatil(indice) == portatil_modificado

def test_modificar_portatil_2():
    nueva_lista.limpiar_lista()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    portatil = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice) == portatil
    assert nueva_lista.modificarPortatil(indice, 4000) == True
    portatil_modificado = {"_id":bson.ObjectId(indice), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":4000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice) == portatil_modificado

def test_varias_pruebas_agregar_modificar_eliminar():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    assert nueva_lista.numeroPortatilesEnVenta() == 3
    assert nueva_lista.eliminarPortatilPorIdVenta(indice2) == True
    assert nueva_lista.modificarPortatil(indice1,400,"Modelo","Marca") == True
    portatil_modificado = {"IDventa":indice1, "marca":"Marca", "modelo":"Modelo", "DNIvendedor":"333X", "precio":400, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert nueva_lista.seleccionarPortatil(indice1) == portatil_modificado
    assert nueva_lista.numeroPortatilesEnVenta() == 2
    assert nueva_lista.eliminarPortatilPorIdVenta(indice1) == True
    assert nueva_lista.eliminarPortatilPorIdVenta(indice3) == True
    assert nueva_lista.numeroPortatilesEnVenta() == 0

def test_indices():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    assert nueva_lista.numeroPortatilesEnBD() == 3
    assert nueva_lista.eliminarPortatilPorIdVenta(indice2) == True
    indice4 = nueva_lista.agregarPortatil("ASUN","TUF2","373X",947)
    assert indice1 != indice2 != indice3 != indice4

def test_portatiles_en_venta_de_usuario():
    nueva_lista.limpiar_lista()
    mis_portatiles_en_venta = nueva_lista.portatiles_en_venta_de_usuario("333X")
    assert len(mis_portatiles_en_venta) == 0
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","345X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    mis_portatiles_en_venta = nueva_lista.portatiles_en_venta_de_usuario("333X")
    assert len(mis_portatiles_en_venta) == 2
    portatil1 = {"_id":bson.ObjectId(indice1), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    portatil2 = {"_id":bson.ObjectId(indice3), "marca":"ACER", "modelo":"Aspire 3", "DNIvendedor":"333X", "precio":957, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert mis_portatiles_en_venta[0] == portatil1
    assert mis_portatiles_en_venta[1] == portatil2
    assert nueva_lista.eliminarPortatilPorIdBD(indice1) == True
    mis_portatiles_en_venta = nueva_lista.portatiles_en_venta_de_usuario("333X")
    assert len(mis_portatiles_en_venta) == 1
    assert mis_portatiles_en_venta[0] == portatil2


def test_buscar_portatil_por_precio():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    portatiles_busqueda = nueva_lista.buscar_portatil_por_precio(0, 1000)
    assert len(portatiles_busqueda) == 1
    portatiles_busqueda = nueva_lista.buscar_portatil_por_precio(1000, 3000)
    assert len(portatiles_busqueda) == 2


def test_buscar_portatil_por_modelo_marca():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    indice4 = nueva_lista.agregarPortatil("MSI","GL62M","356X", 2033)
    portatiles_busqueda = nueva_lista.buscar_portatil_por_modelo_marca("B","A")
    assert len(portatiles_busqueda) == 0
    portatiles_busqueda = nueva_lista.buscar_portatil_por_modelo_marca("GL62M", "MSI")
    assert len(portatiles_busqueda) == 2

def test_comparar_portatiles():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    indice4 = nueva_lista.agregarPortatil("MSI","GL62M","356X", 1000)
    assert nueva_lista.comparar_portatiles("B","A") == False
    portatiles_comparar = nueva_lista.comparar_portatiles("GL62M", "MSI")
    assert len(portatiles_comparar) == 2
    portatil1 = {"_id":bson.ObjectId(indice4), "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"356X", "precio":1000, "pantalla":"", "procesador":"", "RAM":"", "almacenamiento":"", "grafica":"", "bateria":"", "SO":"",  "comentario":""}
    assert portatiles_comparar[0] == portatil1

def test_imprimir_comparacion():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    indice4 = nueva_lista.agregarPortatil("MSI","GL62M","356X", 999)
    indice5 = nueva_lista.agregarPortatil("MSI","GL62M","356X", 999)
    indice6 = nueva_lista.agregarPortatil("MSI","GL62M","356X", 999)
    indice7 = nueva_lista.agregarPortatil("MSI","GL62M","356X", 999)
    portatiles_comparar = nueva_lista.comparar_portatiles("GL62M", "MSI")
    nueva_lista.imprimir_comparacion(portatiles_comparar, "comparacion.pdf")

def test_buscar_portatil_por_modelo_marca_excluyendo_en_venta():
    nueva_lista.limpiar_lista()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333PRUEBAX",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333PRUEBAX",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333PRUEBAX",957)
    indice4 = nueva_lista.agregarPortatil("MSI","GL62M","333PRUEBAX", 2033)
    #En venta para que de 1 posteriormente
    nueva_lista.cambiar_stock_portatil(indice4,1)
    portatiles_busqueda = nueva_lista.buscar_portatil_por_modelo_marca("B","A")
    assert len(portatiles_busqueda) == 0
    portatiles_busqueda = nueva_lista.buscar_portatil_por_modelo_marca("GL62M", "MSI")
    assert len(portatiles_busqueda) == 1

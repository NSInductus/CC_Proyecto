import pytest
import sys
sys.path.append('src')

from Portatiles import Portatiles

def test_lista_portatiles_vacia():
    nueva_lista = Portatiles()
    assert nueva_lista.numeroPortatilesEnVenta() == 0
    assert nueva_lista.seleccionarPortatil(1) == False

def test_agregar_nuevo_portatil():
    nueva_lista = Portatiles()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    portatil = {"IDventa":indice, "marca":"MSI", "modelo":"GL62M", "DNIvendedor":"333X", "precio":2000}
    assert nueva_lista.seleccionarPortatil(indice) == portatil

def test_agregar_varios_portatiles():
    nueva_lista = Portatiles()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    indice4 = nueva_lista.agregarPortatil("MSI","GL62M","555X",2002)
    indice5 = nueva_lista.agregarPortatil("MSI","GL90","888X",1208)
    assert nueva_lista.numeroPortatilesEnVenta() == 5
    portatil1 = {"IDventa":indice1, "marca":"MSI","modelo":"GL62M","DNIvendedor":"333X","precio":2000}
    assert nueva_lista.seleccionarPortatil(indice1) == portatil1
    portatil2 = {"IDventa":indice2, "marca":"ASUN","modelo":"TUF","DNIvendedor":"333X","precio":1500}
    assert nueva_lista.seleccionarPortatil(indice2) == portatil2
    portatil3 = {"IDventa":indice3, "marca":"ACER","modelo":"Aspire 3","DNIvendedor":"333X","precio":957}
    assert nueva_lista.seleccionarPortatil(indice3) == portatil3
    portatil4 = {"IDventa":indice4, "marca":"MSI","modelo":"GL62M","DNIvendedor":"555X","precio":2002}
    assert nueva_lista.seleccionarPortatil(indice4) == portatil4
    portatil5 = {"IDventa":indice5, "marca":"MSI","modelo":"GL90","DNIvendedor":"888X","precio":1208}
    assert nueva_lista.seleccionarPortatil(indice5) == portatil5

def test_eliminar_portatil():
    nueva_lista = Portatiles()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    assert nueva_lista.indiceEnListaIDventa(indice) == 0
    assert nueva_lista.eliminarPortatilPorIdVenta(90) == False
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    assert nueva_lista.indiceEnListaIDventa(indice) == 0
    assert nueva_lista.eliminarPortatilPorIdVenta(indice) == True
    assert nueva_lista.numeroPortatilesEnVenta() == 0
    assert nueva_lista.indiceEnListaIDventa(indice) == False
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    assert nueva_lista.eliminarPortatilPorIdVenta(indice) == True
    assert nueva_lista.numeroPortatilesEnVenta() == 1

def test_modificar_portatil():
    nueva_lista = Portatiles()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    portatil = {"IDventa":indice, "marca":"MSI","modelo":"GL62M","DNIvendedor":"333X","precio":2000}
    assert nueva_lista.seleccionarPortatil(indice) == portatil
    assert nueva_lista.modificarPortatil(indice, 1500,"GL82M","MSI-PLUS") == True
    portatil_modificado = {"IDventa":indice, "marca":"MSI-PLUS","modelo":"GL82M","DNIvendedor":"333X","precio":1500}
    assert nueva_lista.seleccionarPortatil(indice) == portatil_modificado

def test_modificar_portatil_2():
    nueva_lista = Portatiles()
    indice = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    assert nueva_lista.numeroPortatilesEnVenta() == 1
    portatil = {"IDventa":indice, "marca":"MSI","modelo":"GL62M","DNIvendedor":"333X","precio":2000}
    assert nueva_lista.seleccionarPortatil(indice) == portatil
    assert nueva_lista.modificarPortatil(indice, 4000) == True
    portatil_modificado = {"IDventa":indice, "marca":"MSI","modelo":"GL62M","DNIvendedor":"333X","precio":4000}
    assert nueva_lista.seleccionarPortatil(indice) == portatil_modificado

def test_varias_pruebas_agregar_modificar_eliminar():
    nueva_lista = Portatiles()
    indice1 = nueva_lista.agregarPortatil("MSI","GL62M","333X",2000)
    indice2 = nueva_lista.agregarPortatil("ASUN","TUF","333X",1500)
    indice3 = nueva_lista.agregarPortatil("ACER","Aspire 3","333X",957)
    assert nueva_lista.numeroPortatilesEnVenta() == 3
    assert nueva_lista.eliminarPortatilPorIdVenta(indice2) == True
    assert nueva_lista.modificarPortatil(indice2) == False
    assert nueva_lista.modificarPortatil(indice1,400,"Modelo","Marca") == True
    portatil_modificado = {"IDventa":indice1, "marca":"Marca","modelo":"Modelo","DNIvendedor":"333X","precio":400}
    assert nueva_lista.seleccionarPortatil(indice1) == portatil_modificado
    assert nueva_lista.numeroPortatilesEnVenta() == 2
    assert nueva_lista.eliminarPortatilPorIdVenta(indice1) == True
    assert nueva_lista.eliminarPortatilPorIdVenta(indice3) == True
    assert nueva_lista.numeroPortatilesEnVenta() == 0

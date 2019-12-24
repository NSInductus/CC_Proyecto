import pytest
import sys
sys.path.append('src')

import Portatiles_rest

app = Portatiles_rest.app.test_client()

def test_prueba():
    respuesta = app.get('/')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_ruta_desconocida():
    respuesta = app.get('/kokoko')
    if (respuesta.status_code == 204):
        assert (respuesta.status_code == 204)

def test_rest_numero_portatiles():
    respuesta = app.get('/numeroPortatilesEnVenta')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)


def test_rest_seleccionar_portatil():
    respuesta = app.get('/seleccionarPortatil/1')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_agregar_portatil_version_corta():
    respuesta = app.get('/agregarPortatil/msi/gl62/333X/600')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_agregar_portatil_version_larga():
    respuesta = app.get('/agregarPortatil/msi/gl62/333X/600/Muy%20bueno/15/i7/GB%20DDR4/1gb/GTX/2H/Linux')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_modificar_portatil_solo_precio():
    respuesta = app.get('/modificarPortatil/1/800000')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_eliminar_portatil():
    respuesta = app.get('/eliminarPortatilPorIdVenta/1')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_buscar_portatil_dnivendedor():
    respuesta = app.get('/verPortatilesEnVentaDeUsuario/333X')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_buscar_portatil_precio():
    respuesta = app.get('/buscarPortatilPorPrecio/500/1000')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

def test_rest_busar_portatil_modelo_marca():
    respuesta = app.get('/buscarPortatilPorModeloMarca/gl62/msi')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)


def test_rest_comparar_portatiles():
    respuesta = app.get('/compararPotatiles/gl62/msi')
    if (respuesta.status_code == 200):
        assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    else:
        assert (respuesta.status_code == 412)

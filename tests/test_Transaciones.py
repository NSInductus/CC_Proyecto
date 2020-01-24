import pytest
import sys
import os

sys.path.append('src')

import bson

from Portatiles import Portatiles
from MongoDM import MongoDM

data_manager = MongoDM(os.environ['URI_ENVIRON'],'Nueva',os.environ['CO_ENVIRON'])
nueva_lista = Transaciones(data_manager)

def test_lista_transaciones_vacia():
    nueva_lista.limpiarLista()
    assert nueva_lista.numeroTransaciones() == 0
    assert nueva_lista.seleccionarTransacion("1") == False

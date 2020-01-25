from invoke import task, run
import sys
import os

#Instalacion de dependencias necesarias para el proyecto
@task
def install(c):
    c.run("pip3 install -r requirements.txt")
    print("La instalacion de dependencias necesarias para el proyecto concluida.")

#Ejecucion de test
@task
def test(c):
    os.environ['URI_ENVIRON'] = 'localhost:27017'
    os.environ['BD_ENVIRON'] = 'BDPruebaPortatiles'
    os.environ['CO_ENVIRON'] = 'COPortatiles'
    c.run("pytest -q tests/test_*.py")
    print("La ejecucion de tests concluida.")

#Ejecucion de test de covertura
@task
def coverage(c):
    os.environ['URI_ENVIRON'] = 'localhost:27017'
    os.environ['BD_ENVIRON'] = 'BDPruebaPortatiles'
    os.environ['CO_ENVIRON'] = 'COPortatiles'
    c.run("pytest --cov=src tests/")
    print("La ejecucion de tests de covertura concluida.")

#Iniciar el servidor
@task
def start(c, host="0.0.0.0", puerto="8080"):
    os.environ['URI_ENVIRON'] = 'localhost:27017'
    os.environ['BD_ENVIRON'] = 'BDPortatiles'
    os.environ['CO_ENVIRON'] = 'COPortatiles'
    sys.path.append('src')
    with c.cd('src/'):
        c.run("gunicorn -b " + host + ":" + puerto + " Portatiles_rest:app")

#Parar el servidor
@task
def stop(c):
    c.run("pkill gunicorn")

@task
def clear(c):
    c.run("rm -rf __pycache__")
    c.run("rm -rf .pytest_cache")
    c.run("rm -rf src/__pycache__/")
    c.run("rm -rf src/.pytest_cache/")
    c.run("rm -rf tests/__pycache__/")
    c.run("rm .coverage")
    c.run("rm comparacion.pdf")
    c.run("rm transaciones.pdf")

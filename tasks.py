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
    #os.environ['URI_BD_P'] = 'localhost:27017'
    #os.environ['BD_P'] = 'BDPruebaPortatiles'
    #os.environ['CO_P'] = 'COPruebaPortatiles'
    #os.environ['URI_BD_T'] = 'localhost:27017'
    #os.environ['BD_T'] = 'BDPruebaTransaciones'
    #os.environ['CO_T'] = 'COPruebaTransaciones'
    #os.environ['HOST'] = 'localhost'
    #os.environ['PORT'] = '8080'
    #os.environ['PORT_2'] = '8000'
    c.run("pytest -q tests/test_*.py")
    print("La ejecucion de tests concluida.")

#Ejecucion de test de covertura
@task
def coverage(c):
    #os.environ['URI_BD_P'] = 'localhost:27017'
    #os.environ['BD_P'] = 'BDPruebaPortatiles'
    #os.environ['CO_P'] = 'COPruebaPortatiles'
    #os.environ['URI_BD_T'] = 'localhost:27017'
    #os.environ['BD_T'] = 'BDPruebaTransaciones'
    #os.environ['CO_T'] = 'COPruebaTransaciones'
    #os.environ['HOST'] = 'localhost'
    #os.environ['PORT'] = '8080'
    #os.environ['PORT_2'] = '8000'
    c.run("pytest --cov=src tests/")
    print("La ejecucion de tests de covertura concluida.")

#Iniciar el servidor
@task
def start(c, host="0.0.0.0", micro= "", puerto="8080", puerto_2="8000"):
    #os.environ['URI_BD_P'] = 'localhost:27017'
    #os.environ['BD_P'] = 'BDPruebaPortatiles'
    #os.environ['CO_P'] = 'COPruebaPortatiles'
    #os.environ['URI_BD_T'] = 'localhost:27017'
    #os.environ['BD_T'] = 'BDPruebaTransaciones'
    #os.environ['CO_T'] = 'COPruebaTransaciones'
    #os.environ['HOST'] = 'localhost'
    #os.environ['PORT'] = '8080'
    #os.environ['PORT_2'] = '8000'
    #host = os.environ['HOST']
    #port = os.environ['PORT']
    #port2 = os.environ['PORT_2']
    sys.path.append('src')
    with c.cd('src/'):
        if micro == "":
            c.run("gunicorn -b " + host + ":" + puerto + " Portatiles_rest:app --daemon")
            c.run("gunicorn -b " + host + ":" + puerto_2 + " Transacciones_rest:app --daemon")
        elif micro == "Portatiles":
            c.run("gunicorn -b " + host + ":" + puerto + " Portatiles_rest:app")
        elif micro == "Transacciones":
            c.run("gunicorn -b " + host + ":" + puerto + " Transacciones_rest:app")

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
    c.run("rm transacciones.pdf")

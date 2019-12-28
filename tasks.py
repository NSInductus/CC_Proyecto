from invoke import task, run
import sys

#Instalacion de dependencias necesarias para el proyecto
@task
def install(c):
    c.run("pip3 install -r requirements.txt")
    print("La instalacion de dependencias necesarias para el proyecto concluida.")

#Ejecucion de test
@task
def test(c):
    c.run("pytest -q tests/test_*.py")
    print("La ejecucion de tests concluida.")

#Ejecucion de test de covertura
@task
def coverage(c):
    c.run("pytest --cov=src tests/")
    print("La ejecucion de tests de covertura concluida.")

#Iniciar el servidor
@task
def start(c, host="0.0.0.0", puerto="8080"):
    sys.path.append('src')
    c.run("gunicorn -b " + host + ":" + puerto + " Portatiles_rest:app")

#Parar el servidor
@task
def stop(c):
    c.run("pkill gunicorn")

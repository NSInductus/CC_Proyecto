from invoke import task, run

#Instalacion de dependencias necesarias para el proyecto
@task
def install():
    run("pip install -r requirements.txt")
    print("La instalacion de dependencias necesarias para el proyecto concluida.")

#Ejecucion de test
@task
def test():
    run("pytest -q tests/test_*.py")
    print("La ejecucion de tests concluida.")

#Ejecucion de test de covertura
@task
def coverage():
    run("pytest --cov=src tests/")
    print("La ejecucion de tests de covertura concluida.")

#Borrado de ficheros generados automaticamente
@task
def clean():
    run("rm tasks.pyc")
    run("rm ./src/Portatiles.pyc")
    run("rm .coverage")
    run("rm -r .pytest_cache")
    run("rm -r ./tests/__pycache__")
    run("rm .coverage")
    print("El borrado de ficheros generados automaticamente concluido.")

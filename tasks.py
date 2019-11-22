from invoke import task, run

#Instalacion de dependencias necesarias para el proyecto
@task
def install(c):
    c.run("pip install -r requirements.txt")
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

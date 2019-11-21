from invoke import task, run

#Instalación de dependencias necesarias para el proyecto
@task
def install(c):
    c.run("pip install -r requirements.txt")
    print("La instalación de dependencias necesarias para el proyecto concluida.")

#Ejecución de test
@task
def test(c):
    c.run("pytest -q tests/test_*.py")
    print("La ejecución de tests concluida.")

#Ejecución de test de covertura
@task
def coverage(c):
    c.run("pytest --cov=src tests/")
    print("La ejecución de tests de covertura concluida.")

#Borrado de ficheros generados automaticamente
@task
def clean(c):
    c.run(rm .coverade)
    c.run(rm -r .pytest_cache)
    c.run(rm -r ./tests/__pycache__)
    print("El borrado de ficheros generados automaaticamente concluido.")

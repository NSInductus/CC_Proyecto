# Proyecto de Cloud Computing

[![License: LGPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/NSInductus/CC_Proyecto.svg?branch=master)](https://travis-ci.com/NSInductus/CC_Proyecto)
[![CircleCI](https://circleci.com/gh/NSInductus/CC_Proyecto.svg?style=svg)](https://circleci.com/gh/NSInductus/CC_Proyecto)
[![codecov](https://codecov.io/gh/NSInductus/CC_Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/NSInductus/CC_Proyecto)
[![Heroku](https://www.herokucdn.com/deploy/button.svg)](https://cc-proyecto.herokuapp.com/)

Proyecto para desarrollar en la asignatura de **Cloud Computing** correspondiente al Máster de Ingeniería Informática.

## Descripción

El proyecto consistirá en un *bakc-end* para la compra/venta de portátiles. Para una Descripción más detallada del proyecto, ver [aquí](docs/descripcion.md).

## Más información sobre el proyecto

A continuación se muestra en forma de índice el acceso a más información referente al proyecto.

* [Tecnologías utilizadas](docs/tecnologias.md).
* [Historias de usuario](docs/historias_de_usuario.md).
* [Test](docs/test.md).
* [APIs REST](docs/apis_rest.md).
* [Docker](docs/docker.md)
* [Heroku](docs/heroku.md)
* [Licencia](docs/licencia.md).


## Arquitectura

La arquitectura será una arquitectura basada en microservicios. Para más información acerca de la arquitectura del proyecto, ver [aquí](docs/arquitectura.md).

### Arquitectura de los Microservicios

Los microservicios implementados o que se implementarán tendrán una arquitectura por capas, la cuál se basa en separar la funcionalidad del microservicio en diferentes capas, con el fin de seguir los principios de: *abstracción, encapsulamiento, funcionalidad, alta cohesión, reutilizable y desacople.*

Para información más concreta acerca de la arquitectura de cada microservicio, ver [aquí](docs/arquitectura_microservicios.md).


## Herramienta de construcción

Como herramienta de construcción se utilizará **invoke**, por su madurez y fiabilidad frente a otras herramientas , así como por su detallada y clara documentación que permiten al usuario saber como tiene que utilizar invoke en cada momento.

Para poder utilizarla hay que instalarla en python, para eso se escribe en la terminal el siguiente comando:

```shell
$ pip install invoke
```

Para la configuración de la misma, se ha agregado el fichero [tasks.py](https://github.com/NSInductus/CC_Proyecto/blob/master/tasks.py).


```
buildtool: tasks.py
```

Para utilizar la herramienta de construcción se ha de escribir en la terminal "invoke" seguido de la tarea que se desea que realice la herramienta. Estas tareas se han definido anteriormente en el fichero de configuración de la herramienta.

Las posibles tareas que se pueden hacer son:

* **install**: Esta tarea es la encargada de instalar las dependencias necesarias para que funcione nuestro proyecto, las cuales están definidas en el fichero [requirements.txt](https://github.com/NSInductus/CC_Proyecto/blob/master/requirements.txt). Para esto hay que escribir en la terminal:
```
$ invoke install
```

* **test**: Esta tarea es la encargada de ejecutar los test unitarios, sobre nuestras clases de python. Para esto hay que escribir en la terminal:
```
$ invoke test
```

* **coverage**: Esta tarea es la encargada de ejecutar los test de cobertura, sobre nuestras clases de python. Para esto hay que escribir en la terminal:
```
$ invoke coverage
```

* **start**: Esta tarea es la encargada de levantar el microservicios utilizando gunicorn. En esta tarea se pueden utilizar varios argumentos opcionales para modificar el host y los diferentes puertos donde se ejecutarán los microservicios, por defecto el host será *0.0.0.0* , el puerto será *8080* y el puerto_2 será *8000*.
Hay varias opciones:
* No introducir el argumento micro, por lo que lanzará los dos microservicios, Portatiles en el puerto y Transacciones en el puerto_2
* Introducir *Portatiles* en el argumento micro, y solo se lanzará el microservicio Portatiles.
* Introducir *Transacciones* en el argumento micro, y solo se lanzará el microservicio Transacciones.

```
$ invoke start [-h/--host <host>] [-m/--micro <puerto>] [--puerto <puerto>] [--puerto_2 <puerto_2>]
```

* **stop**: Esta tarea es la encargada de detener el microservicio lanzado anteriormente con la tarea: *start*.
```
$ invoke stop
```
* **clear**: Esta tarea es la encargada de eliminar todos los ficheros innecesarios que se generan en los test y en los test de covertura.
```
$ invoke clear
```

## Integración continua

Como herramientas para la integración continua se ha utilizado: **TravisCi** & **CircleCI**. Para más información acerca de la integración continua, ver [aquí](docs/integracion_continua.md).



## Almacén de datos

Confirmando lo expuesto en la sección de tecnologías, se ha utilizado **MongoDB** como base de datos para nuestro proyecto, las
razones son las siguientes:

* Realiza muchas operaciones por segundo, siendo mucho más rápida que una base de datos relacional.
* Capaz de almacenar grandes cantidades de datos sin inconveniente.
* Es variable en el sentido de que no fuerza que todos los registros de una colección se guarden con los mismos atributos.


También apuntar que las manipulaciones sobre la base de datos se realizarán concretamente con la librería *pymongo*, que cuenta con una serie de funciones que realizan las operaciones básicas (aunque también más avanzadas) que cualquier tipo de base de datos tiene como búsqueda, inserción, eliminación o actualización de elementos

Se ha utilizado MongoDB de dos formas diferentes:

* De forma **local**

* De forma **Remoto**


*Destacar que hay una base de datos por microservicio.*

### De forma local

Para poder utilizar MongoDB en local, es decir, desde tu máquina, es necesario instalar mongo, en nuestro caso, se ha instalado la versión *3.6.8*. Para eso se ha introducido en terminal el siguiente comando:

```

sudo apt-get install mongo==3.6.8

```


De este modo ya se pueden utilizar bases de datos de mongoDB de forma local, si introducimos el siguiente comando en terminal:

```

mongo

```

Se puede ver en la siguiente captura de pantalla:

![](docs/img/terminal_mongo.png)

Se acede a la administración de la base de datos a través de la misma terminal donde podremos ver las bases de datos disponibles, sus colecciones internas (lo que en una base de datos SQL serían tablas), insertar, modificar o eliminar datos, entre otras funcionalidades. En la siguiente captura de pantalla se puede ver:



### En remoto

Para utilizar MongoBD de forma remota, se valoraron varias opciones, para finalmente acabar quedándonos con **MongoAtlas**, por los siguientes motivos:

* Tiene opciones gratuitas.
* Cuenta con automatización, de tal forma que el usuario puede programar actividades sobre la base de datos MongoDB en la nube.
* Tiene un buen rendimiento.


Una vez seleccionada esta tecnología, nos dirigimos al dominio web de MongoAtlas, el cual es el siguiente: dominio

El primer paso a realizar en esta web es registrarnos (se puede realizar de forma muy rápida usando la cuenta de *gmail*). Seguidamente tendremos que seleccionar un plan, se escogerá el plan gratuito:

![](docs/img/seleccionar_cluster.png)

Posteriormente debemos de crear un cluster, para ello seleccionamos como base uno de los gratuitos proporcionados por el dominio web. En la siguiente captura de pantalla se puede ver que se ha seleccionado *Cloud* y la región *belga* que son totalmente gratuitas:

![](docs/img/provedor_region.png)

Posteriormente el usuario selecciona la opción de *Crear base de datos*, para allí crear la base de datos tan solo introduciendo el nombre de la misma, así como la colección (es lo que sería una tabla en una base de datos SQL), se puede ver en la siguiente imagen:

![](docs/img/crear_bd.png)

Por ultimo se ha conseguido ver como se conecta la base de datos con cualquier aplicación para utilizarla, es a través de una ruta proporcionada que sustituirá a nuestro *URI*, es decir, a nuestra ruta base. En la siguiente captura de pantalla se puede observar:


![](docs/img/conectar_atlas.png)






## Data Manager: MongoDM.py


Para la incrustación de la base de datos de MongoDB a los microservicios implementados se ha utilizado como anteriormente he mencionado la librería **pymongo**.

Utilizando la librería anteriormente comentada se ha creado el fichero MongoDM.py, el cuáĺ es mi *data manager* (o *controlador de datos*), el cual implementa una serie de funciones definidas por mi que utilizan las funciones proporcionadas por pytest, estas funciones son:

* **obtener_elemento:** se encarga de introducir un elemento en la colección de la base de datos.
* **obtener_conjunto_elementos:** se encarga de obtener un conjunto de elementos de la colección de la base de datos que cumplan una determinada característica.
* **obtener_todos_elementos:** se encarga de obtener todos los elementos existentes en la colección de la base de datos.
* **insertar_elemento:** se encarga de insertar un elemento en la colección de la base de datos.
* **actualizar_elemento:** se encarga de actualizar un elemento que ya exista en la colección de la base de datos.
* **borrar_elemento:** se encarga de borrar un elemento existente en la colección de nuestra base de datos.
* **numero_elementos:** se encarga de proporcionar el numero de elementos existentes en la colección de la base de datos.
* **borrar_conjunto:** se encarga de borrar todos los elementos existentes en la colección de la base de datos.

Esta fichero será incrustado a los diferentes microservicios a través de la técnica de la inyección de dependencias, que se explicará con más detalle en otra apartado, concretamente en [este](docs/inyeccion_de_dependencias.md).

### Modificaciones en otros ficheros

Se han tenido que realizar una serie de modificaciones sobre algunos ficheros para adaptarlos a la incorporación del data_manager (MongoDM.py).

1. En primer lugar se han tenido que modificar los ficheros correspondientes al primer microservicio que se había implementado anteriormente, es decir, el microservicio de Portatiles. Porque este trabajaba con una lista interna, que se ha sustituido por un data_manager al cuál se le introduce el data_manager que se ha creado anteriormente, es decir, MongoDM.py.
Pero tenido en cuenta que se puede cambiar en cualquier momento, si se decide cambiar la base de datos, teniendo solo que cambiar el fichero data_manager. Destacar que hay que cambiar tanto los ficheros de código propiamente dicho, es decir, Portatiles.py y Portatiles_rest.py, como los ficheros de test (aunque los cambios sean más insignificativos comparados con los de los ficheros anteriores), es decir, test_Portatiles.py y test_Portatiles_rest.py.

2. En segundo lugar, los sistemas de integración continua se ha tenido que realizar los siguientes cambios:

* *En TravisCi:* Se ha añadido las variables de entorno y se ha agregado de servicio, el servicio de mongoDB.

* *En CircleCi:* Se ha agregago las variables de entorno y se ha agregado una imagen de docke.

3. En tercer lugar, se ha creado un Dockerfile nuevo, así como se ha creado una nueva regla, se puede ver con más detalle [aquí](docs/docker.md).




*Destacar que en las nuevas clases implementadas, ya se tiene en cuenta que utilicen el data_manager desde el primer momento*



## Estudio de prestaciones

Prestaciones: performance_test.yml

Las prestaciones se han evaluado usando **Taurus**. Se han realizado varias pruebas:

1. Prueba de prestaciones **sobre el microservicio Portatiles**.
2. Prueba de prestaciones **sobre el microservicio Transaciones**, utilizando solo rutas que no interactúan sobre el otro microservicio.
3. Prueba de prestaciones sobre el microservicio Transaciones, utilizando entre las rutas una que envía peticiones al otro microservicio (Portatiles), es decir, es una prueba conjunta **sobre los dos microservicios**.


Toda esta batería de pruebas se han realizado en varias circunstancias:
* En local utilizando una base de datos mongoDB de forma local
* En local utilizando una base de datos mongoDB de forma remota, concretamente utilizando MongoAtlas.


Las pruebas de prestaciones debían de superar o igualar *1000 peticiones por segundo* utilizando 10 usuarios concurrentes sin tener ningún error durante el proceso.

El código del fichero donde se definen las pruebas se comentará a continuación:



```
# EVALUACION DE PRESTACIONES CON TAURUS
execution:
    - concurrency: 10   
      ramp-up: 10s      
      hold-for: 50s     
      scenario: portatiles-test   #

```

En primer lugar se definen:
* **concurrency:** número de hilos que participarán de forma simultánea.
* **ramp-up:** tiempo en segundos que tardará en llegar a los hilos definidos anteriormente .
* **hold-for:** tiempo que se mantienen los hilos.
* **scenario:** escenario a ejecutar en el test entre los posibles.

```
#Posibles escenarios
scenarios

    portatiles-test:
        requests:
        - once:
          - url: http://localhost:8080/portatiles/agregarPortatil/msi/gl62/333X/2500
            method: POST
        - url: http://localhost:8080/portatiles/seleccionarPortatil/5e2cfeefd46dbb22740a0d96
          method: GET
        - url: http://localhost:8080/portatiles/seleccionarPortatil/wqwqdqwfqfefewq
          method: GET
        - once:
          - url: http://localhost:8080/portatiles/eliminarPortatilPorIdVenta/5e2cff09d46dbb22740a0d97
            method: DELETE

```

Primero de los escenarios (portatiles-test) que tiene las siguientes peticiones:

* Una petición *POST* que agrega un portátil a la base de datos, esta al estar dentro de *once* solo se ejecutará una vez por hebra.
* Una petición *GET* para seleccionar un determinado portátil que existe en la base de datos.
* Una petición *GET* que intentar seleccionar otro portatil de la base de datos pero en esta ocasión no lo encontrará, puesto que no eciste.
* Una petición *DELETE* que elimina un portátil de la base de datos, al igual que la primera petición esta también se ejecuta solo una vez por hebra, el portátil que intenta borrar existe y por lo tanto podrá borrarlo la primera vez que lo intente, después ya no existirá.


```
transacciones-test:
    requests:

    - url: http://localhost:8000/transacciones/
      method: GET
    - once:
      - url: http://localhost:8000/transacciones/verEstadisticas/339X
        method: GET

```

Segundo de los escenarios (transacciones-test) que tiene las siguientes peticiones:

* Una petición *GET* que simplemente es la petición de bienvenida de este microservicio
* Una petición *GET* que recoge todas las estadisticas de un usuario, es decir, todas sus transaciones para ello las cogerá todas y se quedará con las del usuario, como la base de datos esta bastante llena solo se realizará este proceso una vez por hebra.


```
combinada-test:
    requests:

    - url: http://localhost:8000/transacciones/
      method: GET
    - url: http://localhost:8000/transacciones/devolverPortatil/5e2d0c1baa15ba4dcb7f8176/333X
      method: POST

```

Tercer de los escenarios (combinada-test) que tiene las siguientes peticiones:

* Una petición *GET* que simplemente es la petición de bienvenida de este microservicio
* Una petición *POST* que mete una transacción en la base de datos y además con el mismo id del portátil, se dirige ha realizar un *PUT* en el otro microservicio, el cual consiste en cambiar el atributo *vendido* del portátil que coincida con el id proporcionado por el otro microservicio.

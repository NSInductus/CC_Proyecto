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
* Es variable en el sentido de que no fuerza que todos los registros de una collección se guarden con los mismos atributos.


También apuntar que las manipulaciones sobre la base de datos se realizarán concretamente con la librería *pymongo*, que cuenta con una serie de funciones que realizan las operaciones básicas (aunque también más avanzadas) que cualquier tipo de base de datos tiene como búsqueda, inserción, eliminación o actualización de elementos

Se ha utilizado MongoDB de dos formas diferentes:

* De forma **local**

* De forma **Remoto**


*Destacar que hay una base de datos por microservicio.*

### De forma local

Para poder utilizar MongoDB en local, es decir, desde tu máquina, es necesario instalar mongo, en nuestro caso, se ha instalado la versión *x.x.x*. Para eso se ha introducido en terminal el siguiente comando:

```

sudo apt-get install mongo==3.6.8

```


De este modo ya se pueden utilizar bases de datos de mongoDB de forma local, si introducimos el siguiente comando en terminal:

```

mongo

```

Se acede a la administración de la base de datos a través de la misma terminal donde podremos ver las bases de datos disponibles, sus colecciones internas (lo que en una base de datos SQL serían tablas), insertar, modificar o eliminar datos, entre otras funcionalidades. En la siguiente captura de pantalla se puede ver:

imagen


### En remoto

Para utilizar MongoBD de forma remota, se valoraron varias opciones, para finalmente acabar quedándonos con **MongoAtlas**, por los siguientes motivos:

* Tiene opciones gratuitas.
* Cuenta con automatización, de tal forma que el usuario puede programar actividades sobre la base de datos MongoDB en la nube.
* Tiene un buen rendimiento.


Una vez seleccionada esta tecnología, nos dirigimos al dominio web de MongoAtlas, el cual es el siguiente: dominio

El primer paso a realizar en esta web es registrarnos (se puede realizar de forma muy rápida usando la cuenta de *gmail*).

imagen

Posteriormente debemos de crear un cluster, para ello seleccionamos como base uno de los gratuitos proporcionados por el dominio web. En la siguiente captura de pantalla se puede ver que se ha seleccionado la x *Cloud* y la región *belga* que son totalmente gratuitas:

imagen

Posteriormente el usuario selecciona la opción de *Crear base de datos*, para allí crear la base de datos tan solo introduciendo el nombre de la misma, así como la colección (es lo que sería una tabla en una base de datos SQL), se puede ver en la siguiente imagen:

imagen

Por ultimo se ha conseguido ver como se conecta la base de datos con cualquier aplicación para utilizarla, es a través de una ruta proporcionada que sustituirá a nuestro *URI*, es decir, a nuestra ruta base. En la siguiente captura de pantalla se puede observar:


imagen






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

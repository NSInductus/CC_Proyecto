# Proyecto de Cloud Computing

[![License: LGPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/NSInductus/CC_Proyecto.svg?branch=master)](https://travis-ci.com/NSInductus/CC_Proyecto)
[![CircleCI](https://circleci.com/gh/NSInductus/CC_Proyecto.svg?style=svg)](https://circleci.com/gh/NSInductus/CC_Proyecto)
[![codecov](https://codecov.io/gh/NSInductus/CC_Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/NSInductus/CC_Proyecto)
[![Heroku](https://www.herokucdn.com/deploy/button.svg)](https://cc-proyecto.herokuapp.com/portatiles/)

Proyecto para desarrollar en la asignatura de **Cloud Computing** correspondiente al Máster de Ingeniería Informática.

## Descripción

El proyecto consistirá en un *back-end* para la compra/venta de portátiles. Para una Descripción más detallada del proyecto, ver [aquí](docs/descripcion.md).

## Más información sobre el proyecto

A continuación se muestra en forma de índice el acceso a más información referente al proyecto.

* [Tecnologías utilizadas](docs/tecnologias.md).
* [Historias de usuario](docs/historias_de_usuario.md).
* [Arquitectura](docs/arquitectura.md).
* [Test](docs/test.md).
* [APIs REST](docs/apis_rest.md).
* [Integración continua](docs/integracion_continua.md).
* [Herramienta de construccion](docs/herramienta_de_construccion.md).
* [Docker](docs/docker.md).
* [Heroku](docs/heroku.md).
* [Licencia](docs/licencia.md).

## Herramienta de construcción

```
buildtool: tasks.py
```

Para más información, ver [aquí](docs/herramienta_de_construccion.md).

## Docker

Contenedor: https://hub.docker.com/repository/docker/nsinductus/cc_proyecto

Para más información, ver [aquí](docs/docker.md).

# Hito 4 Reenvío

## Creación de nuevo microservicio: Transacciones

Se ha implementado el nuevo microservicio: Transacciones, su API REST, así como sus respectivos tests para comprobar su correcto funcionamiento.

Tanto la [API REST](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Transacciones_rest.py) como los tests: [test del microservicio](https://github.com/NSInductus/CC_Proyecto/blob/master/tests/test_Transacciones.py) y [test de la API REST](https://github.com/NSInductus/CC_Proyecto/blob/master/tests/test_Transacciones_rest.py) se han realizado con las mismas tecnologías que se utilizaron para el primer microservicio, es decir, flask para la API REST y pytest para los tests.

Este microservicio se encarga de las transacciones necesarias del servicio, en estas transacciones se registrarán compras y devoluciones de ordenadores portátiles. También se encargará de mostrar las estadísticas de las transacciones que realicen los usuarios.

### Arquitectura del microservicio: Transacciones

* **Primera capa:** la primera capa de este microservicio contiene la API REST, es decir, el archivo [Transacciones_rest.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Transacciones_rest.py), este contendrá las rutas que se utilizarán para utilizar el mic
* **Segunda capa:**  la segunda capa de este microservicio se encarga de administrar la lógica del microservicio, esta contiene el archivo [Transacciones.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Transacciones.py), el cuál está repleto de funciones que son de utilidad para poder cumplir con las historias de usuario.

* **Tercera capa:** la tercera capa de este microservicio se encarga de administrar la base de datos donde se guardan y administran todas las transacciones, esta capa contiene el archivo [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py) (se explicará posteriormente).

La Arquitectura de este servicio se puede comprender fácilmente observando la siguiente imagen:

![](docs/img/a_capas_transacciones.png)

## Almacén de datos

Confirmando lo expuesto en la sección de tecnologías, se ha utilizado **MongoDB** como base de datos para nuestro proyecto, las
razones son las siguientes:

* Realiza muchas operaciones por segundo, siendo mucho más rápida que una base de datos relacional.
* Capaz de almacenar grandes cantidades de datos sin inconveniente.
* Es variable en el sentido de que no fuerza que todos los registros de una colección se guarden con los mismos atributos.

También apuntar que las manipulaciones sobre la base de datos se realizarán concretamente con la librería *pymongo*, que cuenta con una serie de funciones que realizan las operaciones básicas (aunque también más avanzadas) que cualquier tipo de base de datos tiene como búsqueda, inserción, eliminación o actualización de elementos.

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

Se acede a la administración de la base de datos a través de la misma terminal donde podremos ver las bases de datos disponibles, sus colecciones internas (lo que en una base de datos SQL serían tablas), insertar, modificar o eliminar datos, entre otras funcionalidades.

### En remoto

Para utilizar MongoBD de forma remota, se valoraron varias opciones, para finalmente acabar quedándonos con **MongoAtlas**, por los siguientes motivos:

* Tiene opciones gratuitas.
* Cuenta con automatización, de tal forma que el usuario puede programar actividades sobre la base de datos MongoDB en la nube.
* Tiene un buen rendimiento.

Una vez seleccionada esta tecnología, nos dirigimos al dominio web de MongoAtlas, el cual es el siguiente: [dominio](https://www.mongodb.com/cloud/atlas).

El primer paso a realizar en esta web es registrarnos (se puede realizar de forma muy rápida usando la cuenta de *gmail*). Seguidamente tendremos que seleccionar un plan, se escogerá el plan gratuito:

![](docs/img/seleccionar_cluster.png)

Posteriormente debemos de crear un cluster, para ello seleccionamos como base uno de los gratuitos proporcionados por el dominio web. En la siguiente captura de pantalla se puede ver que se ha seleccionado *Cloud* y la región *belga* que son totalmente gratuitas:

![](docs/img/provedor_region.png)

Posteriormente el usuario selecciona la opción de *Crear base de datos*, para allí crear la base de datos tan solo introduciendo el nombre de la misma, así como el nombre de la colección (es lo que sería una tabla en una base de datos SQL), se puede ver en la siguiente imagen:

![](docs/img/crear_bd.png)

Por ultimo se ha conseguido ver como se conecta la base de datos con cualquier aplicación para utilizarla, es a través de una ruta proporcionada que sustituirá a nuestro *URI*, es decir, a nuestra ruta base. En la siguiente captura de pantalla se puede observar:

![](docs/img/conectar_atlas.png)

*Destacar que en nuestro proyecto para cambiar entre usar MongoDB en local o en remoto es suficiente con modificar las variables de entorno, para más información acerca de estas, clicar [aqui](docs/variables_de_entorno.md)*.

## Data Manager: MongoDM.py

Para la incrustación de la base de datos de MongoDB a los microservicios implementados se ha utilizado como anteriormente he mencionado la librería **pymongo**.

Utilizando la librería anteriormente comentada se ha creado el fichero [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py), el cual es mi *data manager* (o *controlador de datos*), el cual implementa una serie de funciones definidas por mi que utilizan las funciones proporcionadas por pytest, estas funciones son:

* **obtener_elemento:** se encarga de introducir un elemento en la colección de la base de datos.
* **obtener_conjunto_elementos:** se encarga de obtener un conjunto de elementos de la colección de la base de datos que cumplan una determinada característica.
* **obtener_todos_elementos:** se encarga de obtener todos los elementos existentes en la colección de la base de datos.
* **insertar_elemento:** se encarga de insertar un elemento en la colección de la base de datos.
* **actualizar_elemento:** se encarga de actualizar un elemento que ya exista en la colección de la base de datos.
* **borrar_elemento:** se encarga de borrar un elemento existente en la colección de nuestra base de datos.
* **numero_elementos:** se encarga de proporcionar el numero de elementos existentes en la colección de la base de datos.
* **borrar_conjunto:** se encarga de borrar todos los elementos existentes en la colección de la base de datos.

Para utilizar este Data Manager se recurrirá a la técnica de la inyección de dependencias.

### Inyección de dependencias

Como se ha comentado anteriormente se ha utilizado la técnica de la *inyección de dependencias* para conseguir que los microservicios de nuestro proyecto utilicen de forma abstracta la base de datos, para ello se ha creado la clase [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py).

Para la inyección de esta clase, se importará en los ficheros que implementan la lógica de negocio de cada uno de los microservicos, es decir, [Portatiles.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Portatiles.py) y [Transacciones.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Transacciones.py), para posteriormente crear un objeto de la clase [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py). Los campos existentes en el constructor de la clase son:

* **uri:** Este parámetro contiene la dirección base, de la base de datos, en el caso de que se este lanzando en local tendremos que poner: *localhost:5000*. Como se ha podido ver: el formato de esta dirección base es el siguiente: *host:puerto*
* **basedatos:** Este parámetro contiene el nombre de la base de datos con la que se trabajará.
* **coleccion:** Esta parámetro contiene el nombre de la colección con la que se trabajará.

*Para la introducción de estos parámetros se utilizarán variables de entorno, para más información acerca de éstas, clicar [aqui](docs/variables_de_entorno.md).*

El *objetivo o fin* de este proceso es que la lógica de negocio de un microservicio y la base de datos sean totalmente independientes, de tal forma que si en el futuro se desea cambiar de base de datos tan solo sea necesario cambiar el *Data Manager*.

De tal forma que la *API REST* realizará llamadas a las funciones de la lógica de negocio del microservicio y esta utilizará el *Data Manager* para gestionar los datos. Cumpliendo con la arquitectura por capas, la cual es la arquitectura que poseen todos mis microservicios implementados.

### Modificaciones en otros ficheros

Se han tenido que realizar una serie de modificaciones sobre algunos ficheros para adaptarlos a la incorporación del *Data Manager*, es decir, del fichero [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py).

1. En primer lugar, se han tenido que modificar los ficheros correspondientes al primer microservicio que se había implementado anteriormente, es decir, el microservicio de Portatiles. Porque éste trabajaba con una lista interna, que se ha sustituido por un data_manager, por eso al constructor de esta clase se le introduce un objeto que actuará como data_manager, en este caso, un objeto de tipo MongoDM.
Destacar que hay que cambiar tanto los ficheros de código propiamente dicho, es decir, [Portatiles.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Portatiles.py) y [Portatiles_rest.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Portatiles_rest.py), como los ficheros de test (aunque los cambios sean más insignificativos comparados con los de los ficheros anteriores), es decir, [test_Portatiles.py](https://github.com/NSInductus/CC_Proyecto/blob/master/test/test_Portatiles.py) y [test_Portatiles_rest.py](https://github.com/NSInductus/CC_Proyecto/blob/master/test/test_Portatiles_rest.py).

2. En segundo lugar, los sistemas de integración continua se ha tenido que realizar los siguientes cambios:

  * *En TravisCi:* Se ha añadido las variables de entorno y se ha agregado de servicio, el servicio de mongoDB.

  * *En CircleCi:* Se ha agregago las variables de entorno y se ha agregado una imagen de docker (correspondiente a MongoDB).

3. En tercer lugar, se ha creado un Dockerfile nuevo, así como se ha creado una nueva regla de construcción automática, se puede ver con más detalle [aquí](docs/docker.md).

*Destacar que en el nuevo microservicio implementado, ya se tiene en cuenta que se utilice el Data Manager desde el primer momento.*

## Estudio de prestaciones

Prestaciones: performance_test.yml

Las prestaciones se han evaluado usando **Taurus**. Se han realizado sobre varios escenarios:

1. Prueba de prestaciones **sobre el microservicio Portatiles**.
2. Prueba de prestaciones **sobre el microservicio Transaciones**.

Estos diferentes escenarios se han probado con dos tipos de bases de datos:

* Una base de datos mongoDB de forma local.
* Una base de datos mongoDB de forma remota, concretamente utilizando MongoAtlas.

Estos diferentes escenarios se han probado levantando el servicio de formas diferentes:

* De forma local, utilizando *gunicorn* con 1 worker.
* De forma local, utilizando *gunicorn* con 2 worker.
* De forma local, utilizando *gunicorn* con 8 worker.
* Levantando un Contenedor(*Docker*).

Mezclando las diferentes posibilidades conseguimos realizar 8 pruebas de prestaciones por microservicio.

Las pruebas de prestaciones debían de superar o igualar *1000 peticiones por segundo* utilizando 10 usuarios concurrentes sin tener ningún error durante el proceso.

El código del fichero donde se definen las pruebas se comentará a continuación:

```
# EVALUACION DE PRESTACIONES CON TAURUS
execution:
    - concurrency: 10   
      ramp-up: 10s      
      hold-for: 50s     
      scenario: portatiles-test  

```
En primer lugar se definen:
* **concurrency:** número de usuarios que participarán de forma simultánea.
* **ramp-up:** tiempo en segundos que tardará en llegar a los usuarios definidos anteriormente .
* **hold-for:** tiempo que se mantienen los usuarios.
* **scenario:** escenario a ejecutar en el test entre los posibles.

```
#Posibles escenarios
scenarios:
    #Escenario microservicio PORTATILES
    portatiles-test:
      requests:
      #Prueba basica: REST DE TRANSACIONES
      - url: http://localhost:8080/portatiles/
        method: GET
      #Numero de portatiles en la BD
      - url: http://localhost:8080/portatiles/numeroPortatilesEnBD
        method: GET
      #Seleccionar un portatil en concreto
      - url: http://localhost:8080/portatiles/seleccionarPortatil/5e2cfeefd46dbb220a0d96
        method: GET
      #Ver portatiles que vende un usuario
      - url: http://localhost:8080/portatiles/verPortatilesEnVentaDeUsuario/358D
        method: GET
```

**El primer escenario: (portatiles-test)**, tiene las siguientes peticiones:

* Una petición *GET* que simplemente es la petición de bienvenida de este microservicio.
* Una petición *GET* para comprobar el numero de portatiles que existen en la base de datos.
* Una petición *GET* que selecciona un determinado portatil de la base de datos con un identificador en concreto.
* Una petición *GET* para encontrar los diferentes portátiles que tiene en venta un usuario, buscando por el DNI del usuario.

```
    #Escenario microservicio TRANSACCIONES
    transacciones-test:
        requests:
        #Prueba basica: REST DE TRANSACIONES
        - url: http://localhost:8000/transacciones/
          method: GET
        #Algun portatil en la base de datos con ese usuario introducido
        - url: http://localhost:8000/transacciones/verEstadisticas/339X
          method: GET
          
```
**El segundo escenario: transacciones-test**, tiene las siguientes peticiones:

* Una petición *GET* que simplemente es la petición de bienvenida de este microservicio
* Una petición *GET* que recoge todas las estadisticas de un usuario, es decir, todas sus transacciones, para ello las cogerá todas y se quedará con las del usuario.

Una vez creado este fichero para ejecutarlo hay que poner en terminal el siguiente comando:

```
$ bzt performance_test.yml -report
```

### Resultados de prestaciones

Para comenzar se levantó el servicio en local utilizando *gunicorn* con 1 solo worker, los resultados se pueden ver a continuación:

* Primer escenario, utilizando 1 Worker y MongoDB de forma local:

![](docs/img/taurus/portatiles/1wk/1wk-local-terminal.png)
![](docs/img/taurus/portatiles/1wk/1wk-local-final.png)

En esta prueba se consiguen **1387.9 peticiones por segundo**, teniendo un tiempo de respuesta medio de 6ms.

* Segundo escenario, utilizando 1 Worker y MongoDB de forma local:

![](docs/img/taurus/transacciones/1wk/1wk-local-terminal.png)
![](docs/img/taurus/transacciones/1wk/1wk-local-final.png)

En esta prueba se consiguen **1570.8 peticiones por segundo**, teniendo un tiempo de respuesta medio de 8ms.

* Primer escenario, utilizando 1 Worker y una BD remota (MongoAtlas):

![](docs/img/taurus/portatiles/1wk/1wk-remoto-terminal.png)
![](docs/img/taurus/portatiles/1wk/1wk-remoto-final.png)

En esta prueba se consiguen **66.24 peticiones por segundo**, teniendo un tiempo de respuesta medio de 141ms. Por lo que en estas condiciones no se supera el mínimo de peticiones (1000).

* Segundo escenario, utilizando 1 Worker y una BD remota (MongoAtlas):

![](docs/img/taurus/transacciones/1wk/1wk-remoto-terminal.png)
![](docs/img/taurus/transacciones/1wk/1wk-remoto-final.png)

En esta prueba se consiguen **64.62 peticiones por segundo**, teniendo un tiempo de respuesta medio de 142ms. Por lo que en estas condiciones no se supera el mínimo de peticiones (1000).

A continuación se subió el número de workers a 2, los resultados se pueden ver a continuación:

* Primer escenario, utilizando 2 Worker y MongoDB de forma local:

![](docs/img/taurus/portatiles/2wk/2wk-local-terminal.png)
![](docs/img/taurus/portatiles/2wk/2wk-local-final.png)

En esta prueba se consiguen **2134.23 peticiones por segundo**, teniendo un tiempo de respuesta medio de 4ms.

* Segundo escenario, utilizando 2 Worker y MongoDB de forma local:

![](docs/img/taurus/transacciones/2wk/2wk-local-terminal.png)
![](docs/img/taurus/transacciones/2wk/2wk-local-final.png)

En esta prueba se consiguen **1661.38 peticiones por segundo**, teniendo un tiempo de respuesta medio de 5ms.

* Primer escenario, utilizando 2 Worker y una BD remota (MongoAtlas):

![](docs/img/taurus/portatiles/2wk/2wk-remoto-terminal.png)
![](docs/img/taurus/portatiles/2wk/2wk-remoto-final.png)

En esta prueba se consiguen **130.07 peticiones por segundo**, teniendo un tiempo de respuesta medio de 70ms.

* Segundo escenario, utilizando 2 Worker y una BD remota (MongoAtlas):

![](docs/img/taurus/transacciones/2wk/2wk-remoto-terminal.png)
![](docs/img/taurus/transacciones/2wk/2wk-remoto-final.png)

En esta prueba se consiguen **131.42 peticiones por segundo**, teniendo un tiempo de respuesta medio de 71ms. Por lo que en estas condiciones no se supera el mínimo de peticiones (1000).

A continuación se subió el número de workers a 8 (cercano al número máximo de workers que puede soportar mi ordenador), los resultados se pueden ver a continuación:

* Primer escenario, utilizando 8 Worker y MongoDB de forma local:

![](docs/img/taurus/portatiles/8wk/8wk-local-terminal.png)
![](docs/img/taurus/portatiles/8wk/8wk-local-final.png)

En esta prueba se consiguen **2763.8 peticiones por segundo**, teniendo un tiempo de respuesta medio de 3ms.

* Segundo escenario, utilizando 8 Worker y MongoDB de forma local:

![](docs/img/taurus/transacciones/8wk/8wk-local-terminal.png)
![](docs/img/taurus/transacciones/8wk/8wk-local-final.png)

En esta prueba se consiguen **2399.85 peticiones por segundo**, teniendo un tiempo de respuesta medio de 3ms.

* Primer escenario, utilizando 8 Worker y una BD remota (MongoAtlas):

![](docs/img/taurus/portatiles/8wk/8wk-remoto-terminal.png)
![](docs/img/taurus/portatiles/8wk/8wk-remoto-final.png)

En esta prueba se consiguen **198.64 peticiones por segundo**, teniendo un tiempo de respuesta medio de 47ms. Por lo que en estas condiciones no se supera el mínimo de peticiones (1000).

* Segundo escenario, utilizando 8 Worker y una BD remota (MongoAtlas):

![](docs/img/taurus/transacciones/8wk/8wk-remoto-terminal.png)
![](docs/img/taurus/transacciones/8wk/8wk-remoto-final.png)

En esta prueba se consiguen **194.1 peticiones por segundo**, teniendo un tiempo de respuesta medio de 47ms. Por lo que en estas condiciones no se supera el mínimo de peticiones (1000).

Por último se realizaron las pruebas utilizando un Docker local para levantar el microservicio, los resultados se pueden ver a continuación:

* Primer escenario, utilizando un Docker y MongoDB de forma local:

![](docs/img/taurus/portatiles/docker/docker-local-terminal.png)
![](docs/img/taurus/portatiles/docker/docker-local-final.png)

En esta prueba se consiguen **1057.7 peticiones por segundo**, teniendo un tiempo de respuesta medio de 8ms. 

* Segundo escenario, utilizando un Docker y MongoDB de forma local:

![](docs/img/taurus/transacciones/docker/docker-local-terminal.png)
![](docs/img/taurus/transacciones/docker/docker-local-final.png)

En esta prueba se consiguen **1309.88 peticiones por segundo**, teniendo un tiempo de respuesta medio de 6ms.

* Primer escenario, utilizando un Docker y una BD remota (MongoAtlas):

![](docs/img/taurus/portatiles/docker/docker-remoto-terminal.png)
![](docs/img/taurus/portatiles/docker/docker-remoto-final.png)

En esta prueba se consiguen **65.17 peticiones por segundo**, teniendo un tiempo de respuesta medio de 141ms. Por lo que en estas condiciones no se supera el mínimo de peticiones (1000).

* Segundo escenario, utilizando un Docker y una BD remota (MongoAtlas):

![](docs/img/taurus/transacciones/docker/docker-remoto-terminal.png)
![](docs/img/taurus/transacciones/docker/docker-remoto-final.png)

En esta prueba se consiguen **64.77 peticiones por segundo**, teniendo un tiempo de respuesta medio de 142ms. Por lo que en estas condiciones no se supera el mínimo de peticiones (1000).

#### Resumen de resultados

El resumen de todas de las pruebas realizadas sobre ambos escenarios se muestran a continuación:

| Servicio | BD | Escenario | Avg. Throughput | Avg. Response Time |
|--------|--------|---------|---------|---------|
| Gunicorn 1 Worker | BD Local | 1 | 1059.7 | 6 |
| Gunicorn 1 Worker | BD Local | 2 | 1570.8 | 8 |
| Gunicorn 1 Worker | BD Remota | 1 | 65.17 | 141 |
| Gunicorn 1 Worker | BD Remota | 2 | 64.62| 142 |
| Gunicorn 2 Workers | BD Local | 1 | 1307.9 | 4 |
| Gunicorn 2 Workers | BD Local | 2 | 1661.38 | 5 |
| Gunicorn 2 Workers | BD Remota | 1 | 66.24 | 70 |
| Gunicorn 2 Workers | BD Remota | 2 | 131.42 | 71 |
| Gunicorn 8 Workers | BD Local | 1 | 2139.23 | 3 |
| Gunicorn 8 Workers | BD Local | 2 | 2399.85 | 3 |
| Gunicorn 8 Workers | BD Remota | 1 | 130.07 | 47 |
| Gunicorn 8 Workers | BD Remota | 2 | 194.1 | 47 |
| Docker | BD Local | 1 | 2763.8 | 8 |
| Docker | BD Local | 2 | 1309.88 | 6 |
| Docker | BD Remota | 1 | 198.64 | 141 |
| Docker | BD Remota | 2 | 64.77 | 142 |

#### Conclusiones de los resultados

Las conclusiones obtenidas de la ejecución de estas pruebas son:

* **Ambos microservicios (Portatiles & Transacciones)** han superado todas las prueba utilizando una base de datos local, puesto que se ha conseguido que superen las 1000 peticiones por segundo, en algunos casos las han multiplicado. En las pruebas que se utiliza una base de datos remota se nota mucho la diferencia en las peticiones, debido a la latencia que se produce al conectar con la base de datos remota.
* Como más peticiones se consiguen es levantando el servicio con 8 Workers utilizando guricorn o levantando un Docker local.
* Conforme más Workers utiliza guricorn mejores resultados se consiguen.

También documento, que se comenzó ejecutando las pruebas sobre una máquina virtual instalada en mi ordenador portátil, los resultados de lanzar la prueba del primer escenario (1 Worker con MongoDB local) en la máquina virtual, fueron los siguientes:

![](docs/img/taurus/test_maquina.png)

Por lo tanto se decidió cambiar la máquina virtual por mi ordenador de sobremesa que tiene instalado Ubuntu 19, y los resultados comenzaron a ser satisfactorios (resultados expuestos anteriormente).

Por lo que se concluye que la máquina donde se realiza el test de prestaciones también es importante y realizarlas en una máquina virtual no es una buena idea.
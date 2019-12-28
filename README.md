# Proyecto de Cloud Computing

[![License: LGPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/NSInductus/CC_Proyecto.svg?branch=master)](https://travis-ci.com/NSInductus/CC_Proyecto)
[![CircleCI](https://circleci.com/gh/NSInductus/CC_Proyecto.svg?style=svg)](https://circleci.com/gh/NSInductus/CC_Proyecto)
[![codecov](https://codecov.io/gh/NSInductus/CC_Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/NSInductus/CC_Proyecto)
[![Heroku](https://www.herokucdn.com/deploy/button.svg)](https://cc-proyecto.herokuapp.com/)

Proyecto para desarrollar en la asignatura de **Cloud Computing** correspondiente al Máster de Ingeniería Informática.

## Descripción

El proyecto consistirá en un bakc-end para la compra/venta de portátiles. Para una Descripción más detallada del proyecto, ver [aquí](docs/descripcion.md).

## Más información sobre el proyecto

A continuación se muestra en forma de índice el acceso a más información referente al proyecto.

* [Tecnologías utilizadas](docs/tecnologias.md).
* [Historias de usuario](docs/historias_de_usuario.md).
* [Test](docs/test.md).
* [Licencia](docs/licencia-md)

## Arquitectura

La arquitectura será una arquitectura basada en microservicios. Para más información acerca de la arquitectura del proyecto, ver [aquí](docs/arquitectura.md).

### Arquitectura de los Microservicios

Los microservicios implementados o que se implementarán tendrán una arquitectura por capas, la cuál se basa en separar la funcionalidad del microservicio en diferentes capas, con el fin de seguir los principios de: abstracción, encapsulamiento, funcionalidad, alta cohesión, reutilizable y desacople.

#### Arquitectura del microservicio: Portatiles


* **Primera capa:** la primera capa de este microservicio contiene la API REST, es decir, el archivo [Portatiles_rest.py](src/Portatiles_rest.py), este contendrá las rutas que se utilizarán para utilizar el microservicio, es decir, para realizar peticiones


* **Segunda capa:**  la segunda capa de este microservicio se encarga de administrar la lógica del microservicio, esta consiste en el archivo [Portatiles.py](src/Portatiles.py), el cuál está repleto de funciones que son de utilidad para la segunda capa.


* *Pendiente de añadir la última capa que contendrá la base de datos del microservicio y que será utilizada por el mismo.*

La Arquitectura de este servicio se puede comprender fácilmente observando la siguiente imagen:

![](docs/img/arquitectura_microservicio_portatiles.png)

## Microservicio: Portatiles

Este microservicio presenta las siguientes rutas:

1. **GET-> /** es la ruta de presentación y también sirbe para comprobar que funciona bien el microservicio.
2. **GET-> /numeroPortatilesEnVenta** es para ver cuantos portatiles existen en venta.
3. **GET-> /seleccionarPortatil/int:id_venta>** selecciona para mostrar el portatil en venta cuyo *id_vente* coincida con el introducido en la ruta.
4. **POST-> /agregarPortatil/marca/modelo/DNIvendedor/int:precio/comentario/pantalla/procesador/RAM/almacenamiento/grafica/bateria/SO** es para agregar un portátil al stock de venta, destacar que los 4 primeros argumentos son obligatorios: marca, modelo, DNIvendedor y precio, mientras el resto son opcionales.
5. **PUT-> /modificarPortatil/int:id_venta/int:precio/modelo/marca/comentario/pantalla/procesador/RAM/almacenamiento/grafica/bateria/SO** es para modificar un portátil anteriormente introducido en el stock de venta, destacar que son necesarios los 2 primeros argumentos: id_venta y precio, mientras los demás son opcionales.
6. **DELETE-> /eliminarPortatilPorIdVenta/int:id_venta>** es para eliminar un portátil existente en el stock de venta de portátiles.
7. **GET-> /verPortatilesEnVentaDeUsuario/DNIusuario** es para ver los portátiles que tiene en venta el usuario cuyo *DNI* coincida con el *DNIvendedor* de los portátiles.
8. **GET-> /buscarPortatilPorPrecio/int:limite_inferior/int:limite_superior** es para buscar un portátil por un rango de precios, entre los existentes en el stock de venta de portátiles.
9. **GET-> /buscarPortatilPorModeloMarca/modelo/marca** es para búscar un portátil por su modelo y su marca, entre los existentes en el stock de venta de portátiles.
10. **GET-> /compararPotatiles/modelo/marca** es parecida a la ruta anterior pero consigues una comparación de estos portátiles por precio de venta.
*Destacar que el microservicio manda los datos al cliente en forma de archivo json*

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

* **start**: Esta tarea es la encargada de levantar el microservicio utilizando gunicorn. En esta tarea se pueden utilizar 2 argumentos opcionales para modificar el host y el puerto donde se ejecuta, por defecto el host será *0.0.0.0* y el puerto será *8080*.
```
$ invoke start [-h/--host <host>] [-p/--puerto <puerto>]
```

* **stop**: Esta tarea es la encargada de detener el microservicio lanzado anteriormente con la tarea: *start*.
```
$ invoke stop
```

## Integración continua

La integración continua es una técnica que consiste en hacer integraciones de un proyecto con la mayor frecuencia posible, para detectar errores y problemas lo más pronto posible. La integración consiste en la compilación de todo el proyecto y la ejecución de las pruebas sobre el mismo.

Para el proyecto se han utilizado dos herramientas de integración continua, las cuales son:

* **Travis-CI**: La configuración de esta herramienta se encuentra en el fichero [.travis.yml](https://github.com/NSInductus/CC_Proyecto/blob/master/.travis.yml). Esta herramienta primero instalará las dependencias necesarias, es decir, las contenidas en el fichero [requirements.txt](https://github.com/NSInductus/CC_Proyecto/blob/master/requirements.txt), para posteriormente ejecutar tanto los test unitarios como los test de cobertura. Por último una vez se ejecuten los test, se enviarán los resultados de los test de cobertura a **codecov**. Según la configuración establecida en el fichero **.travis.yml** se ejecutará sobre un sistema **Linux** y sobre las versiones de **python**: 3.5.8, 3.6.9, 3.7.0, 3.7.3, 3.7.5 y 3.8.0.
* **Circle-CI**: La configuración de esta herramienta se encuentra en el fichero [config.yml](https://github.com/NSInductus/CC_Proyecto/blob/master/.circleci/config.yml). Esta herramienta tiene un funcionamiento parecido a la usada anteriormente aunque en este caso es necesario la creación de un entorno virtual (en el caso de este proyecto se usa **pipenv**) para el correcto funcionamiento de esta herramienta de integración continua. En esta caso se ejecutará en **Linux** sobre la versión de **python** 3.7.5.

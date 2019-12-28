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

* [Arquitectura](docs/arquitectura.md).
* [Tecnologías utilizadas](docs/tecnologias.md).
* [Historias de usuario](docs/historias_de_usuario.md).
* [Test](docs/test.md).
* [Licencia](docs/licencia-md)

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


## Integración continua

La integración continua es una técnica que consiste en hacer integraciones de un proyecto con la mayor frecuencia posible, para detectar errores y problemas lo más pronto posible. La integración consiste en la compilación de todo el proyecto y la ejecución de las pruebas sobre el mismo.

Para el proyecto se han utilizado dos herramientas de integración continua, las cuales son:

* **Travis-CI**: La configuración de esta herramienta se encuentra en el fichero [.travis.yml](https://github.com/NSInductus/CC_Proyecto/blob/master/.travis.yml). Esta herramienta primero instalará las dependencias necesarias, es decir, las contenidas en el fichero [requirements.txt](https://github.com/NSInductus/CC_Proyecto/blob/master/requirements.txt), para posteriormente ejecutar tanto los test unitarios como los test de cobertura. Por último una vez se ejecuten los test, se enviarán los resultados de los test de cobertura a **codecov**. Según la configuración establecida en el fichero **.travis.yml** se ejecutará sobre un sistema **Linux** y sobre las versiones de **python**: 3.5.8, 3.6.9, 3.7.0, 3.7.3, 3.7.5 y 3.8.0.
* **Circle-CI**: La configuración de esta herramienta se encuentra en el fichero [config.yml](https://github.com/NSInductus/CC_Proyecto/blob/master/.circleci/config.yml). Esta herramienta tiene un funcionamiento parecido a la usada anteriormente aunque en este caso es necesario la creación de un entorno virtual (en el caso de este proyecto se usa **pipenv**) para el correcto funcionamiento de esta herramienta de integración continua. En esta caso se ejecutará en **Linux** sobre la versión de **python** 3.7.5.

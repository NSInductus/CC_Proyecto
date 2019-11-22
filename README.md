# Proyecto de Cloud Computing

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![](https://travis-ci.com/NSInductus/CC_Proyecto.svg?branch=master)](https://travis-ci.com/NSInductus/CC_Proyecto)
[![](https://circleci.com/gh/NSInductus/CC_Proyecto.svg?style=svg)](https://circleci.com/gh/NSInductus/CC_Proyecto)
[![](https://codecov.io/gh/NSInductus/CC_Proyecto/branch/master/graph/badge.svg)](https://codecov.io/gh/NSInductus/CC_Proyecto)


Proyecto para desarrollar en la asignatura de Cloud Computing correspondiente al Máster de Ingeniería Informática.

## Descripción del problema

Hoy día todos sabemos de la importancia de los ordenadores y de Internet, prácticamente toda familia tiene más de un ordenador en casa.
En los últimos años, los ordenadores portátiles han ganado mucho terreno a los ordenadores de sobremesa, por poder tener un ordenador con las mismas características que un ordenador de sobremesa sumado a su gran comodidad a la hora de ser trasportado.
Los estudiantes de universidad necesitan el ordenador sea cuál sea la carrera que estén estudiando aunque solo lo necesiten para descargar apuntes y escribir en archivos de texto. Los ordenadores portátiles nuevos con unas características decentes para que les puedan servir fuera de la universidad para algo más que para descargar apuntes no suelen ser baratos, si a esto le sumamos que normalmente los estudiantes tienen problemas de dinero, estos pueden llegar a tener dificultades para conseguir un ordenador portátil medio decente.

## Descripción de la solución

Como solución se creará un servicio ficticio para que el cliente pueda tanto comprar como vender unicamente ordenadores portátiles. Esto facilitará la vida a las personas que quieran encontrar un ordenador decente por una cantidad no muy alta de dinero. El cliente podrá comprar los ordenadores a través de monedas virtuales que se podrán adquirir con dinero real, una vez comprado el ordenador se mandará a la dirección del cliente comprador. El cliente comprador podrá probar el ordenador durante unos 5 días y si no le convence podrá devolverlo mediante la aplicación, de forma que irán a recogerlo de forma totalmente gratuita. En definitiva el proyecto tratará de la creación de un backend para un servicio de venta de portátiles.

## Arquitectura

La arquitectura será una arquitectura basada en microservicios, contaremos con microservicios que se conectarán entre sí para cumplir con las funcionalidades que ofrece la aplicación. Para más información acerca de la arquitectura del proyecto, ver [aquí](docs/arquitectura.md).

## Tecnologías utilizadas


Para la información completa de las tecnologías que se utilizarán, ver [aquí](docs/tecnologias.md).

## Historias de usuarios

Las historias de usuario se pueden ver [aquí](docs/historias_de_usuario.md).

## Test

Destacar que durante este proyecto se ha optado por una técnica de diseño e implementación software que se incluye dentro de la metodología ágil, concretamente la técnica del desarrollo dirigido por pruebas (TDD), puesto que al diseñar aplicando este técnica se consigue:
* La implementación de las funciones justas que quiere el cliente y nada más.
* La minimización del número de defectos software.
* La creación de un software modular. reutilizable y que se pueda cambiar en el futuro.

Para realizar los test en este proyecto se utilizará el framework **pytest**.

Para instalar **pytest** se escribe en terminal el siguiente comando:
```shell
$ pip install pytest
```

Para los test de covertura se ha utilizado el plug-in **pytest-cov**.


Para instalar **pytest-cov** se escribe en la terminal el siguiente comando:
```shell
$ pip install pytest-cov
```

## Herramienta de construcción

Como herramienta de construcción se utilizará **invoke**, por su...

Para poder utilizarla hay que instalarla en python, para eso se escribe en la terminal el siguiente comando:

```shell
$ pip install invoke
```

Para la configuración de la misma, se ha agregado el fichero **tasks.py**.


```
buildtool: tasks.py
```

Para utilizar la herramienta de construcción se ha de escribir en la terminal "invoke" seguido de la tarea que se desea que realice la herramienta. Estas tareas se han definido anteriormente en el fichero de configuración de la herramienta.

Las posibles tareas que se pueden hacer son:

* **install**: Esta tarea es la encargada de instalar las dependencias necesarias para que funcione nuestro proyecto, las cuales están definidas en el fichero **requirements.txt**. Para esto hay que escribir en la terminal:
```shell
$ invoke install
```

* **test**: Esta tarea es la encargada de ejecutar los test unitarios, sobre nuestras clases de python. Para esto hay que escribir en la terminal:
```shell
$ invoke test
```

* **coverage**: Esta tarea es la encargada de ejecutar los test de covertura, sobre nuetsras clases de python. Para esto hay que escribir en la terminal:
```shell
$ invoke coverage
```


## Integración continua


## Licencia

Este proyecto está licenciado bajo la licencia GNU General Public License v3.0.

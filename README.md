# Proyecto de Cloud Computing

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


## Licencia

Este proyecto está licenciado bajo la licencia GNU General Public License v3.0.

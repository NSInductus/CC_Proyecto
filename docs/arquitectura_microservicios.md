# Arquitectura de microservicios

A continuación se va a describir especificamente la arquitectura de los dos microservicios disponibles, es decir, del microservicio de gestión de portatiles (Portatiles) y del microservicio de transaciones (Transaciones).

## Arquitectura del microservicio: Portatiles


* **Primera capa:** la primera capa de este microservicio contiene la API REST, es decir, el archivo [Portatiles_rest.py](src/Portatiles_rest.py), este contendrá las rutas que se utilizarán para utilizar el microservicio, es decir, para realizar peticiones referentes a la gestión de portátiles.


* **Segunda capa:**  la segunda capa de este microservicio se encarga de administrar la lógica de negocio del microservicio, esta contiene el archivo [Portatiles.py](src/Portatiles.py), el cuál está repleto de funciones que son de utilidad para poder cumplir con las historias de usuario.

* **Tercera capa:** la tercera capa de este microservicio se encarga de administrar la base de datos donde se guardan y administran todos los portatiles, esta capa contiene el archivo [MongoDM.py](src/MongoDM.py).

La Arquitectura de este servicio se puede comprender fácilmente observando la siguiente imagen:

![](docs/img/arquitectura_microservicio_portatiles.png)


## Arquitectura del microservicio: Transaciones


* **Primera capa:** la primera capa de este microservicio contiene la API REST, es decir, el archivo [Transaciones_rest.py](src/Transaciones_rest.py), este contendrá las rutas que se utilizarán para utilizar el microservicio, es decir, para realizar peticiones referentes a las transaciones de compra/venta/devolución.


* **Segunda capa:**  la segunda capa de este microservicio se encarga de administrar la lógica del microservicio, esta contiene el archivo [Transaciones.py](src/Transaciones.py), el cuál está repleto de funciones que son de utilidad para poder cumplir con las historias de usuario.


* **Tercera capa:** la tercera capa de este microservicio se encarga de administrar la base de datos donde se guardan y administran todas las transaciones, esta capa contiene el archivo [MongoDM.py](src/MongoDM.py).

La Arquitectura de este servicio se puede comprender fácilmente observando la siguiente imagen:

![](docs/img/arquitectura_microservicio_portatiles.png)

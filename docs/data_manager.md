# Data Manager: MongoDM.py

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

## Inyección de dependencias

Como se ha comentado anteriormente se ha utilizado la técnica de la *inyección de dependencias* para conseguir que los microservicios de nuestro proyecto utilicen de forma abstracta la base de datos, para ello se ha creado la clase [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py).

Para la inyección de esta clase, se importará en los ficheros que implementan la lógica de negocio de cada uno de los microservicos, es decir, [Portatiles.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Portatiles.py) y [Transacciones.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Transacciones.py), para posteriormente crear un objeto de la clase [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py). Los campos existentes en el constructor de la clase son:

* **uri:** Este parámetro contiene la dirección base, de la base de datos, en el caso de que se este lanzando en local tendremos que poner: *localhost:5000*. Como se ha podido ver: el formato de esta dirección base es el siguiente: *host:puerto*
* **basedatos:** Este parámetro contiene el nombre de la base de datos con la que se trabajará.
* **coleccion:** Esta parámetro contiene el nombre de la colección con la que se trabajará.

*Para la introducción de estos parámetros se utilizarán variables de entorno, para más información acerca de éstas, clicar [aqui](variables_de_entorno.md).*

El *objetivo o fin* de este proceso es que la lógica de negocio de un microservicio y la base de datos sean totalmente independientes, de tal forma que si en el futuro se desea cambiar de base de datos tan solo sea necesario cambiar el *Data Manager*.

De tal forma que la *API REST* realizará llamadas a las funciones de la lógica de negocio del microservicio y esta utilizará el *Data Manager* para gestionar los datos. Cumpliendo con la arquitectura por capas, la cual es la arquitectura que poseen todos mis microservicios implementados.

## Modificaciones en otros ficheros

Se han tenido que realizar una serie de modificaciones sobre algunos ficheros para adaptarlos a la incorporación del *Data Manager*, es decir, del fichero [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py).

1. En primer lugar, se han tenido que modificar los ficheros correspondientes al primer microservicio que se había implementado anteriormente, es decir, el microservicio de Portatiles. Porque éste trabajaba con una lista interna, que se ha sustituido por un data_manager, por eso al constructor de esta clase se le introduce un objeto que actuará como data_manager, en este caso, un objeto de tipo MongoDM.
Destacar que hay que cambiar tanto los ficheros de código propiamente dicho, es decir, [Portatiles.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Portatiles.py) y [Portatiles_rest.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Portatiles_rest.py), como los ficheros de test (aunque los cambios sean más insignificativos comparados con los de los ficheros anteriores), es decir, [test_Portatiles.py](https://github.com/NSInductus/CC_Proyecto/blob/master/test/test_Portatiles.py) y [test_Portatiles_rest.py](https://github.com/NSInductus/CC_Proyecto/blob/master/test/test_Portatiles_rest.py).

2. En segundo lugar, los sistemas de integración continua se ha tenido que realizar los siguientes cambios:

  * *En TravisCi:* Se ha añadido las variables de entorno y se ha agregado de servicio, el servicio de mongoDB.

  * *En CircleCi:* Se ha agregago las variables de entorno y se ha agregado una imagen de docker (correspondiente a MongoDB).

3. En tercer lugar, se ha creado un Dockerfile nuevo, así como se ha creado una nueva regla de construcción automática, se puede ver con más detalle [aquí](docker.md).

*Destacar que en el nuevo microservicio implementado, ya se tiene en cuenta que se utilice el Data Manager desde el primer momento.*
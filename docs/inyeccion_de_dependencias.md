# Inyección de dependencias

Como se comento en la sección anterior se ha utilizado el método de la *inyección de dependencias* para incrustar la base de datos de MongoDB en nuestros microservicios, para ello se ha creado la clase [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py), descrita en la sección anterior.

Para la incrustación de la misma, se importara en los ficheros que implementan la lógica de negocio de cada uno de los microservicos, es decir, [Portatiles.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Portatiles.py) y [Transacciones.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/Transacciones.py), para posteriormente crear un objeto de la clase [MongoDM.py](https://github.com/NSInductus/CC_Proyecto/blob/master/src/MongoDM.py). Los campos existentes en el constructor de la clase son:

* **uri:** Este parámetro contiene la dirección base, de la base de datos, en el caso de que se este lanzando en local tendremos que poner: *localhost:5000*. Como se ha podido ver: el formato de esta dirección base es el siguiente: *host:puerto*
* **basedatos:** Este parámetro contiene el nombre de la base de datos con la que se trabajará.
* **coleccion:** Esta parámetro contiene el nombre de la colección con la que se trabajará.

Para la introducción de estos parámetros se utilizarán variables de entorno.

El *objetivo o fin* de este proceso es que la lógica de negocio de un microservicio y la base de datos sean totalmente independientes, de tal forma que si en el futuro se desea cambiar de base de datos tan solo sea necesario cambiar el *data_manager*.

De tal forma que la *APIREST* realizará llamadas a las funciones de la lógica de negocio del microservicio y esta utilizará el *data_manager* para gestionar los datos. Cumpliendo con la arquitectura por capas, la cual es la arquitectura que poseen todos mis microservicios.

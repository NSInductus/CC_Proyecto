# Variables de entorno

Las variables de entorno son neecesarias antes de lanzar el *invoke test*, *invoke coverage* o el *invoke start*.

Estas variables de entorno ayudarán a conseguir la uri base de los microservicios, los nombres de bases de datos, de colecciones o las uri base de las bases de datos, por esto son muy importantes.

Las variables de entorno que debemos configurar son:
* **URI_BD_P:** contiene la dirección base (uri base) de la base de datos del microservicio Portatiles.
* **URI_BD_T:** contiene la dirección base (uri base) de la base de datos del microservicio Transaciones.
* **BD_P:** contiene el nombre de la base de datos del microservicio Portatiles.
* **BD_T:** contiene el nombre de la base de datos del microservicio Transacciones.
* **CO_P:** contiene el nombre de la colección del microservicio Portatiles.
* **CO_T:** contiene el nombre de la colección del microservicio Transaciones.
* **HOST:** contiene la direccion donde se quiere que arranque el microservicio o los microservicios.
* **PORT:** contiene el puerto donde arrancará el primer microservicio (Portatiles o Transacciones si no se arranca Portatiles)
* **PORT_2:** contiene el puerto donde arrancará el segundo microservicio (transacciones)




Un ejemplo para configurar estas variables es abrir el terminal de *Ubuntu* y introducir el siguiente código:


```
export URI_BD_P="mongodb+srv://Inductus:1234@cluster0-498ya.gcp.mongodb.net/test?retryWrites=true&w=majority"
export URI_BD_T="mongodb+srv://Inductus:1234@cluster0-498ya.gcp.mongodb.net/test?retryWrites=true&w=majority"
export BD_P="BDPruebaPortatiles"
export CO_P="COPruebaPortatiles"
export BD_T="BDPruebaTransacciones"
export CO_T="COPruebaTransacciones"
export HOST="localhost"
export PORT="8080"
export PORT_2="8000"
```


*Destacar que los sistemas de integración continua se encargan por sí mismos de inicializarlas, tanto TravisCI como CircleCI*

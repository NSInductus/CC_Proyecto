# APIs REST

Cada uno de los microservicios utiliza una **API REST**, que actúa como interfaz, al que se puede acceder a través de rutas *HTTP*, con el fin de conseguir datos o hacer operaciones sobre datos, en nuestro caso en formato *JSON*.

A continuación se especifica las rutas para cada uno de los microservicios existentes.

## Microservicio: Portatiles

Este microservicio presenta las siguientes rutas:

1. **GET-> /portatiles/** es la ruta de presentación y también sirve para comprobar que funciona bien el microservicio.
2. **GET-> /portatiles/numeroPortatilesEnVenta** es para ver cuantos portatiles existen en venta.
3. **GET-> /portatiles/seleccionarPortatil/int:id_venta>** selecciona un portátil en venta, cuyo *id_vente* coincida con el introducido en la ruta.
4. **POST-> /portatiles/agregarPortatil/marca/modelo/DNIvendedor/int:precio/comentario/pantalla/procesador/RAM/almacenamiento/grafica/bateria/SO** es para agregar un portátil al stock de venta, destacar que los 4 primeros argumentos son obligatorios: marca, modelo, DNIvendedor y precio, mientras el resto son opcionales.
5. **PUT-> /portatiles/modificarPortatil/int:id_venta/int:precio/modelo/marca/comentario/pantalla/procesador/RAM/almacenamiento/grafica/bateria/SO** es para modificar un portátil anteriormente introducido en el stock de venta, destacar que son necesarios los 2 primeros argumentos: id_venta y precio, mientras los demás son opcionales.
6. **DELETE-> /portatiles/eliminarPortatilPorIdVenta/int:id_venta** es para eliminar un portátil existente en el stock de venta de portátiles.
7. **GET-> /portatiles/verPortatilesEnVentaDeUsuario/DNIusuario** es para ver los portátiles que tiene en venta el usuario cuyo *DNI* coincida con el *DNIvendedor* de los portátiles.
8. **GET-> /portatiles/buscarPortatilPorPrecio/int:limite_inferior/int:limite_superior** es para buscar un portátil por un rango de precios, entre los existentes en el stock de venta de portátiles.
9. **GET-> /portatiles/buscarPortatilPorModeloMarca/modelo/marca** es para búscar un portátil por su modelo y su marca, entre los existentes en el stock de venta de portátiles.
10. **GET-> /portatiles/compararPotatiles/modelo/marca** es parecida a la ruta anterior pero consigues una comparación de estos portátiles por precio de venta.


*Destacar que el microservicio manda los datos al cliente en forma de archivo json*



## Microservicio: Transaciones

Este microservicio presenta las siguientes rutas:

1. **GET-> /transaciones/** es la ruta de presentación y también sirve para comprobar que funciona bien el microservicio.
2. **POST-> /transaciones/venderPortatil/id_portatil/DNIcomprador/comentario** es para vender un portátil que tenemos disponible en el stock, de esta forma se pondrá el atributo "vendido" del portátil a True(1), lo que significará que se ha vendido, además de crear dos transacciones una indicando que el comprador a comprado el portátil y otra indicando que el vendedor a vendido el portátil.
3. **POST-> /transaciones/devolverPortatil/id_portatil/DNIcomprador/comentario** es para devolver un portátil que el usuario comprara anteriormente, de esta forma se pondrá el atributo "vendido" del portátil a False(0), lo que significará que se ha devuelto y se puedo volver a comprar. Además añadirá una transacción a la persona que lo devuelva.
4. **GET-> /transaciones/verEstadisticas/DNIusuario/int:tipo** se pueden comprobar todas las transacciones de un usuario. Hay dos formas, la primera es en general, es decir, se comprueban las transacciones de tipo compra/venta/devolución. La segunda forma es comprobar la transacciones de un usuario pero solo las de un tipo, es decir, o las transacciones de compra o las de venta o las de devolución.

*La razón para tener el atributo vendido, y no eliminar el portátil directamente es por una posible devolución, es decir, por si el comprador decide devolverlo.*

*Destacar que el microservicio manda los datos al cliente en forma de archivo json*

# Comparación de imagenes base

El proceso de selección a consistido en: probar con 4 imágenes diferentes, las 4 de repositorios oficiales, 2 de ellas de python (imagenes que ya traian instalado python sobre un sistema Linux), 1 de ellas de fedora y otra de debian, destacar que para estas 2 últimas se ha tenido que instalar python puesto que no lo traían instalado de serie.

Concretamente las imágenes con las que se ha probado han sido:

* **python:3.6-slim-stretch**
* **python:slim-buster**
* **fedora:31**
* **debian:unstable-slim**

El proceso de selección se ha basado en el uso de la herramienta: *ab - Apache HTTP server benchmarking tool* realizando una serie de peticiones a una de las rutas y comprobar cuál de las imágenes conseguía realizar las peticiones en el menor tiempo posible. Los resultados se pueden ver a continuación:

|Imagen Base|Tiempo para realizar las peticiones|
|--------|--------|
|python:3.6-slim-stretch|0.236 segundos|
|python:slim-buster|0.215 segundos|
|fedora:31|0.238 segundos|
|debian:unstable-slim|0.168 segundos|

Como se demuestra en la tabla anterior la mejor opción es la imagen base de **debian**.

*Destacar que para la realización de estas pruebas se ha tenido que arrancar el contenedor y posteriormente instalar la herramienta apache2-utils antes de poder utilizar ab.*

A continuación se muestra el código saliente procedente de la terminal después de realizar cada una de las peticiones:

* python:3.6-slim-stretch

```
Server Software:        gunicorn/20.0.4
Server Hostname:        0.0.0.0
Server Port:            8080

Document Path:          /agregarPortatil/MSI/GL60/333X/2500
Document Length:        3 bytes

Concurrency Level:      10
Time taken for tests:   0.236 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      15400 bytes
HTML transferred:       300 bytes
Requests per second:    424.26 [#/sec] (mean)
Time per request:       23.571 [ms] (mean)
Time per request:       2.357 [ms] (mean, across all concurrent requests)
Transfer rate:          63.80 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       1
Processing:     3   22   4.5     21      30
Waiting:        2   22   4.5     21      29
Total:          4   22   4.3     21      30

Percentage of the requests served within a certain time (ms)
  50%     21
  66%     24
  75%     26
  80%     26
  90%     28
  95%     28
  98%     29
  99%     30
 100%     30 (longest request)
```

* python:slim-buster

```
Server Software:        gunicorn/20.0.4
Server Hostname:        0.0.0.0
Server Port:            8080

Document Path:          /agregarPortatil/MSI/GL60/333X/2500
Document Length:        3 bytes

Concurrency Level:      10
Time taken for tests:   0.215 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      15400 bytes
HTML transferred:       300 bytes
Requests per second:    465.15 [#/sec] (mean)
Time per request:       21.499 [ms] (mean)
Time per request:       2.150 [ms] (mean, across all concurrent requests)
Transfer rate:          69.95 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     2   20   4.9     19      28
Waiting:        2   20   4.9     19      27
Total:          3   20   4.8     19      28

Percentage of the requests served within a certain time (ms)
  50%     19
  66%     22
  75%     24
  80%     25
  90%     26
  95%     27
  98%     28
  99%     28
 100%     28 (longest request)

```

* fedora:31

```

Server Software:        gunicorn/20.0.4
Server Hostname:        0.0.0.0
Server Port:            8080

Document Path:          /agregarPortatil/MSI/GL60/333X/2500
Document Length:        3 bytes

Concurrency Level:      10
Time taken for tests:   0.238 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      15400 bytes
HTML transferred:       300 bytes
Requests per second:    420.78 [#/sec] (mean)
Time per request:       23.765 [ms] (mean)
Time per request:       2.377 [ms] (mean, across all concurrent requests)
Transfer rate:          63.28 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       1
Processing:     3   22   5.3     23      33
Waiting:        2   22   5.3     23      32
Total:          3   22   5.2     23      33

Percentage of the requests served within a certain time (ms)
  50%     23
  66%     25
  75%     26
  80%     26
  90%     28
  95%     30
  98%     33
  99%     33
 100%     33 (longest request)

```

* debian:unstable-slim

```

Server Software:        gunicorn/20.0.4
Server Hostname:        0.0.0.0
Server Port:            8080

Document Path:          /agregarPortatil/MSI/GL60/333X/2500
Document Length:        3 bytes

Concurrency Level:      10
Time taken for tests:   0.168 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      15400 bytes
HTML transferred:       300 bytes
Requests per second:    595.83 [#/sec] (mean)
Time per request:       16.783 [ms] (mean)
Time per request:       1.678 [ms] (mean, across all concurrent requests)
Transfer rate:          89.61 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       1
Processing:     2   16   3.4     16      23
Waiting:        2   15   3.4     16      22
Total:          3   16   3.3     16      23

Percentage of the requests served within a certain time (ms)
  50%     16
  66%     17
  75%     17
  80%     18
  90%     19
  95%     20
  98%     22
  99%     23
 100%     23 (longest request)

```

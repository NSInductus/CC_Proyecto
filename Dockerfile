# Elegimos la imagen base y el tag deseado.
FROM debian:unstable-slim

# Nombre y correo de la persona que mantiene el contenedor
LABEL maintainer="Angel Murcia Diaz <angelmd96@correo.ugr.es>"

# Puerto como Argumento para pasar a la hora de construir
#Por defecto sera el puerto 8080
ARG PORT=8080

# Establecemos las variables de entorno para el contenedor
# Definimos el puerto
ENV PORT=${PORT}

# Establecer el directorio de trabajo
WORKDIR /

# Instalamos python3 y pip3
RUN apt-get update && apt-get install -y python python3-pip

# Copiamos el archivo requirements
COPY requirements.txt /tmp/

# Instalamos lo necesario utilizando el requirements
RUN pip3 install --no-cache-dir -r ./tmp/requirements.txt

# Copiamos los archivos necesarios para levantar el microservicio
COPY src /src/

# Puerto donde va a escuchar el servidor
EXPOSE ${PORT}

# Cambiar el directorio de trabajo
WORKDIR /src/

# Lanzar el servidor
CMD gunicorn -b 0.0.0.0:${PORT} Portatiles_rest:app

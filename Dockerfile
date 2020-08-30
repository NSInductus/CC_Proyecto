# Elegimos la imagen base y el tag deseado.
FROM debian:unstable-slim

# Nombre y correo de la persona que mantiene el contenedor
LABEL maintainer="Angel Murcia Diaz <angelmd96@correo.ugr.es>"

# Se definen las variables a utilizar
ARG URI_BD_P
ARG BD_P
ARG CO_P
ARG PORT

# Se asigna el valor de la variable de entorno a la variable
ENV URI_BD_P=${URI_BD_P}
ENV BD_P=${BD_P}
ENV CO_P=${CO_P}
ENV PORT=${PORT}

# Establecer el directorio de trabajo
WORKDIR /

# Se actualizna los repositorios de debian y se instala el paquete de utilidades
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -yq apt-utils

# Instalamos python3 y pip3
RUN apt-get install -y python3 python3-pip

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
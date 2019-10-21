# Descargar git y configurar

En primer lugar se ha descargado a través de la terminal de linux git, introduciendo los siguientes comandos:

	sudo apt-get update
	sudo apt-get install git

Después se ha configurado git para que aparezcan mis datos en los commit, poniendo en la terminal los siguientes comandos:

	git config --global user.name "Ángel Murcia Díaz"
	git config --global user.email "angel.ns.333@gmail.com"

# Modificación del perfil de GITHUB

Se ha añadido una foto del estudiante, así como su nombre completo, ciudad y universidad, el perfil a quedado como se ve en la siguiente imagen:

![](img/PerfilActualizado.png)

PerfilActualizado.png

# Creación de de clave SSH

Para esto hemos creado una clave a través de la terminal poniendo:

	ssh-keygen rsa -b 4096 "angel.ns.333@gmail.com"

Una vez creada la clave copiamos el interior del fichero id_rsa.pub y pegamos su contenido en GITHUB, concretamente en el recuadro que sale cuando el cusuario presiona Setting y después SSH Keys.

# Activar Two-facto authentication

Para esto dentro de GITHUB entramos a la opción Two-factor authentication (dentro de Setting y Security)

Una vez alli le damos a activar, posteriormente nos dirimos a nuestro Smartphone y nos descargamos cualquier aplicación que tenga la funcionalidad de Two-factor authentication, yo me he descargado 2FAS Auth, una vez descargada escaneamos el código QR que aparece en GITHUB para posteriormente introducir en GITHUB el código de 6 dígitos que proporciona la APP.

Después de configurar GITHUB con este tipo de seguridad cada vez que intento acceder a GITHUB necesito introducir un código de 6 digitos que genera la APP al instante.

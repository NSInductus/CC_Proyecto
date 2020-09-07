# Vagrantfile

Como se explico en la sección anterior el *Vagrantfile* es el archivo de configuración que utiliza *Vagrant* para crear máquinas virtuales. El punto fuerte de este es que se puede replicar exactamente la misma máquina virtual en numerosas ocasiones.

En el caso de mi proyecto se necesitan dos *Vagranfiles* diferentes, uno para el despliegue local y otro para el despliegue remoto, pero están ambos contenidos en el siguiente fichero: [Vagrantfile](https://github.com/NSInductus/CC_Proyecto/blob/master/Vagrantfile).

De forma que se descomenta la parte útil, por ejemplo si se desea hacer un despliegue de forma local se descomenta la parte "Vagrantfile Local", por el contrario si se desea realizar un despliegue remoto se descomenta la parte "Vagrantfile Azure".

## Vagrantfile Local

```
#Version de la configuracion
Vagrant.configure("2") do |config|

    #Utiliza ubuntu/bionic como box (sistema operativo)
    config.vm.box = "ubuntu/bionic64"
```
En esta primera parte está comprobando que la versión de la configuración de *Vagrant* sea la 2 y posteriormente esta instalando la imagen base, en este caso ubuntu/bionic64.

```
    #Puertos de la maquina virtual que se conectaran a los puertos de nuestra maquina
    config.vm.network "forwarded_port", guest: 8080, host: 8080
    config.vm.network "forwarded_port", guest: 8000, host: 8000
```
Después esta conectando los puertos de la máquina virtual con los puertos del ordenador para poder acceder a ellos con mayor facilidad.

```
    #Configuramos la memoria y el numero de cpus que tendra la maquina virtual
    config.vm.provider "virtualbox" do |virtualbox|
        virtualbox.memory = 2048
        virtualbox.cpus = 2
    end
```
A continuación se definen los recursos que queremos que tenga la máquina virtual que se va a crear.
```
    #Configuramos la provision a traves de ansible
    config.vm.provision "ansible" do |ansible|
        #ansible.verbose="vvv"
        ansible.inventory_path = "./provision/ansible_hosts"
        ansible.limit="hostlocal"
        ansible.playbook = "./provision/workstate.yml"
    end

end
```
Por último, se provisiona según el fichero playbook de ansible, también se indica la ruta del inventario.

## Vagrantfile Remoto

```
# Incluir vagrant-azure
require 'vagrant-azure'

Vagrant.configure('2') do |config|
    # Usamos la box que hemos descargado para Azure
    config.vm.box = 'azure'
```
En este caso se incluye el plugin instalado (vagrant-azure) y al igual que en el caso del despliegue local se comprueba la version de la configuración de *Vagrant*, para despues usar la box descargada anteriormente.

```
    # Clave ssh
    config.ssh.private_key_path = '~/.ssh/id_rsa'
```
Se le indica la ruta donde se encuentra la clave privada ssh, se puede crear en caso de que el usuario no la posea.

```
    # Provider en Azure
    config.vm.provider :azure do |az, override|
        # Variables de entorno necesarias para despliegue en azure
        az.tenant_id = ENV['AZURE_TENANT_ID']
        az.client_id = ENV['AZURE_CLIENT_ID']
        az.client_secret = ENV['AZURE_CLIENT_SECRET']
        az.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

        # Parámetros de la maquina virtual a crear
        #Nombre de la máquina
        az.vm_name = 'proyectoccazure'
        # Recursos
        az.vm_size = 'Standard_B2s'
        # Imagen a utilizar
        az.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:latest'
        # Nombre grupo de recursos
        az.resource_group_name = 'vagrant-azure'
        # Puertos a utilizar
        az.tcp_endpoints = [8080, 8000]
    end
```
A continuación se indica a azure todas las variables de entorno necesarias (*estás variables son privadas únicas para cada persona por lo que no serán visibles*), también se le indican parámetros como el nombre de la máquina, el tamaño (entre tamaños definidos), la imagen base a utilizar, el nombre del grupo de recursos y finalmente los puertos a utilizar.

```
    # Provision con ansible
    config.vm.provision "ansible" do |ansible|
        #ansible.verbose="vvv"
        ansible.inventory_path = "./provision/ansible_hosts"
        ansible.limit="hostazure"
        ansible.playbook = "./provision/workstate.yml"
    end
end
```

Finalmente, se provisiona la máquina virtual creada en *Azure* con el mismo playbook que se utilizó anteriormente (comentar la línea adecuada).
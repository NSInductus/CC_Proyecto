#Referencia: https://www.adictosaltrabajo.com/2015/09/04/creacion-de-entornos-de-integracion-con-ansible-y-vagrant/
#Vagrantfile Local

#Version de la configuracion
#Vagrant.configure("2") do |config|

    #Utiliza ubuntu/bionic como box (sistema operativo)
    #config.vm.box = "ubuntu/bionic64"

    #Puertos de la maquina virtual que se conectaran a los puertos de nuestra maquina
    #config.vm.network "forwarded_port", guest: 8080, host: 8080
    #config.vm.network "forwarded_port", guest: 8000, host: 8000

    #Configuramos la memoria y el numero de cpus que tendra la maquina virtual
    #config.vm.provider "virtualbox" do |virtualbox|
        #virtualbox.memory = 2048
        #virtualbox.cpus = 2
    #end

    #Configuramos la provision a traves de ansible
    #config.vm.provision "ansible" do |ansible|
        ##ansible.verbose="vvv"
        #ansible.inventory_path = "./provision/ansible_hosts"
        #ansible.limit="hostlocal"
        #ansible.playbook = "./provision/workstate.yml"
    #end

#end

# Referencia: https://github.com/Azure/vagrant-azure
#Vagrantfile Azure

# Incluir vagrant-azure
require 'vagrant-azure'

#Version de la configuracion
Vagrant.configure('2') do |config|
    # Usamos la box que hemos descargado para Azure
    config.vm.box = 'azure'

    # Clave ssh
    config.ssh.private_key_path = '~/.ssh/id_rsa'

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

    # Provision con ansible
    config.vm.provision "ansible" do |ansible|
        #ansible.verbose="vvv"
        ansible.inventory_path = "./provision/ansible_hosts"
        ansible.limit="azure"
        ansible.playbook = "./provision/workstate.yml"
    end
end
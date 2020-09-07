#Referencia: https://www.adictosaltrabajo.com/2015/09/04/creacion-de-entornos-de-integracion-con-ansible-y-vagrant/
#Vagrantfile Local

#Version de la configuracion
Vagrant.configure("2") do |config|

    #Utiliza ubuntu/bionic como box (sistema operativo)
    config.vm.box = "ubuntu/bionic64"

    #Puertos de la maquina virtual que se conectaran a los puertos de nuestra maquina
    config.vm.network "forwarded_port", guest: 8080, host: 8080
    config.vm.network "forwarded_port", guest: 8000, host: 8000

    #Configuramos la memoria y el numero de cpus que tendra la maquina virtual
    config.vm.provider "virtualbox" do |virtualbox|
        virtualbox.memory = 2048
        virtualbox.cpus = 2
    end

    #Configuramos la provision a traves de ansible
    config.vm.provision "ansible" do |ansible|
        #ansible.verbose="vvv"
        ansible.inventory_path = "./provision/ansible_hosts"
        ansible.limit="hostlocal"
        ansible.playbook = "./provision/workstate.yml"
    end

end
# Playbook de Ansible: Workstate.yml

Como se ha comentado anteriormente el playbook de *Ansible* es como un libro de recetas que configura todas las tareas que el usuario ha definido en la máquina virtual.

Tal como están preparado el proyecto con el mismo fichero se puede provisionar tanto la máquina virtual creada de forma local como la máquina virtual creada de forma remota. Tan solo hay que comentar la parte que no sea de utilidad.

El fichero se puede ver [aquí](https://github.com/NSInductus/CC_Proyecto/blob/master/provision/workstate.yml).

A continuación se va a detallar en profundidad:

```
#Playbook para provisionar la maquina levantada con Vagrant en local
---
#Host
#- hosts: hostazure
- hosts: hostlocal
  #Activa root
  become: yes
  #Roles que se ejecutan antes de las tareas
  roles:
    - enix.mongodb
    - geerlingguy.docker
  #Fichero de variables de entorno
  vars_files:
    - ./env/env-file.yml
```
En esta primera parte, se está indicando que host se va a utilizar (definidos en el fichero de inventario), se están activando los privilegios de administrador (root), se están activando para ser usados los roles (enix.mongodb y geerlingguy.docker) y por ultimo estamos introduciendo el archivo env-files.yml como el archivo que contiene las variables de entorno necesarias.

```
  #Tareas
  tasks:
    #Tarea para iniciar el servio de MongoDB
    - name: Arrancar el servicio de MongoDB
      service: 
        name: mongod
        state: started
    #Tarea para actualizar el sistema con update
    - name: Actualizar sistema
      command: apt update
    #Tarea para instalar Python3 y pip3
    - name: Instalar Python3 y Pip3
      apt:
        pkg: ["python3","python3-pip"]
        state: present 
    #Tarea para instalar Docker
    - name: Instalar Docker
      pip:
        name: docker
    #Tarea para descargar la imagen del microservicio Portatiles de dockerhub
    - name: Descargar imagen del microservicio portatiles
      docker_image:
        name: nsinductus/cc_proyecto:latest
        source: pull
    #Tarea para descargar la imagen del microservicio Portatiles de dockerhub
    - name: Descargar imagen del microservicio transacciones
      docker_image:
        name: nsinductus/cc_proyecto:latest_transaciones
        source: pull
    #Tarea para crear el contenedor del microservicio Portatiles
    - name: Arrancar contenedor del microservicio portatiles
      docker_container:
        name: portatiles
        image: nsinductus/cc_proyecto:latest
        auto_remove: yes
        detach: yes
        published_ports: 8080:8080
        network_mode: host
        env:
          URI_BD_T: "{{ URI_BD_T }}"
          BD_T: "{{ BD_T }}"
          CO_T: "{{ CO_T }}"
          PORT_2: "{{ PORT_2 }}"
          URI_BD_P: "{{ URI_BD_P }}"
          BD_P: "{{ BD_P }}"
          CO_P: "{{ CO_P }}"
          PORT: "{{ PORT }}"
          HOST: "{{ HOST }}"
    #Tarea para crear el contenedor del microservicio Transacciones
    - name: Arrancar contenedor del microservicio transacciones
      docker_container:
        name: transaciones
        image: nsinductus/cc_proyecto:latest_transaciones
        auto_remove: yes
        detach: yes
        published_ports: 8000:8000
        network_mode: host
        env:
          URI_BD_T: "{{ URI_BD_T }}"
          BD_T: "{{ BD_T }}"
          CO_T: "{{ CO_T }}"
          PORT_2: "{{ PORT_2 }}"
          URI_BD_P: "{{ URI_BD_P }}"
          BD_P: "{{ BD_P }}"
          CO_P: "{{ CO_P }}"
          PORT: "{{ PORT }}"
          HOST: "{{ HOST }}"
```
En esta segunda parte se están definiendo las tareas a realizar, primero se actualizan los repositorios y se instala tanto Python3 como Pip3, para posteriormente utilizar docker para descargar las imágenes de los microservicios (disponibles en mi repositorio de dockerhub) y finalmente ser lanzados esos servicios utilizando las imágenes docker descargardas posteriormente.

*Como se puede ver, en esos docker se introducen variables de entorno que toman los valores que tenían en el fichero "./provision/env/env-file.yml"*
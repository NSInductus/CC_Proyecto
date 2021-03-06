from reportlab.pdfgen import canvas

#Clase Portatiles: contenedora de la lógica de negocio del microservicio Portatiles
class Portatiles:
    #Constructor
    def __init__ (self, data_manager):
        #Se inicializa con un data_manager
        self.data_manager = data_manager

    # Funcion para conseguir el número de portatiles existentes
    def numeroPortatilesEnBD(self):
        return self.data_manager.numero_elementos()

    #Funcion para agregar un portatil
    def agregarPortatil(self, marca, modelo, DNIvendedor, precio, comentario="", pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
        portatil = {"marca":marca,"modelo":modelo, "pantalla":pantalla, "procesador":procesador, "RAM":RAM, "almacenamiento":almacenamiento, "grafica":grafica, "bateria":bateria, "SO":SO, "DNIvendedor":DNIvendedor, "comentario":comentario, "precio":precio, "vendido": 0}
        _id = self.data_manager.insertar_elemento(portatil)
        return _id

    #Funcion para eliminar un portatil sabiendo su identificador (_id)
    def eliminarPortatilPorIdVenta(self, _id):
        existe = self.data_manager.obtener_elemento("_id", _id)
        if existe != False:
            self.data_manager.borrar_elemento(_id)
            return True
        else:
            return False

    #Funcion para modificar un portatil ya existente
    def modificarPortatil(self, _id, precio="", modelo="", marca="",comentario="",  pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
        portatil = self.data_manager.obtener_elemento("_id", _id)
        if portatil != False:
            if comentario == "":
                comentario = portatil.get("comentario")
            if precio == "":
                precio = portatil.get("precio")
            if pantalla == "":
                pantalla = portatil.get("pantalla")
            if procesador == "":
                procesador = portatil.get("procesador")
            if RAM == "":
                RAM = portatil.get("RAM")
            if almacenamiento == "":
                almacenamiento = portatil.get("almacenamiento")
            if grafica == "":
                grafica = portatil.get("grafica")
            if bateria == "":
                bateria = portatil.get("bateria")
            if SO == "":
                SO = portatil.get("SO")
            if marca == "":
                marca = portatil.get("marca")
            if modelo == "":
                modelo = portatil.get("modelo")
            dni = portatil.get("DNIvendedor")
            vendido = portatil.get("vendido")
            portatil_nuevo = {"marca":marca,"modelo":modelo, "pantalla":pantalla, "procesador":procesador, "RAM":RAM, "almacenamiento":almacenamiento, "grafica":grafica, "bateria":bateria, "SO":SO, "DNIvendedor":dni, "comentario":comentario, "precio":precio, "vendido": vendido}
            self.data_manager.actualizar_elemento(_id, portatil_nuevo)
            return True
        else:
            return False

    #Funcion solo para modificar el stock
    #Si se vende un portatil => vendido = 1
    #Si se devuelve un portatil => vendido = 0
    def cambiarStockPortatil(self, _id, vendido_nuevo):
        #existe = self.portatilEnListaIDventa(_id)
        portatil = self.data_manager.obtener_elemento("_id", _id)
        if portatil != False:
            comentario = portatil.get("comentario")
            precio = portatil.get("precio")
            pantalla = portatil.get("pantalla")
            procesador = portatil.get("procesador")
            RAM = portatil.get("RAM")
            almacenamiento = portatil.get("almacenamiento")
            grafica = portatil.get("grafica")
            bateria = portatil.get("bateria")
            SO = portatil.get("SO")
            marca = portatil.get("marca")
            modelo = portatil.get("modelo")
            dni = portatil.get("DNIvendedor")
            vendido = vendido_nuevo
            portatil_nuevo = {"marca":marca,"modelo":modelo, "pantalla":pantalla, "procesador":procesador, "RAM":RAM, "almacenamiento":almacenamiento, "grafica":grafica, "bateria":bateria, "SO":SO, "DNIvendedor":dni, "comentario":comentario, "precio":precio, "vendido":vendido_nuevo}
            self.data_manager.actualizar_elemento(_id, portatil_nuevo)
            return True
        else:
            return False

    #Funcion para seleccionar un portatil
    def seleccionarPortatil(self, _id):
        return self.data_manager.obtener_elemento("_id", _id)

    #Funcion para ver los portatiles que tiene a la venta un usuario sabiendo su DNI
    def buscarPortatilesEnVentaUsuario(self, DNIusuario):
        lista_portatiles = self.data_manager.obtener_todos_elementos()
        portatiles_usuario = []
        for i, portatil in enumerate(lista_portatiles):
            if (portatil.get("DNIvendedor") == DNIusuario) and (portatil.get("vendido") == 0):
                portatiles_usuario.append(portatil)
        return portatiles_usuario

    #Funcion para buscar portatiles por un rango de precios
    def buscarPortatilPorPrecio(self, limite_inferior, limite_superior):
        lista_portatiles = self.data_manager.obtener_todos_elementos()
        portatiles_busqueda = []
        for i, portatil in enumerate(lista_portatiles):
            if (portatil.get("precio") <= limite_superior) and (portatil.get("precio") >= limite_inferior) and (portatil.get("vendido") == 0):
                portatiles_busqueda.append(portatil)
        return portatiles_busqueda

    #Funcion para buscar portatiles por modelo, marca
    def buscarPortatilPorModeloMarca(self, modelo, marca):
        lista_portatiles = self.data_manager.obtener_todos_elementos()
        portatiles_busqueda = []
        for i, portatil in enumerate(lista_portatiles):
            if (portatil.get("modelo") == modelo) and (portatil.get("marca") == marca) and (portatil.get("vendido") == 0):
                portatiles_busqueda.append(portatil)
        return portatiles_busqueda

    #Funcion para comparar portatiles por modelo, marca
    #Te compara portatiles de la misma marca y modelo y te los ordena por precio
    def compararPortatiles(self, modelo, marca):
        lista_portatiles = self.data_manager.obtener_todos_elementos()
        portatiles_iguales = []
        for i, portatil in enumerate(lista_portatiles):
            if (portatil.get("modelo") == modelo) and (portatil.get("marca") == marca) and (portatil.get("vendido") == 0):
                portatiles_iguales.append(portatil)
        print(portatiles_iguales)
        if len(portatiles_iguales) >= 1:
            portatiles_iguales = sorted(portatiles_iguales, key=lambda k: k['precio'])
            return portatiles_iguales
        else:
            return False
    #Funcion para imprimir la comparacion en PDF
    def imprimirComparacion(self, vector_comparacion, ruta):
        c = canvas.Canvas(ruta)
        for i, portatil in enumerate(vector_comparacion):
            c.drawString(200, 10*(i+1), "Portatil: " + str(portatil.get("marca")) + " " + str(portatil.get("modelo")) + " " + str(portatil.get("pantalla")) + " " +portatil.get("procesador") + " " +str(portatil.get("RAM")) + " " +str(portatil.get("almacenamiento")) + " " +str(portatil.get("grafica")) + " " +str(portatil.get("bateria")) + " " +str(portatil.get("SO")) + " " +str(portatil.get("comentario")) + " " + str(portatil.get("precio")))
        c.save()

    def limpiarLista(self):
        self.data_manager.borrar_conjunto()

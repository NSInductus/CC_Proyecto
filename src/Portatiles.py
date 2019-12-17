class Portatiles:
    def __init__ (self):
        self.lista_portatiles = []
        self.indice = 1

    def numeroPortatilesEnVenta(self):
        return len(self.lista_portatiles)

    def agregarPortatil(self, marca, modelo, DNIvendedor, precio, comentario="", pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
        id_venta = self.indice
        self.indice = self.indice + 1
        portatil = {"IDventa":id_venta, "marca":marca,"modelo":modelo, "pantalla":pantalla, "procesador":procesador, "RAM":RAM, "almacenamiento":almacenamiento, "grafica":grafica, "bateria":bateria, "SO":SO, "DNIvendedor":DNIvendedor, "comentario":comentario, "precio":precio}
        self.lista_portatiles.append(portatil)
        return id_venta

    def existeEnListaIDventa(self, id_venta):
        for i, portatil in enumerate(self.lista_portatiles):
            if portatil.get("IDventa") == id_venta:
                return True
        return False

    def indiceEnListaIDventa(self, id_venta):
        existe = self.existeEnListaIDventa(id_venta)
        if existe != False:
            for i, portatil in enumerate(self.lista_portatiles):
                if portatil.get("IDventa") == id_venta:
                    return i
        return False

    def eliminarPortatilPorIdVenta(self, id_venta):
        existe = self.existeEnListaIDventa(id_venta)
        if existe != False:
            indice = self.indiceEnListaIDventa(id_venta)
            del(self.lista_portatiles[indice])
            return True
        else:
            return False

    def modificarPortatil(self, id_venta, precio="", modelo="", marca="",comentario="",  pantalla="", procesador="", RAM="", almacenamiento="", grafica="", bateria="", SO=""):
        existe = self.existeEnListaIDventa(id_venta)
        if existe != False:
            indice = self.indiceEnListaIDventa(id_venta)
            portatil = self.seleccionarPortatil(id_venta)
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
            self.eliminarPortatilPorIdVenta(id_venta)
            portatil_nuevo = {"IDventa":id_venta, "marca":marca,"modelo":modelo, "pantalla":pantalla, "procesador":procesador, "RAM":RAM, "almacenamiento":almacenamiento, "grafica":grafica, "bateria":bateria, "SO":SO, "DNIvendedor":dni, "comentario":comentario, "precio":precio}
            self.lista_portatiles.append(portatil_nuevo)
            return True
        else:
            return False

    def seleccionarPortatil(self, id_venta):
        existe = self.existeEnListaIDventa(id_venta)
        if existe != False:
            indice = self.indiceEnListaIDventa(id_venta)
            return self.lista_portatiles[indice]
        else:
            return False

    def portatiles_en_venta_de_usuario(self, DNIusuario):
        portatiles_usuario = []
        for i, portatil in enumerate(self.lista_portatiles):
            if portatil.get("DNIvendedor") == DNIusuario:
                portatiles_usuario.append(portatil)
        return portatiles_usuario

    def buscar_portatil_por_precio(self, limite_inferior, limite_superior):
        portatiles_busqueda = []
        for i, portatil in enumerate(self.lista_portatiles):
            if (portatil.get("precio") <= limite_superior) and (portatil.get("precio") >= limite_inferior):
                portatiles_busqueda.append(portatil)
        return portatiles_busqueda

    def buscar_portatil_por_modelo_marca(self, modelo, marca):
        portatiles_busqueda = []
        for i, portatil in enumerate(self.lista_portatiles):
            if (portatil.get("modelo") == modelo) and (portatil.get("marca") == marca):
                portatiles_busqueda.append(portatil)
        return portatiles_busqueda

    #Te compara portatiles de la misma marca y modelo y te los ordena por precio
    def comparar_portatiles(self, modelo, marca):
        portatiles_iguales = []
        for i, portatil in enumerate(self.lista_portatiles):
            if (portatil.get("modelo") == modelo) and (portatil.get("marca") == marca):
                portatiles_iguales.append(portatil)
        print(portatiles_iguales)
        if len(portatiles_iguales) >= 1:
            portatiles_iguales = sorted(portatiles_iguales, key=lambda k: k['precio'])
            return portatiles_iguales
        else:
            return False

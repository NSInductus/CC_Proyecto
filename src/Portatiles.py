class Portatiles:
    def __init__ (self):
        self.lista_portatiles = []
        self.indice = 1

    def numeroPortatilesEnVenta(self):
        return len(self.lista_portatiles)

    def agregarPortatil(self, marca, modelo, DNIvendedor, precio):
        id_venta = self.indice
        self.indice = self.indice + 1
        portatil = {"IDventa":id_venta, "marca":marca,"modelo":modelo,"DNIvendedor":DNIvendedor,"precio":precio}
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

    def modificarPortatil(self, id_venta,  precio="", modelo="", marca=""):
        existe = self.existeEnListaIDventa(id_venta)
        if existe != False:
            indice = self.indiceEnListaIDventa(id_venta)
            portatil = self.seleccionarPortatil(id_venta)
            if marca == "":
                marca = portatil.get("marca")
            if modelo == "":
                modelo = portatil.get("modelo")
            if precio == "":
                precio = portatil.get("precio")
            dni = portatil.get("DNIvendedor")
            self.eliminarPortatilPorIdVenta(id_venta)
            portatil_nuevo = {"IDventa":id_venta, "marca":marca,"modelo":modelo,"DNIvendedor":dni,"precio":precio}
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

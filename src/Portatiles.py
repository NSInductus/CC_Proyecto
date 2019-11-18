class Portatiles:
    def __init__ (self):
        self.lista_portatiles = []

    def numeroPortatilesEnVenta(self):
        return len(self.lista_portatiles)

    def agregarPortatil(self, marca, modelo, DNIvendedor, precio):
        id_venta = self.numeroPortatilesEnVenta()+1
        portatil = {"IDventa":id_venta, "marca":marca,"modelo":modelo,"DNIvendedor":DNIvendedor,"precio":precio}
        self.lista_portatiles.append(portatil)
        return id_venta

    def indiceEnListaIDventa(self, id_venta):
        indice = False
        for i, portatil in enumerate(self.lista_portatiles):
            if portatil.get("IDventa") == id_venta:
                return i
        return indice

    def eliminarPortatilPorIdVenta(self, id_venta):
        indice = self.indiceEnListaIDventa(id_venta)
        if indice != False:
            del(self.lista_portatiles[indice])
            return True
        else:
            return False

    def seleccionarPortatil(self, id_venta):
        indice = self.indiceEnListaIDventa(id_venta)
        if indice != False:
            return self.lista_portatiles[indice]
        else:
            return False

    def listar(self):
        for i in self.lista_portatiles:
            print(i)

class Portatiles:
    def __init__ (self):
        self.lista_portatiles = []

    def numeroPortatilesEnVenta(self):
        return len(self.lista_portatiles)

    def agregarPortatil(self, marca, modelo, DNIvendedor, precio):
        portatil = {"marca":marca,"modelo":modelo,"DNIvendedor":DNIvendedor,"precio":precio}
        self.lista_portatiles.append(portatil)
        id = numeroPortatilesEnVenta(self)
        return id

    def eliminarPortatilPorId(self, id):
        if id >= numeroPortatilesEnVenta():
            del(self.lista_portatiles[id])
            return true
        else:
            return false

    def seleccionarPortatil(self, id):
        if id >= numeroPortatilesEnVenta():
            return self.lista_portatiles[id]
        else:
            return false

    def listar(self):
        for i in self.lista_portatiles:
            print(i)

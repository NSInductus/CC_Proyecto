class Portatiles:
    def __init__ (self):
        self.lista_portatiles = []

    def agregarPortatil(self, marca, modelo, DNIvendedor, precio):
        portatil = {marca=marca;modelo=modelo;DNIvendedor=DNIvendedor;precio=precio}
        self.lista_portatiles.append(portatil)

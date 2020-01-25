from reportlab.pdfgen import canvas
import bson

class Transaciones:
    def __init__ (self, data_manager):
        self.data_manager  = data_manager

    def numeroTransaciones(self):
        return self.data_manager.numero_elementos()

    #Tipo 1 => Transacion de compra
    #Tipo 2 => Transacion de venta
    #Tipo 3 => Transacion de devolucion
    def agregarTransacion(self, id_portatil, DNIusuario, tipo, comentario=""):
        transacion = {"id_portatil":id_portatil,"DNIusuario":DNIusuario, "tipo":tipo, "comentario":comentario}
        id_transacion = self.data_manager.insertar_elemento(transacion)
        return id_transacion

    def seleccionarTransacion(self, id_transacion):
        return self.data_manager.obtener_elemento("_id", id_transacion)

    def eliminarTransacion(self, id_transacion):
        existe = self.data_manager.obtener_elemento("_id", id_transacion)
        if existe != False:
            self.data_manager.borrar_elemento(id_transacion)
            return True
        else:
             return False

    def verEstadisticas(self, DNIusuario):
        lista_transaciones = self.data_manager.obtener_todos_elementos()
        transaciones_usuario = []
        for i, transacion in enumerate(lista_transaciones):
            if transacion.get("DNIusuario") == DNIusuario:
                transaciones_usuario.append(transacion)
        return transaciones_usuario

    def verEstadisticasFiltradasTipo(self, DNIusuario, tipo):
        lista_transaciones = self.data_manager.obtener_todos_elementos()
        transaciones_usuario = []
        for i, transacion in enumerate(lista_transaciones):
            if (transacion.get("DNIusuario") == DNIusuario) and (transacion.get("tipo") == tipo):
                transaciones_usuario.append(transacion)
        return transaciones_usuario

    def imprimirComparacion(self, vector_comparacion, ruta):
            c = canvas.Canvas(ruta)
            for i, portatil in enumerate(vector_comparacion):
                c.drawString(200, 10*(i+1), "Transacion: " + str(portatil.get("id_portatil")) + " " + str(portatil.get("DNIusuario")) + " " + str(portatil.get("tipo")) + " " + portatil.get("comentario") )
            c.save()

    def limpiarLista(self):
        self.data_manager.borrar_conjunto()

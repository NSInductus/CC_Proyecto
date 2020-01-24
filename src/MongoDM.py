import pymongo
import bson

#Mi clase Data Manager con MongoBD
class MongoDM:
    #Constructor
    def __init__(self, uri, basedatos, coleccion):
        #Conexión con la base de datos
        self.cliente = pymongo.MongoClient(uri)
        #Conexión con la colección de datos
        self.coleccion = self.cliente[basedatos][coleccion]

    #Obtener un elemento, suele usarse para buscar por identificador
    def obtener_elemento(self, campo, valor):
        #Ver si se busca por _id para tratarlo con ObjectId
        if campo == "_id":
            try:
                salida = self.coleccion.find_one({campo:bson.ObjectId(valor)})
            #Controlar una clave no valida
            except bson.errors.InvalidId as error:
                salida = False
        #Sino buscar normal
        else:
            salida = self.coleccion.find_one({campo:valor})
        return salida

    #Obtener varios elementos
    def obtener_conjunto_elementos(self, campo, valor):
        elementos = self.coleccion.find({campo:valor})
        conjunto = []
        for elemento in elementos:
            conjunto.append(elemento)
        return conjunto

    #Obtener todos los elementos
    def obtener_todos_elementos(self):
        elementos = self.coleccion.find()
        conjunto = []
        for elemento in elementos:
            conjunto.append(elemento)
        return conjunto

    #Insertar un elemento
    def insertar_elemento(self, elemento):
        #Inserta el id en forma de ObjectId automaticamente
        _id = self.coleccion.insert_one(elemento.copy()).inserted_id
        return str(_id)

    #Actualizar un elemento
    def actualizar_elemento(self, id, nuevo):
        #Introducion de campo a modificar
        elemento_nuevo = {"$set":nuevo}
        #utilizo ObjectId puesto que mongo por defecto mete asi los identificadores
        self.coleccion.update_one({"_id":bson.ObjectId(id)},elemento_nuevo)

    #Borrar un elemento
    def borrar_elemento(self,id):
        self.coleccion.delete_one({"_id":bson.ObjectId(id)})

    #Obtener numero de elementos
    def numero_elementos(self):
        lista_portatiles = self.obtener_todos_elementos()
        return len(lista_portatiles)

    #Borra la coleccion completa
    def borrar_conjunto(self):
        self.coleccion.drop()

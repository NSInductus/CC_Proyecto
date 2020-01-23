import pymongo
import bson

class MongoDM:
    def __init__(self, uri, basedatos, coleccion):
        #Conexión con la base de datos
        self.cliente = pymongo.MongoClient(uri)
        #Conexión con la colección de datos
        self.coleccion = self.cliente[basedatos][coleccion]

    def insertar_elemento(self, elemento):
        _id = self.coleccion.insert_one(elemento.copy()).inserted_id
        return str(_id)

        

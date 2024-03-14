#import json
import requests

def getAllGama():
        #json-server storage/gama_producto.json -b 3000/0
        peticion = requests.get("http://172.16.106.94:3000/0")
        data = peticion.json()
        return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre
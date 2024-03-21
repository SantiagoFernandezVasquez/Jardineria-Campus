import os
from tabulate import tabulate
import requests

def clear():
    os.system('cls')
clear()

def  getAllOficinas():
     petition = requests.get('http://localhost:5002/oficinas')
     data = petition.json()
     return data

def getAllOficinasTelefono(telefono):
     for val in getAllOficinas():
        if(val.get('telefono') == telefono):
            return[val]  

def getAllOficinaCodigo(codigo):
    for val in getAllOficinas():
        if(val.get('codigo_cliente') == codigo):
            return[val]
    
def getAllOficinaId(id): 
    for val in getAllOficinas():
        if(val.get('id') == id):
            return[val]
def getAllCodigoCiudad():
    codigoCiudad = list()
    for val in getAllOficinas():
        codigoCiudad.append({
            "Codigo_oficina": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad") 
        }) 
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in getAllOficinas():
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "Ciudad": val.get("ciudad"),
                "Telefono": val.get("telefono"),
                "Oficinas": val.get("codigo_oficina"),
                "Pais": val.get("pais")
            })
        return ciudadTelefono
        
def menu():
    while True:
        clear()
        print("""
  ___                  _               _            __ _    _           
 | _ \___ _ __ ___ _ _| |_ ___ ___  __| |___   ___ / _(_)__(_)_ _  __ _ 
 |   / -_| '_ / _ | '_|  _/ -_(_-< / _` / -_) / _ |  _| / _| | ' \/ _` |
 |_|_\___| .__\___|_|  \__\___/__/ \__,_\___| \___|_| |_\__|_|_||_\__,_|
         |_|                                                            

    1. Obtener las ubicaciones de una oficina en determinada ciudad 
    2. Obtener los datos las oficinas en un pais (pais)
    3. Regresar al Menu Principal
""")
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if(opcion == 1):
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif(opcion == 2):
            pais = str(input("Ingrese el pais: "))
            print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif opcion == 3:
            break


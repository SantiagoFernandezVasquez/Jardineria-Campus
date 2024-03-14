import os
from tabulate import tabulate
import requests

def  getAllOficinas():
     petition = requests.get('http://172.16.106.94:3000/0')
     data = petition.json()
     return data

def getAllCodigoCiudad():
    codigoCiudad = list()
    for val in getAllOficinas.oficina:
        codigoCiudad.append({
            "Codigo_oficina": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad") 
        }) 
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in getAllOficinas.oficina:
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
        elif(opcion == 2):
                pais = str(input("Ingrese el pais: "))
                print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="fancy_grid"))
            
        elif opcion == 3:
            break


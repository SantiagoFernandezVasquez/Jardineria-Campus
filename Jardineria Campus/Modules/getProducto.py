import os
from tabulate import tabulate
import requests

def clear():
    os.system('cls')
clear()

def GetAllData():
    peticion = requests.get('http://localhost:3000/productos')
    data = peticion.json()
    return data

def getAllProductoCodigo(codigo):
    for val in GetAllData():
        if(val.get('codigo_producto') == codigo):
            return[val]

def getAllProductoCodigo(codigo):
    for val in GetAllData():
        if(val.get('codigo_producto') == codigo):
            return[val]
        
def getAllStocksPrecioGama(gama, stock):
    condiciones = []
    for val in GetAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
            def Price(val):
                return val.get("precio_venta")
            condiciones.sort(key=Price)
    for i, val in enumerate(condiciones):
            condiciones[i] = {
                "Codigo": val.get("codigo_producto"),
                "Venta": val.get("precio_venta"),
                "Nombre": val.get("nombre"),
                "Gama": val.get("gama"),
                "Dimensiones": val.get("dimensiones"),
                "Proveedor": val.get("proveedor"),
                "Descripcion": val.get("descripcion"),
                "Stock": val.get("cantidad_en_stock"),
                "Base": val.get("precio_proveedor"),
                }
    return condiciones

def getProductoCodigo(codigo):
    peticion = requests.get(f"http:localhost:3000/productos/{codigo}")
    return[peticion.json()] if peticion.ok  else[]
def menu():
    while True:
        clear()
        print("""
  ___                  _               _       ___            _         _          
 | _ \___ _ __ ___ _ _| |_ ___ ___  __| |___  | _ \_ _ ___ __| |_  _ __| |_ ___ ___
 |   / -_| '_ / _ | '_|  _/ -_(_-< / _` / -_) |  _| '_/ _ / _` | || / _|  _/ _ (_-<
 |_|_\___| .__\___|_|  \__\___/__/ \__,_\___| |_| |_| \___\__,_|\_,_\__|\__\___/__/
         |_|                                                                       

              1. Obtener los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea superior
              2. Regresar al Menu Principal
 """)
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            gama = input("Ingrese la gama del producto: ")
            stock = int(input("Ingrese las unidades del producto que desea mostrar: "))
            print(tabulate(getAllStocksPrecioGama(gama, stock), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 2:
            break

        
import os
from tabulate import tabulate
import json
import requests

def postProducto():
    # json-server storage/producto.json -b 5501
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": input("Ingrese el gama del producto: "),
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    }
    
    peticion = requests.post("http://172.16.106.94:3000/0", data=json.dumps(producto))
    respuesta = peticion.json()
    respuesta["Mensaje"] = "Producto Guardado"
    return [respuesta]

def menu():
    while True:
        os.system("clear")
        print("""
    _      _       _      _    _                     _      _               _                       _         _          
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___   _ __ _ _ ___ __| |_  _ __| |_ ___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) | '_ | '_/ _ / _` | || / _|  _/ _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| | .__|_| \___\__,_|\_,_\__|\__\___/__/
                                                                                   |_|                               
              1. Guardar un producto nuevo
              2. Regresar al menu de productos
 """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if opcion == 1:
            print(tabulate(postProducto(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif opcion == 2:
            break
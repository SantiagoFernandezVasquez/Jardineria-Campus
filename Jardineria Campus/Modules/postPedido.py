import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getPedido as gP

def postPedido():
    # json-server storage/producto.json -b 5501
    pedidos = dict()
    while True:
        try:
            if(not pedidos.get("codigo_pedido")):
                codigo = input("Ingrese el codigo del pedido: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                    data = gP.getAllEmpleadoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo del pedido ya existe")
                    else:
                        pedidos["codigo_pedido"] = codigo
                else: 
                    raise Exception("El codigo del pedido no es valido")
                
            if(not pedidos.get("nombre")):
                nombre = input("Ingrese el nombre del empleado: ")
                if(re.match(r'^[A-Z][a-z]*\s*)+$', nombre) is not None):
                    pedidos["nombre"] = nombre
                    break
                else: 
                    raise Exception("El nombre del pedido no es valido")
                
        except Exception as error:
            print(error)

    print(pedidos)

def menu():
    while True:
        os.system("clear")
        print("""
    _      _       _      _    _                     _      _               _       ___        _ _    _        
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___  | _ \___ __| (_)__| |___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) |  _/ -_/ _` | / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| |_| \___\__,_|_\__,_\___/__/

              1. Ingresar los datos de un pedido nuevo
              2. Regresar al menu principal       
 """)
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            print(tabulate(postPedido(), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 2:
            break
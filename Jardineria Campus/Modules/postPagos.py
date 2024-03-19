import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getPagos as gP

def postPagos():
    # json-server storage/producto.json -b 5501
    pagos = dict()
    while True:
        try:
            if(not pagos.get("codigo_cliente")):
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                    data = gP.getAllproductoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo del cliente ya existe")
                    else:
                        pagos["codigo_cliente"] = codigo
                else: 
                    raise Exception("El codigo del cliente no es valido")
                
            if(not pagos.get("forma_pago")):
                formapago = input("Ingrese la forma de pago: ")
                if(re.match(r'^[A-Z][a-z]*\s*)+$', formapago) is not None):
                    pagos["forma_pago"] = formapago
                    break
                else: 
                    raise Exception("El nombre del cliente no es valido")
                
        except Exception as error:
            print(error)

    print(pagos)

def menu():
    while True:
        print("""
    _      _       _      _    _                     _      _               _       ___                  
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___  | _ \__ _ __ _ ___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) |  _/ _` / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| |_| \__,_\__, \___/__/
                                                                                            |___/       
                            1. Ingresar los datos de un pago nuevo
                            2. Regresar al menu principal
 """)
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            print(tabulate(postPagos(), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 2:
            break
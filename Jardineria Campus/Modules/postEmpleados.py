import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getEmpleados as gE

def postEmpleados():
    # json-server storage/producto.json -b 5501
    empleados = dict()
    while True:
        try:
            if(not empleados.get("codigo_empleado")):
                codigo = input("Ingrese el codigo del empleado: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                    data = gE.getAllEmpleadoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo del empleado ya existe")
                    else:
                        empleados["codigo_cliente"] = codigo
                else: 
                    raise Exception("El codigo del empleado no es valido")
                
            if(not empleados.get("nombre")):
                nombre = input("Ingrese el nombre del empleado: ")
                if(re.match(r'^[A-Z][a-z]*\s*)+$', nombre) is not None):
                    empleados["nombre"] = nombre
                    break
                else: 
                    raise Exception("El nombre del empleado no es valido")
                
        except Exception as error:
            print(error)

    print(empleados)

def menu():
    while True:
        print("""
    _      _       _      _    _                     _      _               _       ___            _             _        
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___  | __|_ __  _ __| |___ __ _ __| |___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) | _|| '  \| '_ | / -_/ _` / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| |___|_|_|_| .__|_\___\__,_\__,_\___/__/
                                                                                             |_| 
                                    1. Ingresar los datos de un empleado nuevo
                                    2. Regresar al menu principal
 """)
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            print(tabulate(postEmpleados(), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 2:
            break
        

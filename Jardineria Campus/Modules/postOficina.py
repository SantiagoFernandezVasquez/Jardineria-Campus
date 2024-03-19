import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getOficina as gO

def clear():
    os.system('cls')
clear()
def postOficina():
    # json-server storage/producto.json -b 5501
    oficina = dict()
    while True:
        try:
            if(not oficina.get("codigo_oficina")):
                codigo = input("Ingrese el codigo de la oficina: ")
                if(re.match(r'^[A-Z]{3}-[A-Z]{1,3}$', codigo)is not None):
                    data = gO.getAllOficinaCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo de la oficina ya existe")
                    else:
                        oficina["codigo_oficina"] = codigo
                else: 
                    raise Exception("El codigo de la oficina no es valido")
                
            if not oficina.get("ciudad"):
                ciudad = input("Ingrese la ciudad de la oficina: ")
                if re.match(r'^([A-Za-z]\s*)+$', ciudad) is not None:
                    oficina["Ciudad"]=ciudad
                else:
                    raise Exception ("La ciudad de la oficina no es valida")
                
            if not oficina.get("pais"):
                pais = input("Ingrese el pais de la oficina: ")
                if re.match(r'^([A-Za-z]\s*)+$', pais) is not None:
                    oficina["Pais"]=pais
                else:
                    raise Exception ("El pais de la oficina no es valida")
                
            if not oficina.get("region"):
                region = input("Ingrese la region de la oficina: ")
                if re.match(r'^([A-Za-z]\s*)+$', region) is not None:
                    oficina["Region"]=region
                else:
                    raise Exception ("La region de la oficina no es valida")
                
            if not oficina.get("codigo_postal"):
                codigopostal = input("Ingrese el codigo postal: de la oficina ")
                if re.match(r'^\d{5,7}$', codigopostal) is not None:
                    oficina["Codigo Postal"] = codigopostal
                else:
                    raise Exception ("El codigo postal de la oficina no es valido")
                
            if not oficina.get("telefono"):
                telefono = input("Ingrese el telefono de la oficina: ")
                if re.match(r'^\d{1,3}(?: ?\d{4}-?\d{4}|\s?\d{6,11})$', telefono) is not None:
                    data= gO.getAllOficinasTelefono(telefono)
                    if(data): 
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El telefono de la oficina ya existe")
                    else:
                        oficina["Telefono"] = telefono
                else:
                    raise Exception ("El telefono de la oficina no es valido")
                         
            if not oficina.get("linea_direccion1"):
                direccion1 = input("Ingrese la direccion 1 de la oficina: ")
                if re.match(r'^[A-Za-z0-9\s\-,.#]+[A-Za-z0-9\s\-,.#]*$', direccion1) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion 1 de la oficina ya existe")
                    else:
                        oficina["Linea Direccion1"] = direccion1
                else:
                    raise Exception ("La direccion 1 de la oficina no es valida")
            
            if not oficina.get("linea_direccion2"):
                direccion2 = input("Ingrese la direccion 2 de la oficina: ")
                if re.match(r'^[A-Za-z0-9\s\-,.#]+[A-Za-z0-9\s\-,.#]*$', direccion2) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion 2 de la oficina ya existe")
                    else:
                        oficina["Linea Direccion2"] = direccion2
                        break
                else:
                    raise Exception ("La direccion 2 de la oficina no es valida")

        except Exception as error:
            print(error)        

    peticion = requests.post("http://localhost:3000/oficinas", data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"]= "Oficina Guardada"
    return [res]

def menu():
    while True:
        clear()
        print("""
    _      _       _      _    _                     _      _               _        ___   __ _    _           
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___   / _ \ / _(_)__(_)_ _  __ _ 
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) | (_) |  _| / _| | ' \/ _` |
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___|  \___/|_| |_\__|_|_||_\__,_|
                                                                                                               
                            1. Ingresar los datos de una oficina nueva
                            2. Regresar al menu principal                                                    
 """)
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            print(tabulate(postOficina(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una tecla para continuar.....")
        elif opcion == 2:
            break
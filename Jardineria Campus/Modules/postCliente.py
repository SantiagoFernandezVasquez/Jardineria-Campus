import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getClientes as gC

def clear():
    os.system('cls')
clear()


def postCliente():
    cliente = dict()
    while True:
        try:
            if(not cliente.get("codigo_cliente")):
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]+$', codigo)is not None):
                    codigo = int(codigo)
                    data = gC.getAllClienteCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo del cliente ya existe")
                    else:
                        cliente["Codigo Cliente"] = codigo
                else: 
                    raise Exception("El codigo del cliente no es valido")
                
            if not cliente.get("nombre_cliente"):
                nombre = input("Ingrese el nombre del cliente: ")
                if re.match(r'^[A-Z][a-z]*\s*[A-Z]*[a-z]*$', nombre) is not None:
                    cliente["Nombre Cliente"] = nombre
                else: 
                    raise Exception("El nombre del cliente no es valido")

                
            if not cliente.get("nombre_contacto"):
                nombrecontacto = input("Ingrese el nombre de contacto del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', nombrecontacto) is not None:
                    cliente["Nombre Contacto"] = nombrecontacto
                else:
                    raise Exception ("El nombre de contacto del cliente no es valido")
                
            if not cliente.get("apellido_contacto"):
                apellidocontacto = input("Ingrese el apellido de contacto del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', apellidocontacto) is not None:
                    cliente["Apellido Contacto"] = apellidocontacto
                else:
                    raise Exception ("El apellido de contacto del cliente no es valido")
                
            if not cliente.get("telefono"):
                telefono = input("Ingrese el telefono del cliente: ")
                if re.match(r'^\d{1,3}(?: ?\d{4}-?\d{4}|\s?\d{6,11})$', telefono) is not None:
                    data= gC.getAllClientTelefono(telefono)
                    if(data): 
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El telefono del cliente ya existe")
                    else:
                        cliente["Telefono"] = telefono
                else:
                    raise Exception ("El telefono del cliente no es valido")
                
            if not cliente.get("fax"):
                fax = input("Ingrese el fax del cliente: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', fax) is not None: 
                    cliente["Fax"] = fax
                    
                else:
                    raise Exception ("El fax del cliente no es valido")
            
                         
            if not cliente.get("linea_direccion1"):
                direccion1 = input("Ingrese la direccion 1 del cliente: ")
                if re.match(r'^[A-Za-z0-9\s\-,.#]+[A-Za-z0-9\s\-,.#]*$', direccion1) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion 1 del cliente ya existe")
                    else:
                        cliente["Linea Direccion1"] = direccion1
                else:
                    raise Exception ("La direccion 1 del cliente no es valida")
            
            if not cliente.get("linea_direccion2"):
                direccion2 = input("Ingrese la direccion 2 del cliente: ")
                if re.match(r'^[A-Za-z0-9\s\-,.#]+[A-Za-z0-9\s\-,.#]*$', direccion2) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion 2 del cliente ya existe")
                    else:
                        cliente["Linea Direccion2"] = direccion2
                else:
                    raise Exception ("La direccion 2 del cliente no es valida")
                
            if not cliente.get("ciudad"):
                ciudad = input("Ingrese la ciudad del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', ciudad) is not None:
                    cliente["Ciudad"]=ciudad
                else:
                    raise Exception ("La ciudad del cliente no es valida")
                
            if not cliente.get("region"):
                region = input("Ingrese la region del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', region) is not None:
                    cliente["Region"]=region
                else:
                    raise Exception ("La region del cliente no es valida")
                
            if not cliente.get("pais"):
                pais = input("Ingrese el pais del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', pais) is not None:
                    cliente["Pais"]=pais
                else:
                    raise Exception ("El pais del cliente no es valida")
                        
            if not cliente.get("codigo_postal"):
                codigopostal = input("Ingrese el codigo postal del cliente: ")
                if re.match(r'^\d{5,7}$', codigopostal) is not None:
                    cliente["Codigo Postal"] = codigopostal
                else:
                    raise Exception ("El codigo postal del cliente no es valido")
                
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigorepventas = input("Ingrese el codigo del representante de ventas: ")
                if re.match(r'^[0-9]+$', codigorepventas) is not None:
                    codigorepventas = int(codigorepventas)
                    cliente["Codigo Empleado Rep Ventas"]=codigorepventas
                else:
                    raise Exception ("El codigo del empleado no es valido")
                        
            if not cliente.get("limite_credito"):
                limitecredito = input("Ingrese el limite de credito del cliente: ")
                if re.match(r'^\d+(\.\d+)?$', limitecredito) is not None:
                    limitecredito = float(limitecredito)
                    cliente["Limite Credito"]=limitecredito
                    break

                else:
                    raise Exception ("El codigo del empleado no es valido")
                
        except Exception as error:
            print(error)        

    peticion = requests.post("http://localhost:3000/clientes", data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"]= "Cliente Guardado"
    return [res]

def borrarCliente(id):
    data = gC.getAllClienteId(id)
    if (len(data)):
        peticion = requests.delete(f"http://localhost:3000/clientes/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Producto eliminado"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "message": "Producto no encontrado",
                    "id": id
            }],
            "status": 400,
        }

def menu():
    while True:
        clear()
        print("""
    _      _       _      _    _                     _      _               _                      _ _         _       
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___   _  _ _ _    __| (_)___ _ _| |_ ___ 
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) | || | ' \  / _| | / -_| ' |  _/ -_)
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___|  \_,_|_||_| \__|_|_\___|_||_\__\___|

              1. Ingresar los datos de un cliente nuevo   
              2. Eliminar un cliente                                                     
              3. Regresar al menu de clientes
""")  
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            print(tabulate(postCliente(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una tecla para continuar.....")
        elif opcion == 2:
            id = input("Ingrese el id del cliente que desea eliminar: ")
            print(tabulate(borrarCliente(id), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 3:
            break
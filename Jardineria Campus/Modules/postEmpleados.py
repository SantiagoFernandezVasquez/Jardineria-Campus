import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getEmpleados as gE

def clear():
    os.system('cls')
clear()

def postEmpleados():
    # json-server storage/producto.json -b 5501
    empleados = dict()
    while True:
        try:
            if(not empleados.get("codigo_empleado")):
                codigo = input("Ingrese el codigo del empleado: ")
                if(re.match(r'^[0-9]*\s*$', codigo)is not None):
                    data = gE.getAllEmpleadoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo del empleado ya existe")
                    else:
                        empleados["Codigo Empleado"] = len(codigo)
                else: 
                    raise Exception("El codigo del empleado no es valido")
                
            if not empleados.get("nombre"):
                nombre = input("Ingrese el nombre del empleado: ")
                if re.match(r'^[A-Z][a-z]*\s*[A-Z]*[a-z]*$', nombre) is not None:
                    empleados["Nombre"] = nombre
                else: 
                    raise Exception("El nombre del empleado no es valido")
            
            if not empleados.get("apellido1"):
                apellidocontacto = input("Ingrese el primer apellido del empleado: ")
                if re.match(r'^([A-Za-z]\s*)+$', apellidocontacto) is not None:
                    empleados["Apellido1 Contacto"] = apellidocontacto
                else:
                    raise Exception ("El primer apellido del empleado no es valido")
            
            if not empleados.get("apellido2"):
                apellidocontacto = input("Ingrese el segundo apellido del empleado: ")
                if re.match(r'^([A-Za-z]\s*)+$', apellidocontacto) is not None:
                    empleados["Apellido2 Contacto"] = apellidocontacto
                else:
                    raise Exception ("El segundo apellido del empleado no es valido")
            
            if not empleados.get("extension"):
                extension = input("Ingrese la extension del empleado: ")
                if re.match(r'^[0-9]+$', extension)is not None:
                    empleados["Extension"] = extension
                else: 
                    raise Exception("La extension del empleado no es valida")
            
            if not empleados.get("email"):
                email = input("Ingrese el email del empleado: ")
                if re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', email) is not None:
                    empleados["Email"] = email
                else:
                    raise Exception("El email del empleado no es valido")
                
            if not empleados.get("codigo_oficina"):
                codigo = input("Ingrese el codigo de la oficina: ")
                if re.match(r'^[A-Z]{3}-[A-Z]{1,3}$', codigo)is not None:
                        empleados["Codigo Oficina"] = codigo
                else: 
                    raise Exception("El codigo de la oficina no es valido")
                
            if not empleados.get("codigo_jefe"):
                codigojefe = input("Ingrese el codigo de jefe: ")
                if re.match(r'^[0-9]*\s*$', codigojefe)is not None:
                    empleados["Codigo Jefe"] = len(codigojefe)
                else:
                    raise Exception("El codigo de jefe no es valido")
            
            if not empleados.get("puesto"):
                puesto = input("Ingrese el puesto del empleado: ")
                if re.match(r'^[A-Z][a-z]*\s*[A-Z]*[a-z]*$', puesto) is not None:
                    empleados["Puesto"] = puesto
                    break
                else: 
                    raise Exception("El puesto del empleado no es valido")

        except Exception as error:
            print(error)

    peticion = requests.post("http://localhost:5003/empleados", data=json.dumps(empleados))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

def borrarEmpleado(id):
    data = gE.getAllEmpleadoId(id)
    if (len(data)):
        peticion = requests.delete(f"http://localhost:5003/empleados/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Empleado eliminado"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
        else:
            return {
                "body":[{
                    "message": "Empleado no encontrado",
                    "id": id
                }],
                "status": 400,
            }

def menu():
    while True:
        clear()
        print("""
    _      _       _      _    _                     _      _               _       ___            _             _        
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___  | __|_ __  _ __| |___ __ _ __| |___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) | _|| '  \| '_ | / -_/ _` / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| |___|_|_|_| .__|_\___\__,_\__,_\___/__/
                                                                                             |_| 
                                    1. Ingresar los datos de un empleado nuevo
                                    2. Eliminar un empleado
                                    3. Regresar al menu principal
 """)
        opcion = (input("\nSeleccione la opcion que le gustaria realizar: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            print(tabulate(postEmpleados(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una tecla para continuar.....")
        if opcion == 2:
            id = input("Ingrese el id del empleado: ")
            print(borrarEmpleado(id))
            input("Presione una tecla para continuar.....")
        elif opcion == 3:
            break

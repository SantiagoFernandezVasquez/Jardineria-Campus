import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getPagos as gP

def clear():
    os.system('cls')
clear()

def postPagos():
    pagos = {}
    while True:
        try:
            if not pagos.get("codigo_cliente"):
                codigo = input("Ingrese el código del cliente: ")
                if re.match(r'^\d+$', codigo) is not None:
                    pagos["codigo_cliente"] = len(codigo)
                else: 
                    raise Exception("El código del cliente no es válido")
                
            if not pagos.get("forma_pago"):
                formapago = input("Ingrese la forma de pago: ")
                if re.match(r'^[A-Za-z\s]+$', formapago) is not None:
                    pagos["forma_pago"] = formapago
                else: 
                    raise Exception("La forma de pago no es válida")
                
            if not pagos.get("id_transaccion"):
                transaccion = input("Ingrese el id de la transacción: ")
                if re.match(r'^[A-Za-z0-9-]+$', transaccion) is not None:
                    pagos["id_transaccion"] = transaccion
                else:
                    raise Exception("El id de la transacción no es válido")
                
            if not pagos.get("fecha_pago"):
                fechapago = input("Ingrese la fecha de pago (YYYY-MM-DD): ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$', fechapago) is not None:
                    pagos["fecha_pago"] = fechapago
                else:
                    raise Exception("La fecha de pago no es válida")
                
            if not pagos.get("total"):
                total = input("Ingrese el total del pago: ")
                if re.match(r'^\d+$', total) is not None:
                    pagos["total"] = total
                    break
                else: 
                    raise Exception("El total del pago no es válido")
                
        except Exception as error:
            print(error)

    peticion = requests.post("http://localhost:5005/pagos", data=json.dumps(pagos))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]

def borrarPago(id):
    data = gP.getAllPagosId(id)
    if (len(data)):
        peticion = requests.delete(f"http://localhost:5005/pagos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Pago eliminado"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
        else:
            return {
                "body": [{
                    "mensaje": "Pago no encontrado",
                    "id": id
                }],
                "status": 400
            }
def menu():
    while True:
        clear()
        print("""
    _      _       _      _    _                     _      _               _       ___                  
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___  | _ \__ _ __ _ ___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) |  _/ _` / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| |_| \__,_\__, \___/__/
                                                                                            |___/       
                            1. Ingresar los datos de un pago nuevo
                            2. Eliminar un pago
                            3. Regresar al menu principal
 """)
        opcion = (input("\nSeleccione la opcion que le gustaria realizar: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            print(tabulate(postPagos(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una tecla para continuar.....")
        elif opcion == 2:
            id = input("Ingrese el id del pago que desea eliminar: ")
            print(borrarPago(id))
            input("Presione una tecla para continuar.....")
        elif opcion == 3:
            break
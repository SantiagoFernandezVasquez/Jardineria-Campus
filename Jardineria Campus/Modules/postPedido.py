import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getPedido as gP

def clear():
    os.system('cls')
clear() 

def postPedido():
    # json-server storage/producto.json -b 5501
    pedidos = dict()
    while True:
        try:
            if(not pedidos.get("codigo_pedido")):
                codigo = input("Ingrese el codigo del pedido: ")
                if(re.match(r'^\d+$', codigo)is not None):
                    data = gP.getAllPedidosCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo del pedido ya existe")
                    else:
                        pedidos["codigo_pedido"] = len(codigo)
                else: 
                    raise Exception("El codigo del pedido no es valido")
                
            if not pedidos.get("fecha_pedido"):
                fechapedido = input("Ingrese la fecha del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$', fechapedido) is not None:
                    pedidos["fecha_pedido"] = fechapedido
                else: 
                    raise Exception("La fecha del pedido no es valido")
            
            if not pedidos.get("fecha_esperada"):
                fechaesperada = input("Ingrese la fecha de espera del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$', fechaesperada) is not None:
                    pedidos["fecha_esperada"] = fechaesperada
                else: 
                    raise Exception("La fecha de espera del pedido no es valido")
                
            if not pedidos.get("fecha_entrega"):
                fechaentrega = input("Ingrese la fecha de entrega del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$', fechaentrega) is not None:
                    pedidos["fecha_entrega"] = fechaentrega
                else: 
                    raise Exception("La fecha de entrega del pedido no es valido")
                
            if not pedidos.get("estado"):
                estado = input("Ingrese el estado del pedido: ")
                if re.match(r'^[A-Za-z\s]+$', estado) is not None:
                    pedidos["estado"] = estado
                else: 
                    raise Exception("El estado del pedido no es valido")
            
            if not pedidos.get("comentario"):
                comentario = input("Ingrese algun comentario que desee del pedido: ")
                if re.match(r'^[A-Z][a-z]*\s*[a-z]*$', comentario) is not None:
                    pedidos["comentario"] = comentario
                else:
                    raise Exception("El comentario del pedido no es valido")
                
            if not pedidos.get("codigo_cliente"):
                codigocliente = input("Ingrese el codigo del cliente")
                if re.match(r'^\d+$', codigocliente) is not None:
                    pedidos["codigo_cliente"] = len(codigo)
                    break
                else: 
                    raise Exception("El codigo del cliente no es valido")
                
        except Exception as error:
            print(error)

    peticion = requests.post("http://localhost:5004/pedidos", data=json.dumps(pedidos))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]


def borrarCliente(id):
    data = gP.getAllPedidosId(id)
    if (len(data)):
        peticion = requests.delete(f"http://localhost:5004/pedidos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Pedido eliminado"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
        else:
            return {
                "body":[{
                    "message": "Pedido no encontrado",
                    "id": id
                }],
                "status": 400,
            }
        
def menu():
    while True:
        clear()
        print("""
    _      _       _      _    _                     _      _               _       ___        _ _    _        
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___  | _ \___ __| (_)__| |___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) |  _/ -_/ _` | / _` / _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| |_| \___\__,_|_\__,_\___/__/

              1. Ingresar los datos de un pedido nuevo
              2. Eliminar un pedido      
              3. Regresar al menu principal
 """)
        opcion = (input("\nSeleccione la opcion que le gustaria realizar: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            print(tabulate(postPedido(), headers="keys", tablefmt="fancy_grid"))
        elif opcion == 2:
            id = input("Ingrese el id del pedido que desea eliminar: ")
            print(borrarCliente(id))
        elif opcion == 3:
            break
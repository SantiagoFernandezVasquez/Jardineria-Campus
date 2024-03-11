from tabulate import tabulate
import Storage.Pedido as ped
from datetime import datetime
def getAllProcesoPedido():
    ProcesoPedidos = []
    for val in ped.pedido:
        ProcesoPedidos.append({
                    "Codigo_pedido": val.get("codigo_pedido"),
                    "Estado": val.get('estado')
                    })
    return ProcesoPedidos 

def getAllPedidosEntregadosAtrasadosDeTiempo():
    PedidoEntregado = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date1, "%d/%m/%Y")
            end = datetime.strptime(date2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                PedidoEntregado.append({
                    "Codigo_pedido": val.get("codigo_pedido"),
                    "Codigo_cliente": val.get("codigo_cliente"),
                    "Fecha_esperada": val.get("fecha_esperada"),
                    "Fecha_entrega": val.get("fecha_entrega"),
                    "Estado_pedido": val.get("estado")
                })
    return PedidoEntregado

def getAllPedidosEntregadosConAntelacion():
    PedidoEntregado = []
    for val in ped.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date1, "%d/%m/%Y")
            end = datetime.strptime(date2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days >= 2):
                PedidoEntregado.append({
                    "Codigo_pedido": val.get("codigo_pedido"),
                    "Codigo_cliente": val.get("codigo_cliente"),
                    "Fecha_esperada": val.get("fecha_esperada"),
                    "Fecha_entrega": val.get("fecha_entrega"),
                    "Estado_pedido": val.get("estado")
                })
    return PedidoEntregado
def getAllPedidosRechazados():
    PedidosRechazados = []
    for val in ped.pedido:
        if("2009") in val.get("fecha_pedido") and val.get("estado") == "Rechazado":
            PedidosRechazados.append({
                "Codigo_pedido": val.get("codigo_pedido"),
                "Codigo_cliente": val.get("codigo_cliente"),
                "Fecha_pedido": val.get("fecha_pedido"),
                "Estado_pedido": val.get("estado")
            })
    return PedidosRechazados

def getAllPedidosEnero():
    PedidosEnero = []
    for val in ped.pedido:
        fecha_entregado = val.get("fecha_entrega")
        if fecha_entregado:
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            if start.month == 1 and val.get("estado") == "Entregado":
                PedidosEnero.append({
                    "Codigo_pedido": val.get("codigo_pedido"),
                    "Codigo_de_cliente": val.get("codigo_cliente"),
                    "Fecha_de_entrega": val.get("fecha_entrega"),
                    "Estado_pedido": val.get("estado")
                })
    return PedidosEnero

def menu():
    print(""" 
  ___                  _               _                   _ _    _        
 | _ \___ _ __ ___ _ _| |_ ___ ___  __| |___   _ __ ___ __| (_)__| |___ ___
 |   / -_| '_ / _ | '_|  _/ -_(_-< / _` / -_) | '_ / -_/ _` | / _` / _ (_-<
 |_|_\___| .__\___|_|  \__\___/__/ \__,_\___| | .__\___\__,_|_\__,_\___/__/
         |_|                                  |_|                          
        
        1. Obtener el proceso de los pedidos
        2. Obtener los pedidos no entregados a tiempo
        3. Obtener los pedidos entregados con antelacion
        4. Obtener los pedidos rechazados
        5. Obtener todos los pedidos de Enero sin importar su año
    """)
    opcion = int(input("\nIngrese la opcion que desea realizar: "))
    if opcion == 1:
        print(tabulate(getAllProcesoPedido(), headers="keys", tablefmt="fancy_grid"))
    if opcion == 2:
        print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="fancy_grid"))
    if opcion == 3:
        print(tabulate(getAllPedidosEntregadosConAntelacion(), headers="keys", tablefmt="fancy_grid"))
    if opcion == 4:
        print(tabulate(getAllPedidosRechazados(), headers="keys", tablefmt="fancy_grid"))
    if opcion == 5:
        print(tabulate(getAllPedidosEnero(), headers="keys", tablefmt="fancy_grid"))
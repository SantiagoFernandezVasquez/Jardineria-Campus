from tabulate import tabulate
import Storage.Pago as pag

def getAllCodigosPagosAño():
    CodigosAño = []
    codigos_vistos = set()
    for val in pag.pago:
        if "2008" in val.get("fecha_pago"):
            codigo_cliente = val.get("codigo_cliente")
            if codigo_cliente not in codigos_vistos:
                CodigosAño.append(
                    {
                        "Codigo_cliente": val.get("codigo_cliente"),
                        "Fecha": val.get("fecha_pago"),
                        "Total": val.get("total")
                    }
                )
                codigos_vistos.add(codigo_cliente)
    return CodigosAño
    
def getAllPagosPaypalAño():
    FechaPagos = []
    for val in pag.pago:
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"):
            FechaPagos.append({
                    "Codigo_de_cliente": val.get("codigo_cliente"),
                    "Fecha_pago": val.get("fecha_pago"),
                    "Forma_pago": val.get("forma_pago"),
                    "Total": val.get("total")
                })
    FechaPagos = FechaPagos[::-1]
    return FechaPagos

def getAllModosPago():
    TipoPago = set()
    for val in pag.pago:
        FormaDePago = val.get("forma_pago") 
        if FormaDePago not in TipoPago:
            TipoPago.add(FormaDePago)
    return TipoPago

def menu():
    print(""" 
  ___                  _               _                             
 | _ \___ _ __ ___ _ _| |_ ___ ___  __| |___   _ __ __ _ __ _ ___ ___
 |   / -_| '_ / _ | '_|  _/ -_(_-< / _` / -_) | '_ / _` / _` / _ (_-<
 |_|_\___| .__\___|_|  \__\___/__/ \__,_\___| | .__\__,_\__, \___/__/
         |_|                                  |_|       |___/    

    1. Obtener los codigos de los clientes que pagaron en 2008
    2. Obtener los pagos realizados en 2008 usando Paypal como medio de pago
    3. Obtener los modos de pago disponibles
 """)
    opcion = int(input("\nIngrese la opcion que desea realizar: "))
    if(opcion == 1):
        print(tabulate(getAllCodigosPagosAño(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 2):
        print(tabulate(getAllPagosPaypalAño(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 3):
        print(tabulate(getAllModosPago(), tablefmt="fancy_grid"))
from tabulate import tabulate
import Storage.Oficina as of 

def getAllCodigoCiudad():
    codigoCiudad = list()
    for val in of.oficina:
        codigoCiudad.append({
            "Codigo_oficina": val.get("codigo_oficina"),
            "Ciudad": val.get("ciudad") 
        }) 
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais") == pais):
            ciudadTelefono.append({
                "Ciudad": val.get("ciudad"),
                "Telefono": val.get("telefono"),
                "Oficinas": val.get("codigo_oficina"),
                "Pais": val.get("pais")
            })
        return ciudadTelefono
        
def menu():
    print("""
  ___                  _               _            __ _    _           
 | _ \___ _ __ ___ _ _| |_ ___ ___  __| |___   ___ / _(_)__(_)_ _  __ _ 
 |   / -_| '_ / _ | '_|  _/ -_(_-< / _` / -_) / _ |  _| / _| | ' \/ _` |
 |_|_\___| .__\___|_|  \__\___/__/ \__,_\___| \___|_| |_\__|_|_||_\__,_|
         |_|                                                            

    1. Obtener las ubicaciones de una oficina en determinada ciudad 
    2. Obtener los datos las oficinas en un pais (pais)
""")
    opcion = int(input("\nIngrese la opcion que desea realizar: "))
    if(opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 2):
        pais = input("Ingrese el pais: ")
        print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="fancy_grid"))
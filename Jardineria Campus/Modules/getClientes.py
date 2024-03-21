import os
import re
from tabulate import tabulate
import requests

def clear():
    os.system('cls')
clear()

def  getAllClientes():
     petition = requests.get("http://localhost:5001/clientes")
     data = petition.json()
     return data

def getAllClienteId(id):
    for val in getAllClientes():
         if(val.get('id') == id):
             return[val]

def getAllClienteCodigo(codigo):
    for val in getAllClientes():
        if(val.get('codigo_cliente') == codigo):
            return[val]
    
def getAllClienteName():
    clienteName = []
    for i,val in enumerate(getAllClientes):
        clienteName.append({
            "Codigo_cliente": val.get('codigo_cliente'),
            "Nombre_cliente": val.get('nombre_cliente')
         })
    return clienteName

def getOneClienteCodigo(codigo):
    for val in getAllClientes():
        if(val.get('codigo_cliente') == codigo):
            return[{
                "Codigo_cliente": val.get('codigo_cliente'),
                "Nombre_cliente": val.get('nombre_cliente')
            }]
def getAllClientCreditCiudad(limiteCredit, ciudad):
            clienteCredic = list()
            for val in getAllClientes(): 
                if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
                    clienteCredic.append({
                         "Codigo": val.get('codigo_cliente'),
                         "Responsable": val.get('nombre_cliente'),
                         "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                         "Telefono": val.get('telefono'),
                         "Fax": val.get('fax'),
                         "Direcciones": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                         "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                         "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                         "Credito": val.get('limite_credito')
                         })
            return clienteCredic

def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
     clientZone = list()
     for val in getAllClientes():
            if(
                 val.get('pais') == pais and
                 (val.get('region') == region or val.get('region') == None) or
                 (val.get('ciudad') == ciudad or val.get('ciudad') == None)
             ):
               clientZone.append({
                    "Codigo_cliente": val.get('codigo_cliente'),
                    "Nombre_cliente": val.get('nombre_cliente'),
                    "Telefono": val.get('telefono'),
                    "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}"
               })
     return clientZone

def getAllClienteCodigoPostal(codigo_postal):
    clienteCodigoPostal = list()
    for val in getAllClientes():
        if val.get('codigo_postal') == codigo_postal:
            clienteCodigoPostal.append({
                "Codigo_cliente": val.get('codigo_cliente'),
                "Nombre_cliente": val.get('nombre_cliente'),
                "Telefono": val.get('telefono'),
                "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                "Credito": val.get('limite_credito')
            })
    return clienteCodigoPostal 

def getAllClientFax(fax):
      clienteFax = list()
      for val in getAllClientes():
            if val.get('fax') == fax:
                  clienteFax.append({
                        "Codigo_cliente": val.get('codigo_cliente'),
                        "Nombre_cliente": val.get('nombre_cliente'),
                        "Telefono": val.get('telefono'),
                        "Fax": val.get('fax'),
                        "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}"
                  })
      return clienteFax

def getAllClientTelefono(telefono):
     for val in getAllClientes():
        if(val.get('telefono') == telefono):
            return[val]  
            
def getAllEspañaClientes():
    PaisClientes = []
    for val in getAllClientes():
        if(val.get("pais") == ("Spain")):
            PaisClientes.append(
                {
                    "nombre_cliente": val.get("nombre_cliente"),
                    "pais_cliente": val.get("pais")
                }
            )
    return PaisClientes


def menu():
    while True:
         clear()
         print("""
  ___                  _               _       _             _ _         _          
 | _ \___ _ __ ___ _ _| |_ ___ ___  __| |___  | |___ ___  __| (_)___ _ _| |_ ___ ___
 |   / -_| '_ / _ | '_|  _/ -_(_-< / _` / -_) | / _ (_-< / _| | / -_| ' |  _/ -_(_-<
 |_|_\___| .__\___|_|  \__\___/__/ \__,_\___| |_\___/__/ \__|_|_\___|_||_\__\___/__/
         |_|                                                                        

            1. Obtener todos los clientes (codigo y nombre)
            2. Obtener un cliente por su codigo (codigo)
            3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0, San Francisco)
            4. Obtener la informacion de un cliente con respecto a su pais, region o ciudad (pais, region, ciudad)
            5. Obtener la informacion de un cliente con respecto a su codigo postal (codigo_postal)
            6. Obtener la informacion de un cliente con respecto a su Fax (fax)
            7. Obtener todos los clientes de España
            8. Regresar al Menu Principal
    """)
         opcion = int(input("\nIngrese la opcion que desea realizar: "))
         if(re.match(r'^[1-8]$', opcion)):
            opcion = int(opcion)
         if opcion == 1:
              print(tabulate(getAllClienteName(), headers="keys", tablefmt="fancy_grid"))
              input("Presione una tecla para continuar.....")
         elif opcion == 2:
              codigo = int(input("Ingrese el codigo del cliente: "))
              print(tabulate(getOneClienteCodigo(codigo), headers="keys", tablefmt="fancy_grid"))
              input("Presione una tecla para continuar.....")
         elif opcion == 3:
              limiteCredit = float(input("Ingrese el limite de credito del cliente: "))
              ciudad = str(input("Ingrese la ciudad del cliente: "))
              print(tabulate(getAllClientCreditCiudad(limiteCredit, ciudad), headers="keys", tablefmt="fancy_grid"))
              input("Presione una tecla para continuar.....")
         elif opcion == 4:
              pais = str(input("Ingrese el pais del cliente: "))
              region = str(input("Ingrese la region del cliente: "))
              ciudad = str(input("Ingrese la ciudad del cliente: "))
              print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers="keys", tablefmt="fancy_grid"))
              input("Presione una tecla para continuar.....")
         elif opcion == 5:
              codigo_postal = str(input("Ingrese el codigo postal del cliente: "))
              print(tabulate(getAllClienteCodigoPostal(codigo_postal), headers="keys", tablefmt="fancy_grid"))
              input("Presione una tecla para continuar.....")
         elif opcion == 6:
              fax = str(input("Ingrese el fax del cliente: "))
              print(tabulate(getAllClientFax(fax), headers="keys", tablefmt="fancy_grid"))
              input("Presione una tecla para continuar.....")
         elif opcion == 7:
              print(tabulate(getAllEspañaClientes(), headers="keys", tablefmt="fancy_grid"))
              input("Presione una tecla para continuar.....")
         elif opcion == 8:
              break
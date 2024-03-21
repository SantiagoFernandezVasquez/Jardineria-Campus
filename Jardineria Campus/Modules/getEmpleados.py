import os
from tabulate import tabulate
import requests

def  getAllEmpleados():
     petition = requests.get('http://localhost:3000/empleados')
     data = petition.json()
     return data

def getAllEmpleadoId(id):
    for val in getAllEmpleados():
        if(val.get('id') == id):
            return[val]
        
def getAllEmpleadoCodigo(codigo):
    for val in getAllEmpleados():
        if(val.get('codigo_cliente') == codigo):
            return[val]
        

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in getAllEmpleados.empleados:
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
                {
                    "Nombre": val.get("nombre"),
                    "Apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                    "Email": val.get("email"),
                    "Jefe": val.get("codigo_jefe")
                }
            )
    return nombreApellidoEmail

def getAllCodigoPuestoNombreApellidos(nombre):
    PuestoNombreApellidos = []
    for val in getAllEmpleados.empleados:
        if(val.get("nombre") == nombre):
            PuestoNombreApellidos.append(
                {
                    "Puesto": val.get("puesto"),
                    "Nombre": val.get("nombre"),
                    "Apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                    "Email": val.get("email")
                }
            )
    return PuestoNombreApellidos

def getAllNombreApellidoNombresPuesto():
    NombreApellidoPuesto = []
    for val in getAllEmpleados.empleados:
        if(val.get("puesto") != ("Representante Ventas")):
            NombreApellidoPuesto.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                    "puesto": val.get("puesto")
                }
            )
    return NombreApellidoPuesto

def menu():
    while True:
        print(""" 
  ___                  _               _                      _             _        
 | _ \___ _ __ ___ _ _| |_ ___ ___  __| |___   ___ _ __  _ __| |___ __ _ __| |___ ___
 |   / -_| '_ / _ | '_|  _/ -_(_-< / _` / -_) / -_| '  \| '_ | / -_/ _` / _` / _ (_-<
 |_|_\___| .__\___|_|  \__\___/__/ \__,_\___| \___|_|_|_| .__|_\___\__,_\__,_\___/__/
         |_|                                            |_|                          
          
          1. Obtener los datos de un jefe con su codigo(codigo_jefe)
          2. Obtener los datos de un jefe con su nombre(nombre_jefe)
          3. Obtener los jefes que no tienen el titulo de "Representante de Ventas"
          4. Regresar al Menu Principal
    """)
        opcion = int(input("\nIngrese la opcion que desea realizar: "))
        if opcion == 1:
            codigo = int(input("Ingrese el codigo del jefe: "))
            print(tabulate(getAllNombreApellidoEmailJefe(codigo), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif opcion == 2:
            nombre = int(input("Ingrese el nombre del jefe: "))
            print(tabulate(getAllCodigoPuestoNombreApellidos(nombre), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif opcion == 3:
            print(tabulate(getAllNombreApellidoNombresPuesto(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif opcion == 4:
            break
    
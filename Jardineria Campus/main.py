import os
import re
import json
from tabulate import tabulate
import Modules.getClientes as Repcliente
import Modules.postCliente as CRDUcliente
import Modules.getOficina as Repoficina
import Modules.postOficina as CRDUoficina
import Modules.getEmpleados as Repempleado
import Modules.postEmpleados as CRDUempleados
import Modules.getPedido as Reppedido
import Modules.postPedido as CRDUpedido
import Modules.getPagos as Reppago
import Modules.postPagos as CRDUpago
import Modules.getProducto as Repproducto
import Modules.postProducto as CRDUproducto

def clear():
    os.system('cls')
clear()

def menuPagos():
    while True:
        clear()
        print("""
  __  __                   _       ___                  
 |  \/  |___ _ _ _  _   __| |___  | _ \__ _ __ _ ___ ___
 | |\/| / -_| ' | || | / _` / -_) |  _/ _` / _` / _ (_-<
 |_|  |_\___|_||_\_,_| \__,_\___| |_| \__,_\__, \___/__/
                                           |___/
              1. Reporte de pagos
              2. Administrar datos de pagos
              3. Regresar al menu principal
 """)
        opcion = (input("\nSeleccione una de las opciones: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if (opcion == 1):
            Reppago.menu()
        if (opcion == 2):
            CRDUpago.menu()
        elif (opcion == 3):
            break


def menuPedidos():
    while True:
        clear()
        print("""
  __  __                   _       ___        _ _    _        
 |  \/  |___ _ _ _  _   __| |___  | _ \___ __| (_)__| |___ ___
 | |\/| / -_| ' | || | / _` / -_) |  _/ -_/ _` | / _` / _ (_-<
 |_|  |_\___|_||_\_,_| \__,_\___| |_| \___\__,_|_\__,_\___/__/

              1. Reporte de pedidos
              2. Adminitrar datos de pedidos
              3. Regresar al menu principal
 """)
        opcion = (input("\nSeleccione una de las opciones: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            Reppedido.menu()
        if opcion == 2:
            CRDUpedido.menu()
        elif opcion == 3:
            break

def menuEmpleados():
    while True:
        clear()
        print("""
  __  __                   _       ___            _             _        
 |  \/  |___ _ _ _  _   __| |___  | __|_ __  _ __| |___ __ _ __| |___ ___
 | |\/| / -_| ' | || | / _` / -_) | _|| '  \| '_ | / -_/ _` / _` / _ (_-<
 |_|  |_\___|_||_\_,_| \__,_\___| |___|_|_|_| .__|_\___\__,_\__,_\___/__/
                                            |_|           
              1. Reporte de empleados
              2. Administrar datos de empleados
              3. Regresar al menu principal
 """) 
        opcion = (input("\nSeleccione una de las opciones: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            Repempleado.menu()
        if opcion == 2:
            CRDUempleados.menu()
        elif opcion == 3:
            break
            
def menuOficina():
    while True:
        clear()
        print("""
  __  __                   _            __ _    _              
 |  \/  |___ _ _ _  _   __| |___   ___ / _(_)__(_)_ _  __ _ ___
 | |\/| / -_| ' | || | / _` / -_) / _ |  _| / _| | ' \/ _` (_-<
 |_|  |_\___|_||_\_,_| \__,_\___| \___|_| |_\__|_|_||_\__,_/__/ 

              1. Reporte de oficinas
              2. Administrar datos de oficinas
              3. Regresar al menu principal                           
 """)
        opcion = (input("\nSeleccione una de las opciones: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if  opcion == 1:
            Repoficina.menu()
        if opcion == 2:
            CRDUoficina.menu()
        elif opcion == 3:
            break

def menuClientes():
    while True:
        clear()
        print("""
  __  __                   _        ___ _ _         _          
 |  \/  |___ _ _ _  _   __| |___   / __| (_)___ _ _| |_ ___ ___
 | |\/| / -_| ' | || | / _` / -_) | (__| | / -_| ' |  _/ -_(_-<
 |_|  |_\___|_||_\_,_| \__,_\___|  \___|_|_\___|_||_\__\___/__/
              
              1. Reporte de clientes
              2. Administrar datos de clientes
              3. Regresar al menu principal                                                      
 """)
        opcion = (input("\nSeleccione una de las opciones: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if  opcion == 1:
            Repcliente.menu()
        if opcion == 2:
            CRDUcliente.menu()
        elif opcion == 3:
            break

def menuProductos():
    while True:
        clear()
        print("""
  __  __                   _       ___            _         _          
 |  \/  |___ _ _ _  _   __| |___  | _ \_ _ ___ __| |_  _ __| |_ ___ ___
 | |\/| / -_| ' | || | / _` / -_) |  _| '_/ _ / _` | || / _|  _/ _ (_-<
 |_|  |_\___|_||_\_,_| \__,_\___| |_| |_| \___\__,_|\_,_\__|\__\___/__/

            1. Reporte de productos
            2. Administrar datos de productos
            3. Regresar al menu principal               
 """)
        opcion = (input("\nSeleccione una de las opciones: "))
        if(re.match(r'^[1-3]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            Repproducto.menu()
        if opcion == 2:
            CRDUproducto.menu()
        elif opcion == 3:
            break
 





if __name__ == "__main__":

    while True:
        clear()
        print("""
          
    __  __                ___     _         _           _ 
   |  \/  |___ _ _ _  _  | _ \_ _(_)_ _  __(_)_ __ __ _| |
 - | |\/| / -_| ' | || | |  _| '_| | ' \/ _| | '_ / _` | | - 
   |_|  |_\___|_||_\_,_| |_| |_| |_|_||_\__|_| .__\__,_|_|
                                           |_|          

                        1. Menu de Clientes
                        2. Menu de Oficinas
                        3. Menu de Empleados
                        4. Menu de Pedidos
                        5. Menu de Pagos
                        6. Menu de Productos
                        7. Salir
    """)    
        opcion = (input("\nSeleccione una de las opciones: "))
        if(re.match(r'^[1-7]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
             menuClientes()
        elif opcion == 2:
             menuOficina()
        elif opcion == 3:
            menuEmpleados()
        elif opcion == 4:
            menuPedidos()
        elif opcion == 5:
            menuPagos()
        elif opcion == 6:
            menuProductos()
        elif opcion == 7:
            break



#with open("Storage/Producto.json", "r") as f:
#        fichero = f.read()
#        data = json.loads(fichero)
#        for i val in enumerate(data):
#            data[i]["id"] = (i+1)
#        data = json.dumps(data, indent=4).encode("utf-8")
#        with open("Storage/Producto.json", "wb+") as f1:
#            f1.write(data)
#           f1.close()
import os
from tabulate import tabulate
import Modules.getClientes as Cliente
import Modules.getOficina as Oficina
import Modules.getEmpleados as Empleado
import Modules.getPedido as Pedido
import Modules.getPagos as Pago
import Modules.getProducto as Repproducto
import Modules.postProducto as CRDUproducto

def menuProductos():
    while True:
        os.system("clear")
        print("""
  __  __                   _       ___            _         _          
 |  \/  |___ _ _ _  _   __| |___  | _ \_ _ ___ __| |_  _ __| |_ ___ ___
 | |\/| / -_| ' | || | / _` / -_) |  _| '_/ _ / _` | || / _|  _/ _ (_-<
 |_|  |_\___|_||_\_,_| \__,_\___| |_| |_| \___\__,_|\_,_\__|\__\___/__/

            1. Reporte de productos
            2. Guardar, Actualizar o Eliminar un producto
            3. Regresar al Menu Principal               
 """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if opcion == 1:
            Repproducto.menu()
        if opcion == 2:
            CRDUproducto.menu()
        elif opcion == 3:
            break
 





if __name__ == "__main__":
    while True:
        print("""
          
    __  __                ___     _         _           _ 
   |  \/  |___ _ _ _  _  | _ \_ _(_)_ _  __(_)_ __ __ _| |
 - | |\/| / -_| ' | || | |  _| '_| | ' \/ _| | '_ / _` | | - 
   |_|  |_\___|_||_\_,_| |_| |_| |_|_||_\__|_| .__\__,_|_|
                                           |_|          

                        1. Cliente
                        2. Oficina
                        3. Empleado
                        4. Pedidos
                        5. Pagos
                        6. Productos
                        7. Salir
    """)    
        opcion = int(input("\nSeleccione una de las opciones: "))
        if opcion == 1:
            Cliente.menu()
        elif opcion == 2:
            Oficina.menu()
        elif opcion == 3:
            Empleado.menu()
        elif opcion == 4:
            Pedido.menu()
        elif opcion == 5:
            Pago.menu()
        elif opcion == 6:
            menuProductos()
        elif opcion == 7:
            break




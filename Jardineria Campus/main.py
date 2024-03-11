from tabulate import tabulate
import Modules.getClientes as Cliente
import Modules.getOficina as Oficina
import Modules.getEmpleados as Empleado
import Modules.getPedido as Pedido
import Modules.getPagos as Pago

if __name__ == "__main__":
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


import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getProducto as gP

def clear():
    os.system('cls')
clear()

def postProducto():
    producto = dict()
    while True:
        try:
            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto: ")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)is not None):
                    data = gP.getAllProductoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid   "))
                        raise Exception("El codigo del producto ya existe")
                    else:
                        producto["Codigo Producto"] = codigo
                else: 
                    raise Exception("El codigo del producto no es valido")

            if not producto.get("nombre"):
                nombre = input("Ingrese el nombre del producto: ")
                if re.match(r'^[A-Z][a-z]*\s*$', nombre) is not None:
                    producto["Nombre"] = nombre
                else: 
                    raise Exception("El nombre del producto no es válido")

                
            if not producto.get("gama"):
                gama = input("Ingrese la gama del producto: ")
                if re.match(r'^[A-Z][a-z]*\s*$', gama) is not None:
                    producto["Gama"] = gama
                else: 
                    raise Exception("El nombre de la gama no es válido")
            
            if not producto.get("dimensiones"):
                dimensiones = input("Ingrese las dimensiones del producto: ")
                if re.match(r'^[0-9][0-9]*\s*$', dimensiones) is not None:
                    producto["Dimensiones"] = dimensiones
                else: 
                    raise Exception("Las dimensiones del producto no son validas")
                
            if not producto.get("proveedor"):
                proveedor = input("Ingrese el nombre del proveedor del producto: ")
                if re.match(r'^[A-Z][a-z]*\s*$', proveedor) is not None:
                    producto["Proveedor"] = proveedor
                else: 
                    raise Exception("El nombre del proveedor del producto no es valido")
                
            if not producto.get("descripcion"):
                descripcion = input("Ingrese una descripcion del producto: ")
                if re.match(r'^[A-Z][a-z]*\s*$', descripcion) is not None:
                    producto["Descripcion"] = descripcion
                else: 
                    raise Exception("La descripcion del producto no es valido")
                
            if not producto.get("cantidad_en_stock"):
                stock = (input("Ingrese la cantidad en stock del producto: "))
                if re.match(r'^[0-9]*\s*$', stock) is not None:
                    producto["Cantidad en Stock"] = len(stock)
                else: 
                    raise Exception("La cantidad en stock del producto no es valido")
                
            if not producto.get("precio_venta"):
                precioventa = (input("Ingrese el precio de venta del producto: "))
                if re.match(r'^[0-9]*\s*$', precioventa) is not None:
                    producto["Precio Venta"] = len(precioventa)
                else: 
                    raise Exception("El precio de venta del producto no es valido")
                
            if not producto.get("precio_proveedor"):
                precioproveedor = (input("Ingrese el precio del proveedor del producto: "))
                if re.match(r'^[0-9]*\s*$', precioproveedor) is not None:
                    producto["Precio Proveedor"] = len(precioproveedor)
                    break
                else: 
                    raise Exception("El precio del proveedor del producto no es valido")
                
        except Exception as error:
            print(error)


    peticion = requests.post("http://localhost:3000/productos", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def borrarProducto(id):
    data = gP.getProductoCodigo(id)
    if (len(data)):
        peticion = requests.delete(f"http://localhost:3000/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "Producto eliminado"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
                "body":[{
                    "message": "Producto no encontrado",
                    "id": id
            }],
            "status": 400,
        }

def menu():
    while True:
        clear()
        print("""
    _      _       _      _    _                     _      _               _                       _         _          
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___   _ __ _ _ ___ __| |_  _ __| |_ ___ ___
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) | '_ | '_/ _ / _` | || / _|  _/ _ (_-<
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___| | .__|_| \___\__,_|\_,_\__|\__\___/__/
                                                                                   |_|                               
              1. Guardar un producto nuevo
              2. Eliminar un producto 
              3. Regresar al menu de productos
 """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if opcion == 1:
            print(tabulate(postProducto(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif opcion == 2:
            id = input("Ingrese el id del producto que desea eliminar: ")
            print(tabulate(borrarProducto(id), headers="keys", tablefmt="fancy_grid"))
            input("Presione una letra para continuar.....")
        elif opcion == 3:
            break
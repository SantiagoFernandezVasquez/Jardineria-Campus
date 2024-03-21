import os
import re
from tabulate import tabulate
import json
import requests
import Modules.getClientes as gC

def clear():
    os.system('cls')
clear()

def GetClientesId(id):
      peticion=requests.get(f"http://localhost:5001/clientes/{id}") 
      return [peticion.json()] if peticion.ok else[]

def postCliente():
    cliente = dict()
    while True:
        try:
            if(not cliente.get("codigo_cliente")):
                codigo = input("Ingrese el codigo del cliente: ")
                if(re.match(r'^[0-9]+$', codigo)is not None):
                    codigo = int(codigo)
                    data = gC.getAllClienteCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
                        raise Exception("El codigo del cliente ya existe")
                    else:
                        cliente["Codigo Cliente"] = codigo
                else: 
                    raise Exception("El codigo del cliente no es valido")
                
            if not cliente.get("nombre_cliente"):
                nombre = input("Ingrese el nombre del cliente: ")
                if re.match(r'^[A-Z][a-z]*\s*[A-Z]*[a-z]*$', nombre) is not None:
                    cliente["Nombre Cliente"] = nombre
                else: 
                    raise Exception("El nombre del cliente no es valido")

                
            if not cliente.get("nombre_contacto"):
                nombrecontacto = input("Ingrese el nombre de contacto del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', nombrecontacto) is not None:
                    cliente["Nombre Contacto"] = nombrecontacto
                else:
                    raise Exception ("El nombre de contacto del cliente no es valido")
                
            if not cliente.get("apellido_contacto"):
                apellidocontacto = input("Ingrese el apellido de contacto del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', apellidocontacto) is not None:
                    cliente["Apellido Contacto"] = apellidocontacto
                else:
                    raise Exception ("El apellido de contacto del cliente no es valido")
                
            if not cliente.get("telefono"):
                telefono = input("Ingrese el telefono del cliente: ")
                if re.match(r'^\d{1,3}(?: ?\d{4}-?\d{4}|\s?\d{6,11})$', telefono) is not None:
                    data= gC.getAllClientTelefono(telefono)
                    if(data): 
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("El telefono del cliente ya existe")
                    else:
                        cliente["Telefono"] = telefono
                else:
                    raise Exception ("El telefono del cliente no es valido")
                
            if not cliente.get("fax"):
                fax = input("Ingrese el fax del cliente: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', fax) is not None: 
                    cliente["Fax"] = fax
                    
                else:
                    raise Exception ("El fax del cliente no es valido")
            
                         
            if not cliente.get("linea_direccion1"):
                direccion1 = input("Ingrese la direccion 1 del cliente: ")
                if re.match(r'^[A-Za-z0-9\s\-,.#]+[A-Za-z0-9\s\-,.#]*$', direccion1) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion 1 del cliente ya existe")
                    else:
                        cliente["Linea Direccion1"] = direccion1
                else:
                    raise Exception ("La direccion 1 del cliente no es valida")
            
            if not cliente.get("linea_direccion2"):
                direccion2 = input("Ingrese la direccion 2 del cliente: ")
                if re.match(r'^[A-Za-z0-9\s\-,.#]+[A-Za-z0-9\s\-,.#]*$', direccion2) is not None:
                    if(data):
                        print(tabulate(data,tablefmt="grid"))
                        raise Exception("La direccion 2 del cliente ya existe")
                    else:
                        cliente["Linea Direccion2"] = direccion2
                else:
                    raise Exception ("La direccion 2 del cliente no es valida")
                
            if not cliente.get("ciudad"):
                ciudad = input("Ingrese la ciudad del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', ciudad) is not None:
                    cliente["Ciudad"]=ciudad
                else:
                    raise Exception ("La ciudad del cliente no es valida")
                
            if not cliente.get("region"):
                region = input("Ingrese la region del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', region) is not None:
                    cliente["Region"]=region
                else:
                    raise Exception ("La region del cliente no es valida")
                
            if not cliente.get("pais"):
                pais = input("Ingrese el pais del cliente: ")
                if re.match(r'^([A-Za-z]\s*)+$', pais) is not None:
                    cliente["Pais"]=pais
                else:
                    raise Exception ("El pais del cliente no es valida")
                        
            if not cliente.get("codigo_postal"):
                codigopostal = input("Ingrese el codigo postal del cliente: ")
                if re.match(r'^\d{5,7}$', codigopostal) is not None:
                    cliente["Codigo Postal"] = codigopostal
                else:
                    raise Exception ("El codigo postal del cliente no es valido")
                
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigorepventas = input("Ingrese el codigo del representante de ventas: ")
                if re.match(r'^[0-9]+$', codigorepventas) is not None:
                    codigorepventas = int(codigorepventas)
                    cliente["Codigo Empleado Rep Ventas"]=codigorepventas
                else:
                    raise Exception ("El codigo del empleado no es valido")
                        
            if not cliente.get("limite_credito"):
                limitecredito = input("Ingrese el limite de credito del cliente: ")
                if re.match(r'^\d+(\.\d+)?$', limitecredito) is not None:
                    limitecredito = float(limitecredito)
                    cliente["Limite Credito"]=limitecredito
                    break

                else:
                    raise Exception ("El codigo del empleado no es valido")
                
        except Exception as error:
            print(error)        

    peticion = requests.post("http://localhost:5001/clientes", data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"]= "Cliente Guardado"
    return [res]

def borrarCliente(id):
    data = gC.getAllClienteId(id)
    if (len(data)):
        peticion = requests.delete(f"http://localhost:5001/clientes/{id}")
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
        
def GetClienteId(id):
    peticion = requests.get("http//localhost:5001/clientes")
    inf = peticion.json()
    return inf

def actualizarCodigoDelCliente(id):

    while True:
        codigo_cliente = (input("Ingresa el nuevo código del cliente: "))
        if not re.match(r"^[0-9]+$", codigo_cliente):
            print("El código del cliente debe ser un número entero positivo.")
            continue
        response = requests.get(f"http://localhost:5001/clientes/{codigo_cliente}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break

    cliente = {"codigo_cliente":int(codigo_cliente)}


    clienteactualizar = GetClientesId(id)
    if not clienteactualizar:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizar[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarNombreDelCliente(id):
    while True:
        nombre_cliente = (input("Ingrese el nuevo nombre del cliente: "))
        if not re.match(r"^([A-Za-z])+$", nombre_cliente):
            print("El nombre del cliente no es válido.")
            continue
         # Validar si el nombre ya existe
        response = requests.get(f"http://localhost:5001/clientes/{nombre_cliente}")
        if response.status_code == 200:
            print("El código del cliente ya existe.")
            continue

        break
   # PRIMERO ponemos todo el listado de información de nuestra lista
    cliente = {"nombre_cliente":(nombre_cliente),}


    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarNombreDelContacto(id):

    while True:
            nombre_contacto=(input("Ingrese el nuevo nombre del contacto del cliente: "))
            if not re.match(r"^([A-Za-z])+$", nombre_contacto):
                print("El nombre del contacto no es válido.")
                continue
            break



    while True:
        apellido_contacto=(input("Ingrese el nuevo apellido del contacto del cliente: "))
        if not re.match(r"^([A-Za-z])+$", apellido_contacto):
            print("El nombre del contacto no es válido.")
            continue
        break

    cliente = { 
         "nombre_contacto":(nombre_contacto),
        "apellido_contacto":(apellido_contacto),}


    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarTelefonoDelContacto(id):


    while True:
        telefono = (input("Ingresa el nuevo teléfono del cliente: "))
        if not re.match(r"^[0-9]+$", telefono):
            print("El teléfono del cliente se construye de 11 dígitos 00000000000.")
            continue
        response = requests.get(f"http://localhost:5001/clientes/{telefono}")
        if response.status_code == 200:
            print("El teléfono del cliente ya existe.")
            continue
        break

    cliente = {"telefono":(telefono),}


    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarDirecciones1Y2DelContacto(id):

    while True:
            linea_direccion1 = (input("Ingresa la nueva dirección del cliente: "))
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion1):
                continue
            response = requests.get(f"http://localhost:5001/clientes/{linea_direccion1}")
            if response.status_code == 200:
                print("La dirección del cliente ya existe.")
                continue
            break


    while True:
            linea_direccion2 = (input("Ingresa una nueva indicacion a la direccion del cliente: "))
            if not re.match(r"^[\x00-\xFF]+$",linea_direccion2):
                continue
            response = requests.get(f"http://localhost:5001/clientes/{linea_direccion2}")
            if response.status_code == 200:
                print("La direccion del cliente ya existe.")
                continue
            break

    cliente = {
        "linea_direccion1":(linea_direccion1),
        "linea_direccion2":(linea_direccion2)}
    

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarCiudadDelContacto(id):

    while True:
            ciudad = (input("Ingresa la nueva ciudad del cliente: "))
            if not re.match(r"^([A-Za-z])$",ciudad):
                print("La ciudad se indica con primera en mayuscula .")
                continue
            break

    cliente = {"ciudad":(ciudad)}

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarRegionDelContacto(id):

    while True:
            region = (input("Ingresa una nueva región del cliente: "))
            if not re.match(r"^([A-Za-z])$",region):
                print("La región se indica con primera en mayuscula .")
                continue
            break
    
    cliente = {"region":(region)}

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarPaisContacto(id):

    while True:
            pais = (input("Ingresa un nuevo país del cliente: "))
            if not re.match(r"^([A-Za-z])$",pais):
                print("El país se indica con primera en mayuscula .")
                continue
            break

    cliente = {"pais":(pais)}

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarCodigoPostalContacto(id):

    while True:
            codigo_postal = (input("Ingresa un nuevo código postal del cliente: "))
            if not re.match(r"^[0-9]$",codigo_postal):
                print("El código postal se indica con  .")
                continue
            break

    cliente = {"codigo_postal":(codigo_postal),}

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarRepresentanteContacto(id):

    while True:
            codigo_empleado_rep_ventas = (input("Ingresa un nuevo codigo del representante de ventas del cliente: "))
            if not re.match(r"^[0-9]+$",codigo_empleado_rep_ventas):
                continue
            break

    cliente = { "codigo_empleado_rep_ventas":int(codigo_empleado_rep_ventas)}

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizarLimiteCreditoContacto(id):

    while True:
            limite_credito = (input("Ingresa un nuevo limite de crédito del cliente: "))
            if not re.match(r"^[0-9]+$",limite_credito):
                print("El limite crédito se indica con un número.")
                continue
            break

    cliente = { "limite_credito":float(limite_credito)}

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]

def actualizaridContacto(id):

    while True:
        idNueva = (input("Ingresa el nuevo id del cliente: "))
        if not re.match(r"^[0-9]+$", idNueva):
            continue

        
        response = requests.get(f"http://localhost:5001/clientes/{idNueva}")
        if response.status_code == 200:
            print("El id del cliente ya existe.")
            continue

        break

    cliente = {"id":int(idNueva)}

    clienteactualizable=GetClientesId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo= {**clienteactualizable[0],**cliente}
    peticion=requests.put(f"http://localhost:5001/clientes/{id}",data=json.dumps(clientenuevo))
    res=peticion.json()

    if peticion.status_code==200:
        res["messaje"]="Cliente actualizado correctamente"
    else:
        res["message"]="Cliente no se pudo actualizar"
    
    return[res]


def ActualizarCodigoCliente(id):
    while True:
            codigo_cliente = input("Ingresa el nuevo codigo del cliente: ")
            if not re.match(r'^\d+$', codigo_cliente):
                print("El codigo del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{codigo_cliente}")
            if res.status_code == 200:
                print("El codigo del cliente ya existe")
                continue
            break
    while True:
                nombre_cliente = input("Ingrese el nuevo nombre del cliente: ")
                if not re.match(r'^[A-Z][a-z]*\s*[A-Z]*[a-z]*$', nombre_cliente):
                    print("El nombre del cliente no es valido")
                    continue
                res = requests.get("http://localhost:5001/clientes/{nombre_cliente}")
                if res.status_code == 200:
                    print("El nombre del cliente ya existe")
                    continue
                break
    while True:
            nombre_contacto = input("Ingrese el nuevo nombre del contacto del cliente: ")
            if not re.match(r'^[A-Z][a-z]*\s*[A-Z]*[a-z]*$', nombre_contacto):
                print("El nombre del contacto del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{nombre_contacto}")
            if res.status_code == 200:
                print("El nombre del contacto del cliente ya existe")
                continue
            break
    while True:
            apellido_contacto = input("Ingrese el nuevo apellido del contacto del cliente: ")
            if not re.match(r'^[A-Z][a-z]*\s*[A-Z]*[a-z]*$', apellido_contacto):
                print("El apellido del contacto del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{apellido_contacto}")
            if res.status_code == 200:
                print("El apellido del contacto del cliente ya existe")
                continue
            break
    while True:
            telefono = input("Ingrese el nuevo telefono del cliente: ")
            if not re.match(r'^[0-9]+$', telefono):
                print("El telefono del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{telefono}")
            if res.status_code == 200:
                print("El telefono del cliente ya existe")
                continue
            break
    while True:
            fax = input("Ingrese el nuevo fax del cliente: ")
            if not re.match(r'^[0-9]+$', fax):
                print("El fax del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{fax}")
            if res.status_code == 200:
                print("El fax del cliente ya existe")
                continue
            break
    while True:
            linea_direccion1 = input("Ingrese la nueva direccion1 del cliente: ")
            if not re.match(r'^[A-Za-z0-9\s]+$', linea_direccion1):
                print("La direccion1 del cliente no es valida")
                continue
            res = requests.get("http://localhost:5001/clientes/{linea_direccion1}")
            if res.status_code == 200:
                print("La direccion1 del cliente ya existe")
                continue
            break
    while True:
            linea_direccion2 = input("Ingrese la nueva direccion2 del cliente: ")
            if not re.match(r'^[A-Za-z0-9\s]+$', linea_direccion2):
                print("La direccion2 del cliente no es valida")
                continue
            res = requests.get("http://localhost:5001/clientes/{linea_direccion2}")
            if res.status_code == 200:
                print("La direccion2 del cliente ya existe")
                continue
            break
    while True:
            ciudad = input("Ingrese la nueva ciudad del cliente: ")
            if not re.match(r'^[A-Za-z0-9\s]+$', ciudad):
                print("La ciudad del cliente no es valida")
                continue
            res = requests.get("http://localhost:5001/clientes/{ciudad}")
            if res.status_code == 200:
                print("La ciudad del cliente ya existe")
                continue
            break
    while True:
            region = input("Ingrese la nueva region del cliente: ")
            if not re.match(r'^[A-Za-z0-9\s]+$', region):
                print("La region del cliente no es valida")
                continue
            res = requests.get("http://localhost:5001/clientes/{region}")
            if res.status_code == 200:
                print("La region del cliente ya existe")
                continue
            break
    while True:
            pais = input("Ingrese el nuevo pais del cliente: ")
            if not re.match(r'^[A-Za-z0-9\s]+$', pais):
                print("El pais del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{pais}")
            if res.status_code == 200:
                print("El pais del cliente ya existe")
                continue
            break
    while True:
            codigo_postal = input("Ingrese el nuevo codigo postal del cliente: ")
            if not re.match(r'^[0-9]+$', codigo_postal):
                print("El codigo postal del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{codigo_postal}")
            if res.status_code == 200:
                print("El codigo postal del cliente ya existe")
                continue
            break
    while True:
            codigo_empleado_rep_ventas = input("Ingrese el nuevo codigo del representante de ventas del cliente: ")
            if not re.match(r'^[0-9]+$', codigo_empleado_rep_ventas):
                print("El codigo del representante de ventas del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{codigo_empleado_rep_ventas}")
            if res.status_code == 200:
                print("El codigo del representante de ventas del cliente ya existe")
                continue
            break
    while True:
            limite_credito = input("Ingrese el nuevo limite de credito del cliente: ")
            if not re.match(r'^[0-9]+$', limite_credito):
                print("El limite de credito del cliente no es valido")
                continue
            res = requests.get("http://localhost:5001/clientes/{limite_credito}")
            if res.status_code == 200:
                print("El limite de credito del cliente ya existe")
                continue
            break
    
    cliente = {
        "codigo_cliente":int(codigo_cliente),
        "nombre_cliente":(nombre_cliente),
        "nombre_contacto":(nombre_contacto),
        "apellido_contacto":(apellido_contacto),
        "telefono":(telefono),
        "fax":(fax),
        "linea_direccion1":(linea_direccion1),
        "linea_direccion2":(linea_direccion2),
        "ciudad":(ciudad),
        "region":(region),
        "pais":(pais),
        "codigo_postal":(codigo_postal),
        "codigo_empleado_rep_ventas":int(codigo_empleado_rep_ventas),
        "limite_credito":float(limite_credito),
        "id":int(id)
    }
        

    clienteactualizable = GetClienteId(id)
    if not clienteactualizable:
            return{"message":"Cliente no encontrado"}
        
    clientenuevo = {**clienteactualizable[0], **cliente}
    peticion = requests.put(f"http://localhost5001/clientes/{id}", data=json.dumps(clientenuevo))
    res = peticion.json()

    if peticion.status_code == 200:
        res["message"] = ("Cliente actualizado")
    else: 
        res["message"] = ("Error al actualizar el cliente")

    return[res]
    

            
        
def menuActualizar():
    while True:
        clear()
        print("""
    _      _             _ _               ___       _          
   /_\  __| |_ _  _ __ _| (_)_____ _ _ _  |   \ __ _| |_ ___ ___
  / _ \/ _|  _| || / _` | | |_ / _` | '_| | |) / _` |  _/ _ (_-<
 /_/ \_\__|\__|\_,_\__,_|_|_/__\__,_|_|   |___/\__,_|\__\___/__/

              1. Actualizar el codigo de un cliente
              2. Actualizar el nombre de un cliente
              3. Actualizar el nombre y apeelido del contacto de un cliente
              4. Actualizar el telefono de un cliente
              5. Actualizar el fax de un cliente
              6. Actualizar las direcciones de un cliente
              7. Actualizar la ciudad del cliente
              8. Actualizar la region del cliente
              9. Actualizar el pais de un cliente
              10. Actualizar el codigo postal de un cliente
              11. Actualizar el codigo del representante de ventas de un cliente
              12  Actualizar el limite de credito de un cliente

              13. Actualizar todas estas
              14 Regresar al Administrador de Clientes
 """)
        opcion = input("\nSeleccione la opcion que le gustaria realizar: ")
        if(re.match(r'^[1-16]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarCodigoDelCliente(id),headers="keys",tablefmt="grid"))
        if opcion == 2:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarNombreDelCliente(id),headers="keys",tablefmt="grid"))
        if opcion == 3:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarNombreDelContacto(id),headers="keys",tablefmt="grid"))
        if opcion == 4:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarTelefonoDelContacto(id),headers="keys",tablefmt="grid"))
        if opcion == 5:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarDirecciones1Y2DelContacto(id),headers="keys",tablefmt="grid"))
        if opcion == 6:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarCiudadDelContacto(id),headers="keys",tablefmt="grid"))             
        if opcion == 7:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarRegionDelContacto(id),headers="keys",tablefmt="grid"))    
        if opcion == 8:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarPaisContacto(id),headers="keys",tablefmt="grid"))    
        if opcion == 9:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarCodigoPostalContacto(id),headers="keys",tablefmt="grid"))    
        if opcion == 10:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarRepresentanteContacto(id),headers="keys",tablefmt="grid"))                                                                                                                                            
        if opcion == 11:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizarLimiteCreditoContacto(id),headers="keys",tablefmt="grid"))                
        if opcion == 12:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(actualizaridContacto(id),headers="keys",tablefmt="grid"))
        if opcion == 13:
            id=input("Ingrese la id del cliente que desea actualizar: ")
            print(tabulate(ActualizarCodigoCliente(id),headers="keys",tablefmt="grid"))
        if opcion == 14:
            break    



def menu():
    while True:
        clear()
        print("""
    _      _       _      _    _                     _      _               _                      _ _         _       
   /_\  __| |_ __ (_)_ _ (_)__| |_ _ _ __ _ _ _   __| |__ _| |_ ___ ___  __| |___   _  _ _ _    __| (_)___ _ _| |_ ___ 
  / _ \/ _` | '  \| | ' \| (_-|  _| '_/ _` | '_| / _` / _` |  _/ _ (_-< / _` / -_) | || | ' \  / _| | / -_| ' |  _/ -_)
 /_/ \_\__,_|_|_|_|_|_||_|_/__/\__|_| \__,_|_|   \__,_\__,_|\__\___/__/ \__,_\___|  \_,_|_||_| \__|_|_\___|_||_\__\___|

                                
                                1. Ingresar los datos de un cliente nuevo   
                                2. Eliminar un cliente                                                     
                                3. Actualizar el nombre del cliente
                                4. Regresar al menu principal
""")  
        opcion = int(input("\nSeleccione la opcion que le gustaria realizar: "))
        if(re.match(r'^[1-4]$', opcion)):
            opcion = int(opcion)
        if opcion == 1:
            print(tabulate(postCliente(), headers="keys", tablefmt="fancy_grid"))
            input("Presione una tecla para continuar.....")
        elif opcion == 2:
            id = input("Ingrese el id del cliente que desea eliminar: ")
            print(borrarCliente(id))
            input("Presione una tecla para continuar.....")
        elif opcion == 3:
            menuActualizar()
        elif opcion == 4:
            break
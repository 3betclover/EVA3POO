def listavehiculo(vehiculos):
    c=1
    for veh in vehiculos:
        datos="{0}. Id: {1} | Nombre: {2} | Marca: {3} | Modelo: {4} | Año: {5} | Mantenciones: {6}"
        print(datos.format(c,veh[0],veh[1],veh[2],veh[3],veh[4],veh[5]))
        c+=1
    print("--------------------------------------------------")


def leerDatosVehiculo():
    nombre=input("Ingrese nombre del cliente: ")
    marca=input("Ingrese marca del vehículo: ")
    modelo=input("Ingrese modelo del vehículo: ")
    anio=int(input("Ingrese año del vehículo: "))
    mantenciones=int(input("Ingrese cantidad de mantenciones: "))
    vehiculo=[0,nombre,marca,modelo,anio,mantenciones]
    return vehiculo

def leerDatosNuevosVehiculo(vehiculo):
    id=vehiculo[0]
    nombre=vehiculo[1]
    marca=vehiculo[2]
    modelo=vehiculo[3]
    anio=vehiculo[4]
    mantenciones=vehiculo[5]
    print(vehiculo)
    while True:
        print("1. nombre: ",nombre)
        print("2. marca: ",marca)
        print("3. modelo: ",modelo)
        print("4. año: ",anio)
        print("5. mantenciones: ",mantenciones)
        print("6. Salir")
        opcion=int(input("Ingrese una opción (1-6):"))
        if opcion==1:
            nombre=input("Ingrese nombre: ")
        elif opcion==2:
            marca=input("Ingrese marca: ")
        elif opcion==3:
            modelo=input("Ingrese modelo: ")
        elif opcion==4:
            anio=int(input("Ingrese año: "))
        elif opcion==5:
            mantenciones=int(input("Ingrese mantenciones: "))
        elif opcion==6:
            vehiculo=[id,nombre,marca,modelo,anio,mantenciones]
            break
        else:
            print("Opción no válida")
    return vehiculo
        
        
def leerIdVehiculo():
    id = int(input("Ingrese el ID del vehículo: "))
    return id
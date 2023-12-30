from DB.conexion import DAO
import VISTA.funciones

def menuPrincipal():
    while True:
        print("***Bienvenido a mi cacharrito***")
        print("1. Listar vehículos")
        print("2. Ingresar vehículo")
        print("3. Eliminar vehículo")
        print("4. Buscar vehículo")
        print("5. Actualizar datos de vehículo")
        print("6. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion < 1 or opcion > 6:
            print("Opción no válida")
        elif opcion == 6:
            print("Hasta la vista")
            break
        else:
            ejecutarOpcionMenu(opcion)

def ejecutarOpcionMenu(opcion):
    dao = DAO()
    if opcion == 1:
        try:
            vehiculos = dao.listavehiculo()
            if len(vehiculos) > 0:
                VISTA.funciones.listavehiculo(vehiculos)
            else:
                print("No hay vehículos registrados")
        except:
            print("Error ...")
    elif opcion == 2:
        vehiculo=VISTA.funciones.leerDatosVehiculo()
        try:
            dao.creardatosvehiculo(vehiculo)
        except:
            print("Error ...")
    elif opcion == 3:
        id=VISTA.funciones.leerIdVehiculo()
        if  dao.buscarVehiculo(id)!=None:
            dao.eliminarVehiculo(id)
        else:
            print("No se encontró el vehículo para eliminar")
    elif opcion == 4:
        id=VISTA.funciones.leerIdVehiculo()
        vehiculo = dao.buscarVehiculo(id)
        if vehiculo != None:
            print("Vehículo encontrado: ", vehiculo)
        else:
            print("No existe el vehículo")
    elif opcion == 5:
        id = VISTA.funciones.leerIdVehiculo()
        vehiculo = dao.buscarVehiculo(id)
        if vehiculo != None:
            nuevos_datos = VISTA.funciones.leerDatosNuevosVehiculo(vehiculo)
            nuevos_datos.insert(-1, id) 
            dao.actualizarVehiculo(nuevos_datos)
            print("Datos del vehículo actualizados correctamente.")
        else:
            print("No existe el vehículo")
menuPrincipal()
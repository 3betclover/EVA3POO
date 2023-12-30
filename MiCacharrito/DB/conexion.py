import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        self.conexion = None
        try:
            # comunicar python con mysql
            self.conexion = mysql.connector.connect(
                host='localhost',  # hosting
                port=3306,  # puerto de mysql
                user='root',  # usuario
                password='',  # contraseña
                database='mi_cacharrito'  # nombre de la base de datos
            )
        except Error as ex:
            print("Error de conexión: ", ex)

    def listavehiculo(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM vehiculo ORDER BY nombre_cliente ASC")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error de conexión: ", ex)

    def creardatosvehiculo(self, vehiculo):
        if self.conexion.is_connected():
            try:  
                cursor = self.conexion.cursor()
                query = "INSERT INTO vehiculo (id, nombre_cliente, marca, modelo, anio, mantenciones) VALUES({0},'{1}','{2}','{3}',{4},{5})"
                cursor.execute(query.format(0,vehiculo[1],vehiculo[2],vehiculo[3],vehiculo[4],vehiculo[5]))
                self.conexion.commit()
                print("Registro de vehiculo insertado correctamente...")
            except Error as ex:
                print("Error al conectar...", ex)

    def eliminarVehiculo(self, idEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "DELETE FROM vehiculo WHERE id={0}"
                cursor.execute(query.format(idEliminar))
                self.conexion.commit()
                print("Registro eliminado correctamente...")
            except Error as ex:
                print("Error al conectar...", ex)

    def buscarVehiculo(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM vehiculo WHERE id={0}".format(id))
                resultado = cursor.fetchone()
                return resultado
            except Error as ex:
                print("Error al conectar...", ex)

    def actualizarVehiculo(self, vehiculo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE vehiculo SET id=%s, nombre_cliente=%s, marca=%s, modelo=%s, anio=%s, mantenciones=%s WHERE id=%s"
                values = (vehiculo[0], vehiculo[1], vehiculo[2], vehiculo[3], vehiculo[4], vehiculo[5], vehiculo[0])
                cursor.execute(query, values)
                self.conexion.commit()
                print("Registro actualizado correctamente...")
            except Error as ex:
                print("Error al conectar...", ex)
                


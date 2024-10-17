
import mysql.connector
from models.registro_tiempo import RegistroDeTiempo
from config.database import db_config

class RegistroDeTiempoController:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)
    
    def crear_registro(self, registro):
        connection = self.conectar()
        cursor = connection.cursor()
        query = ("INSERT INTO registrodetiempo (fecha, horasTrabajadas, descripcion, empleado_id) ""VALUES (%s, %s, %s, %s)")
        cursor.execute(query, (registro.get_fecha(), registro.get_horasTrabajadas(), registro.get_descripcion(), registro.get_empleado_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_registro(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM registrodetiempo"
        cursor.execute(query)
        registro = cursor.fetchall()
        cursor.close()
        connection.close()
        return registro
    
    def buscar_registro_por_id(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM registrodetiempo WHERE id = %s"
        cursor.execute(query, (id,))
        registro = cursor.fetchone()
        cursor.close()
        connection.close()
        return registro 
    
    def modificar_registro(self, registro):
        connection = self.conectar()
        cursor = connection.cursor()
        query = ("UPDATE registrodetiempo SET fecha = %s, horasTrabajadas = %s, descripcion = %s, fecha_inicio = %s WHERE id = %s")
        cursor.execute(query, (registro.get_fecha(), registro.get_horasTrabajadas(), registro.get_descripcion(), registro.get_empleado_id(), registro.get_id()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_registro(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM registrodetiempo WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
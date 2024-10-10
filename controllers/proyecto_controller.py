import mysql.connector
from models.proyecto import Proyecto
from config.database import db_config

class Proyectocontroller:
    def __init__(self):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)
    
    def crear_proyecto(self, proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = ("INSERT INTO Proyecto (id, nombre, descripcion, fecha_inicio) "
                 "VALUES (%s, %s, %s, %s)")
        cursor.execute(query, (proyecto.get_id(), proyecto.get_nombre(), proyecto.get_descripcion(),
                               proyecto.get_fecha_inicio()))
        connection.commit()
        cursor.close()
        connection.close()

    def listar_proyecto(self):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Proyecto"
        cursor.execute(query)
        proyecto = cursor.fetchall()
        cursor.close()
        connection.close()
        return proyecto
    
    def buscar_proyecto_por_id(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "SELECT * FROM Proyecto WHERE id = %s"
        cursor.execute(query, (id,))
        proyecto = cursor.fetchone()
        cursor.close()
        connection.close()
        return proyecto 
    
    def modificar_proyecto(self, proyecto):
        connection = self.conectar()
        cursor = connection.cursor()
        query = ("UPDATE Proyecto SET id = %s, 'nombre' = %s, 'descripcion' = %s, fecha_inicio = %s")
        cursor.execute(query, (proyecto.get_id(), proyecto.get_nombreon(),
                               proyecto.get_descripcion(), proyecto.get_fecha_inicio()))
        connection.commit()
        cursor.close()
        connection.close()

    def eliminar_proyecto(self, id):
        connection = self.conectar()
        cursor = connection.cursor()
        query = "DELETE FROM Proyecto WHERE id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        cursor.close()
        connection.close()
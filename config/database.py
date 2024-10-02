"""
Este módulo maneja la conexión a la base de datos MySQL.
Proporciona funciones para conectar y desconectar la base de datos.
"""

import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """
    Establece una conexión con la base de datos MySQL y la devuelve.

    Returns:
        La conexión a la base de datos MySQL si es exitosa.
        Si ocurre un error al intentar conectarse.
    """
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(
            host='localhost',       # Cambia esto si es necesario
            user='root',            # Tu usuario de MySQL
            password='Inacap.2024', # Tu contraseña de MySQL
            database='ejemplo1',    # Nombre de tu base de datos
            port='3306'             # Puerto de conexion Mysql por defecto
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    # Si ocurre un error, devolver None explícitamente
    return None

def close_db_connection(connection):
    """
    Cierra la conexión a la base de datos MySQL.

    Args:
        La conexión activa a MySQL que se va a cerrar.
    """
    if connection and connection.is_connected():
        connection.close()
        print("Conexión a la base de datos cerrada")

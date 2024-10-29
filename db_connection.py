import mysql.connector
from mysql.connector import Error

class ConectarDB:
    def __init__(self):
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="argbroker"
            )
            # if self.connection.is_connected():
                # print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def desconectar(self):
        if self.connection.is_connected():
            self.connection.close()
            # print("Conexión cerrada")

    def ejecutar_consulta(self, consulta, valores=None):
        cursor = self.connection.cursor()
        try:
            if valores:
                # Al realizar la consulta de este modo, estoy evitando inyecciones SQL
                cursor.execute(consulta, valores)
            else:
                cursor.execute(consulta)
            self.connection.commit()
            # print("Consulta ejecutada exitosamente")
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            
    def obtener_datos(self, consulta, valores=None):
        cursor = self.connection.cursor()
        try:
            if valores:
                cursor.execute(consulta, valores)  # Se agrego la variable de valores para evitar inyecciones SQL
            else:
                cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Error al obtener los datos: {e}")
        finally:
            cursor.close()


# Prueba conexión y muestra usuarios de la base
if __name__ == "__main__":
    db = ConectarDB()
    db.conectar()
    
    consulta_select = "SELECT * FROM Usuario"
    resultados = db.obtener_datos(consulta_select)
    print("Usuarios disponibles en la base de datos: ")
    for fila in resultados:
        print(fila)
    
    db.desconectar()

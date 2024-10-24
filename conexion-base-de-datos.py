import mysql.connector
from mysql.connector import Error

# Conectar a la base de datos MySQL
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='ARGBroker',  # Nombre de tu base de datos
            user='root',           # Cambia por tu usuario de MySQL
            password='password'    # Cambia por tu contraseña de MySQL
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos ARGBroker")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Cerrar la conexión
def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

# Función para mostrar todos los usuarios
def mostrar_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuario")
    usuarios = cursor.fetchall()
    print("\n--- Usuarios Registrados ---")
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Apellido: {usuario[2]}, Email: {usuario[3]}, Saldo: {usuario[5]}")
    cursor.close()

# Función para mostrar las transacciones de un usuario específico
def mostrar_transacciones_usuario(conexion, id_usuario):
    cursor = conexion.cursor()
    query = """
    SELECT tipoTransaccion, cantidad, precio, fechaOperacion 
    FROM Transaccion 
    WHERE idUsuario = %s
    """
    cursor.execute(query, (id_usuario,))
    trancciones = cursor.fetchall()
    print(f"\n--- Transacciones del Usuario {id_usuario} ---")
    for transaccion in transacciones:
        print(f"Tipo: {transaccion[0]}, Cantidad: {transaccion[1]}, Precio: {transaccion[2]}, Fecha: {transaccion[3]}")
    cursor.close()

# Función para mostrar el portafolio de un usuario
def mostrar_portafolio_usuario(conexion, id_usuario):
    cursor = conexion.cursor()
    query = """
    SELECT u.nombre, a.nombre AS accion, p.cantidad 
    FROM Usuario u
    JOIN Portafolio p ON u.idUsuario = p.idUsuario
    JOIN Accion a ON p.idAccion = a.idAccion
    WHERE u.idUsuario = %s
    """
    cursor.execute(query, (id_usuario,))
    portafolio = cursor.fetchall()
    print(f"\n--- Portafolio del Usuario {id_usuario} ---")
    for item in portafolio:
        print(f"Usuario: {item[0]}, Acción: {item[1]}, Cantidad: {item[2]}")
    cursor.close()

# Función para mostrar cotizaciones históricas de una acción
def mostrar_cotizaciones_accion(conexion, id_accion):
    cursor = conexion.cursor()
    query = """
    SELECT fechaHora, precio 
    FROM Cotizacion 
    WHERE idAccion = %s 
    ORDER BY fechaHora DESC
    """
    cursor.execute(query, (id_accion,))
    cotizaciones = cursor.fetchall()
    print(f"\n--- Cotizaciones Históricas de la Acción {id_accion} ---")
    for cotizacion in cotizaciones:
        print(f"Fecha: {cotizacion[0]}, Precio: {cotizacion[1]}")
    cursor.close()

# Función para mostrar todas las acciones disponibles
def mostrar_acciones_disponibles(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, simbolo, precio_actual FROM Accion")
    acciones = cursor.fetchall()
    print("\n--- Acciones Disponibles ---")
    for accion in acciones:
        print(f"Nombre: {accion[0]}, Símbolo: {accion[1]}, Precio Actual: {accion[2]}")
    cursor.close()

# Función principal
def main():
    conexion = crear_conexion()

    if conexion:
        # Mostrar todos los usuarios
        mostrar_usuarios(conexion)
        
        # Mostrar las transacciones de un usuario (por ejemplo, idUsuario = 1)
        mostrar_transacciones_usuario(conexion, 1)

        # Mostrar el portafolio de un usuario (por ejemplo, idUsuario = 1)
        mostrar_portafolio_usuario(conexion, 1)

        # Mostrar cotizaciones históricas de una acción (por ejemplo, idAccion = 1)
        mostrar_cotizaciones_accion(conexion, 1)

        # Mostrar todas las acciones disponibles
        mostrar_acciones_disponibles(conexion)

        # Cerrar la conexión a la base de datos
        cerrar_conexion(conexion)

if __name__ == "__main__":
    main()

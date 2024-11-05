from operaciones_usuario import OperacionesUsuarioDB
from db_connection import ConectarDB

db = ConectarDB()
operaciones = OperacionesUsuarioDB()

def mostrar_menu():
    while True:
        if not operaciones.sesion.es_activa():
            print("\nBienvenido al ARG Broker, ¿qué desea hacer?")
            print("1. Mostrar Datos de Usuarios de Prueba")
            print("2. Iniciar Sesión")
            print("3. Recuperar Contraseña")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                operaciones.mostrar_usuarios()
            elif opcion == "2":
                print("\n--- Iniciar Sesión ---")
                cuil_o_email = input("Ingrese su CUIL o email: ")
                password = input("Ingrese su contraseña: ")
                
                operaciones.iniciar_sesion(cuil_o_email, password)
            elif opcion == "3":
                print("\n--- Recuperar Contraseña ---")
                recuperar_password()
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        else:
            print("\nMenú Usuario")
            print("1. Mostrar Transacciones")
            print("2. Mostrar Portafolio")
            print("3. Mostrar Acciones Disponibles")
            print("4. Mostrar Cotizaciones de una Acción")
            print("5. Cambiar Contraseña")
            print("6. Cerrar Sesión")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                operaciones.mostrar_transacciones()
            elif opcion == "2":
                operaciones.mostrar_portafolio()
            elif opcion == "3":
                mostrar_acciones_disponibles()
            elif opcion == "4":
                mostrar_cotizaciones_accion()
            elif opcion == "5":
                cambiar_password()
            elif opcion == "6":
                operaciones.cerrar_sesion()
            elif opcion == "7": 
                # Esta opción me queda en duda, ya que se podría eliminar dejando solo la opción de cerrar sesión,
                # obligando al usuario a primero cerrar sesión antes de cerrar el programa.
                
                # Pero creo que lo mejor sería dejarlo, asegurandome primero que se cierre la sesión antes de cerrar el programa
                operaciones.cerrar_sesion()                
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
            

def cambiar_password():
    if operaciones.sesion.es_activa():
        usuario_id = operaciones.sesion.usuario[0]  # Obtener el ID del usuario en sesión
        password_actual = input("Ingrese su contraseña actual: ")
        nueva_password = input("Ingrese su nueva contraseña: ")
        
        operaciones.cambiar_password_conectado(usuario_id, password_actual, nueva_password)
    else:
        print("Debe iniciar sesión para cambiar la contraseña.")
        
def recuperar_password():
    cuil_o_email = input("Ingrese su cuil o email: ")
    operaciones.solicitar_codigo_verificacion(cuil_o_email)
    operaciones.recuperar_password(cuil_o_email)

# Función para mostrar cotizaciones históricas de una acción
def mostrar_cotizaciones_accion():
    id_accion = input("Ingrese el ID de la acción: ")
    db.conectar()
    query = """
    SELECT fechaHora, precio 
    FROM Cotizacion 
    WHERE idAccion = %s 
    ORDER BY fechaHora DESC
    """
    print(f"\n--- Cotizaciones Históricas de la Acción {id_accion} ---")
    cotizaciones = db.obtener_datos(query, (id_accion,))
    for cotizacion in cotizaciones:
        print(f"Fecha: {cotizacion[0]}, Precio: {cotizacion[1]}")
    db.desconectar()

# Función para mostrar todas las acciones disponibles
def mostrar_acciones_disponibles():
    db.conectar()
    consulta = "SELECT idAccion, nombre, simbolo, precio_actual FROM Accion"
    acciones = db.obtener_datos(consulta)
    print("\n--- Acciones Disponibles ---")
    for accion in acciones:
        print(f"ID Acción: {accion[0]}, Nombre: {accion[1]}, Símbolo: {accion[2]}, Precio Actual: {accion[3]}")
    db.desconectar()

if __name__ == "__main__":
    mostrar_menu()
from db_connection import ConectarDB
from operaciones_usuario import OperacionesUsuarioDB
from usuario import Usuario
from decimal import Decimal

db = ConectarDB()
operaciones = OperacionesUsuarioDB()
usuario = Usuario()  # Inicia un usuario vacío

def mostrar_menu():
    while True:
        if not operaciones.sesion.es_activa():
            print("\nBienvenido al ARG Broker, ¿qué desea hacer?")
            print("1. Mostrar Datos de Usuarios de Prueba")
            print("2. Iniciar Sesión")
            print("3. Recuperar Contraseña")
            print("4. Crear Usuario")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                mostrar_usuarios()
            elif opcion == "2":
                iniciar_sesion()  
            elif opcion == "3":                
                recuperar_password()
            elif opcion == "4":
                crear_usuario()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        else:
            # Establece los valores de usuario
            usuario.id = operaciones.sesion.usuario[0]
            usuario.nombre = operaciones.sesion.usuario[1]
            usuario.apellido = operaciones.sesion.usuario[2]
            usuario.cuil = operaciones.sesion.usuario[3]
            usuario.email = operaciones.sesion.usuario[4]
            usuario.saldo = operaciones.sesion.usuario[6]    
            
            # Imprime el menú
            print("\nMenú Usuario")
            print("1. Mostrar Datos Cuenta")
            print("2. Depositar Saldo")
            print("3. Mostrar Transacciones")
            print("4. Mostrar Portafolio")
            print("5. Mostrar Acciones Disponibles")
            print("6. Mostrar Cotizaciones de una Acción")
            print("7. Comprar Acciones")
            print("8. Cambiar Contraseña")
            print("9. Cerrar Sesión")
            print("10. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                datos_cuenta()
            elif opcion == "2":
                depositar_saldo()
            elif opcion == "3":
                mostrar_transacciones()
            elif opcion == "4":
                mostrar_portafolio()
            elif opcion == "5":
                mostrar_acciones_disponibles()
            elif opcion == "6":
                mostrar_cotizaciones_accion()
            elif opcion == "7":
                comprar_accion()
            elif opcion == "8":
                cambiar_password()
            elif opcion == "9":
                operaciones.cerrar_sesion()
            elif opcion == "10": 
                # Esta opción me queda en duda, ya que se podría eliminar dejando solo la opción de cerrar sesión,
                # obligando al usuario a primero cerrar sesión antes de cerrar el programa.
                
                # Pero creo que lo mejor sería dejarlo, pero asegurandome primero de que se cierre la sesión antes de cerrar el programa
                operaciones.cerrar_sesion()                
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Funciones menu bienvenida
def mostrar_usuarios():
    db.conectar()
    consulta_select = "SELECT * FROM Usuario"
    resultados = db.obtener_datos(consulta_select)
    
    # Imprimir encabezado con tabuladores
    print("Usuarios disponibles en la base de datos: ")
    print("ID\t\tNombre\t\tApellido\tCUIL\t\tEmail\t\t\tPassword\t\tSaldo\t\tIntentos\t\tHora Bloqueado\t\tCódigo Verificación")
    print("-" * 150)  # Línea divisoria
    
    # Imprimir cada fila de resultados con tabuladores
    for fila in resultados:
        print(
            f"{fila[0]}\t\t{fila[1]}\t\t{fila[2]}\t\t{fila[3]}\t\t{fila[4]}\t\t{fila[5]}\t\t{fila[6]}\t\t{fila[7]}\t\t{fila[8]}\t\t{fila[9]}"
        )
    
    db.desconectar()
    
def iniciar_sesion():
    print("\n--- Iniciar Sesión ---")
    cuil_o_email = input("Ingrese su CUIL o email: ")
    password = input("Ingrese su contraseña: ")
                
    operaciones.iniciar_sesion(cuil_o_email, password) 
        
def recuperar_password():
    print("\n--- Recuperar Contraseña ---")
    cuil_o_email = input("Ingrese su cuil o email: ")
    operaciones.solicitar_codigo_verificacion(cuil_o_email)
    operaciones.recuperar_password(cuil_o_email)


def crear_usuario():
    print("\n--- Crear Usuario ---")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su número de CUIL: ")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
                
    operaciones.crear_usuario(nombre, apellido, cuil, email, password)

# Funciones Usuarios Conectados

# Función para mostrar cotizaciones históricas de una acción

def datos_cuenta():
    print(f"Nombre: {usuario.nombre} {usuario.apellido}")
    print(f"Saldo: {usuario.saldo}")
    
# Esta función es para simular que se agrega saldo, en la realidad se deberían realizar mas comprobaciones como pago efectuado y mas
def depositar_saldo():
    print("\n--- Depositar Saldo en la Cuenta ---")
    print(f"Tu saldo actual es de {usuario.saldo}")
    try:
        saldo_a_depositar = Decimal(input("Monto a depositar: ")).quantize(Decimal('0.01'))
        if saldo_a_depositar <= 0:
            print("Error: El monto a depositar debe ser positivo.")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    confirmar_pago = input("\n1. Si \n2. No \n¿Desea confirmar el deposito?: ")
    
    if confirmar_pago == "1":
        db.conectar()
        consulta = "UPDATE Usuario SET saldo = saldo + %s WHERE idUsuario = %s"
        
        # Actualiza el saldo en la DB
        db.ejecutar_consulta(consulta, (saldo_a_depositar, usuario.id))
        
        # Actualiza el saldo en la instancia usuario
        usuario.saldo += saldo_a_depositar
        print(f"Se han cargado {saldo_a_depositar:.2f} en la cuenta. Tu nuevo saldo es de {usuario.saldo:.2f}.")
        
        db.desconectar()
    else:
        print("Depósito cancelado.")

def mostrar_transacciones():
    db.conectar()
    consulta = "SELECT tipoTransaccion, cantidad, precio, fechaOperacion FROM Transaccion WHERE idUsuario = %s"
    resultados = db.obtener_datos(consulta, (usuario.id,))
    print(f"\n--- Transacciones del Usuario ---")
    for fila in resultados:
        print(fila)
    db.desconectar()

def mostrar_portafolio():
    query = """
    SELECT u.nombre, a.nombre AS accion, p.cantidad 
    FROM Usuario u
    JOIN Portafolio p ON u.idUsuario = p.idUsuario
    JOIN Accion a ON p.idAccion = a.idAccion
    WHERE u.idUsuario = %s
    """
    print(f"\n--- Portafolio de {usuario.nombre} {usuario.apellido} ---")
    db.conectar()
    portafolio = db.obtener_datos(query, (usuario.id, ))
    for item in portafolio:
        print(f"Acción: {item[1]}\t-\tCantidad: {item[2]}")
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
    
def comprar_accion():
    print("\n--- Comprar Acción ---")
    # Mostrar acciones disponibles
    mostrar_acciones_disponibles()

    # ID de la acción que el usuario quiere comprar y la cantidad
    id_accion = input("Ingrese el ID de la acción que desea comprar: ")
    cantidad = input("Ingrese la cantidad que desea comprar: ")

    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return

    # Verifica si la acción existe y obtener su precio
    db.conectar()
    consulta_accion = "SELECT precio_actual FROM Accion WHERE idAccion = %s"
    accion_data = db.obtener_datos(consulta_accion, (id_accion,))
    if not accion_data:
        print("Error: La acción seleccionada no existe.")
        db.desconectar()
        return

    precio_accion = accion_data[0][0]

    # Calcula el costo total
    costo_total = Decimal(precio_accion) * cantidad
    print(f"El costo total de la compra es: {costo_total:.2f}")

    # Verifica si el usuario tiene suficiente saldo
    if usuario.saldo < costo_total:
        print("Error: No tienes suficiente saldo para realizar esta compra.")
        db.desconectar()
        return

    # Confirmar la compra
    confirmar_compra = input(f"Confirmar compra de {cantidad} acciones a {precio_accion:.2f} cada una por un total de {costo_total:.2f}. \n1. Sí \n2. No \n¿Deseas continuar? ")

    if confirmar_compra == "1":
        # Descuenta el saldo de la cuenta
        db.conectar()
        consulta_actualizar_saldo = "UPDATE Usuario SET saldo = saldo - %s WHERE idUsuario = %s"
        db.ejecutar_consulta(consulta_actualizar_saldo, (costo_total, usuario.id))

        # Agrega la acción al portafolio del usuario
        consulta_portafolio = """
        INSERT INTO Portafolio (idUsuario, idAccion, cantidad) 
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE cantidad = cantidad + %s
        """
        db.ejecutar_consulta(consulta_portafolio, (usuario.id, id_accion, cantidad, cantidad))

        # Registra la transacción en la base de datos
        consulta_transaccion = """
        INSERT INTO Transaccion (idUsuario, tipoTransaccion, cantidad, precio, fechaOperacion) 
        VALUES (%s, 'Compra', %s, %s, NOW())
        """
        db.ejecutar_consulta(consulta_transaccion, (usuario.id, cantidad, precio_accion))

        # Actualiza el saldo en la instancia usuario
        usuario.saldo -= costo_total
        print(f"Compra realizada con éxito. Tu nuevo saldo es de {usuario.saldo:.2f}.")
        db.desconectar()
    else:
        print("Compra cancelada.")
    
def cambiar_password():
    print("\n--- Cambiar Contraseña ---")
    password_actual = input("Ingrese su contraseña actual: ")
    nueva_password = input("Ingrese su nueva contraseña: ")
        
    operaciones.cambiar_password_conectado(usuario.id, password_actual, nueva_password)



if __name__ == "__main__":
    mostrar_menu()
 # menu.py

from broker import Usuario, Accion_de_empresa, Transaccion, Porfolio

def mostrar_menu():
    print("\nBienvenido al ARG Broker, ¿qué desea hacer?")
    print("1. Ver datos de la cuenta")
    print("2. Ver portafolio")
    print("3. Comprar acciones")
    print("4. Vender acciones")
    print("5. Salir")

def mostrar_acciones_disponibles():
    acciones = {
        '1': Accion_de_empresa('TechCorp', 1, 150.5, 1000),
        '2': Accion_de_empresa('HealthInc', 1, 220.0, 1000),
        '3': Accion_de_empresa('EcoEnergy', 1, 305.75, 1000),
        '4': Accion_de_empresa('FinServ', 1, 100.0, 1000)
    }
    print("\n--- Acciones Disponibles ---")
    for key, accion in acciones.items():
        print(f"{key}. {accion.nombre_accion_empresa} - Cotización: ${accion.cotizacion}")
    return acciones

def seleccionar_accion(acciones):
    opcion = input("Selecciona el número de la acción: ")
    if opcion in acciones:
        return acciones[opcion]
    else:
        print("Opción inválida. Intente nuevamente.")
        return seleccionar_accion(acciones)

def menu(usuario, porfolio):
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("\n--- Datos de la Cuenta ---")
            print(f"Saldo: {usuario.saldo}")
            print(f"Total invertido: {usuario.total_invertido}")
            print(f"Rendimiento total: {usuario.rendimiento_total}%")
        
        elif opcion == '2':
            print("\n--- Portafolio ---")
            historial = porfolio.historial()
            print(f"Acciones compradas: {historial['compradas']}")
            print(f"Acciones vendidas: {historial['vendidas']}")
            print(f"Ganancias: {historial['ganancias']}")

        elif opcion == '3':
            print("\n--- Comprar Acciones ---")
            acciones = mostrar_acciones_disponibles()
            accion = seleccionar_accion(acciones)
            cantidad = int(input(f"¿Cuántas acciones de {accion.nombre_accion_empresa} deseas comprar? "))
            transaccion = Transaccion("2024-10-14", 10, 0)  # Comision del broker
            try:
                transaccion.compra(accion, cantidad, usuario)
                porfolio.agregar_accion_comprada(accion, cantidad)
                print(f"Compra realizada exitosamente: {cantidad} acciones de {accion.nombre_accion_empresa}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '4':
            print("\n--- Vender Acciones ---")
            acciones = mostrar_acciones_disponibles()
            accion = seleccionar_accion(acciones)
            cantidad = int(input(f"¿Cuántas acciones de {accion.nombre_accion_empresa} deseas vender? "))
            transaccion = Transaccion("2024-10-14", 10, 0)  # Comision del broker
            try:
                transaccion.venta(accion, cantidad, usuario)
                porfolio.agregar_accion_vendida(accion, cantidad)
                print(f"Venta realizada exitosamente: {cantidad} acciones de {accion.nombre_accion_empresa}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '5':
            print("Saliendo del menú...")
            break

        else:
            print("Opción inválida.")

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear un usuario de ejemplo
    usuario = Usuario("Juan", "juan@email.com", "123 Calle", 123456)
    porfolio = Porfolio()

    # Realizar un depósito inicial para tener saldo
    usuario.deposito_inicial(1000)

    # Ejecutar el menú
    menu(usuario, porfolio)
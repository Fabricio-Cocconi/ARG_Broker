from operaciones_usuario import OperacionesUsuarioDB

operaciones = OperacionesUsuarioDB()

def mostrar_menu():
    while True:
        if not operaciones.sesion.es_activa():
            print("\nBienvenido!")
            print("1. Mostrar datos de usuarios de prueba")
            print("2. Iniciar sesión")
            print("3. Recuperar contraseña")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                operaciones.mostrar_usuarios()
            elif opcion == "2":
                print("\n--- Iniciar Sesión ---")
                cuil_o_email = input("Ingrese su CUIL o email: ")
                password = input("Ingrese su contraseña: ")
                
                operaciones.iniciar_sesion(cuil_o_email, password)
                # if operaciones.iniciar_sesion(cuil_o_email, password):
                    # print("Sesión iniciada exitosamente.")
                # else:
                    # print("Error en el inicio de sesión. Intente nuevamente.")
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
            print("1. Cambiar contraseña")
            print("2. Cerrar sesión")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cambiar_password()
            elif opcion == "2":
                operaciones.cerrar_sesion()
            elif opcion == "3":
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

# Iniciar el menú
if __name__ == "__main__":
    # Iniciar el menú principal
    mostrar_menu()
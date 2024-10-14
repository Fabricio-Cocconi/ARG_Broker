def registrar_usuario(usuarios):
    print("\n--- Registro de Nuevo Inversor ---")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cuil = input("Ingrese CUIL: ")
    email = input("Ingrese email: ")
    contraseña = input("Ingrese contraseña: ")
    
    # Creación de un nuevo usuario con los datos proporcionados
    usuario = Usuario(nombre, apellido, cuil, email, contraseña)
    
    # Asignación de un portafolio vacío al usuario
    usuario.portafolio = Portafolio()
    
    # Añadir el nuevo usuario a la lista de usuarios
    usuarios.append(usuario)
    
    print("Usuario registrado exitosamente.\n")

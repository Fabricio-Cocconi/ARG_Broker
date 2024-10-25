from usuario import Usuario
from accion import Accion
from transaccion import Transaccion
from datos import Datos 

def registrar_usuario():
    id = len(Datos.cargar_datos('usuarios.dat')) + 1
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su CUIL: ")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    nuevo_usuario = Usuario(id, nombre, apellido, cuil, email, password)
    usuarios = Datos.cargar_datos('usuarios.dat')
    usuarios.append(nuevo_usuario)
    Datos.guardar_datos(usuarios, 'usuarios.dat')
    print("Usuario registrado exitosamente.")

def iniciar_sesion():
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    usuarios = Datos.cargar_datos('usuarios.dat')
    for usuario in usuarios:
        if usuario.email == email and usuario.password == password:
            print("Inicio de sesión exitoso.")
            return usuario
    print("Email o contraseña incorrectos.")
    return None

def mostrar_datos_cuenta(usuario):
    print(f"Saldo: ${usuario.saldo:.2f}")
    total_invertido = sum([detalles['valor'] for detalles in usuario.portafolio.values()])
    rendimiento_total = sum([(detalles['valor'] / detalles['cantidad']) for detalles in usuario.portafolio.values()])
    print(f"Total Invertido: ${total_invertido:.2f}")
    print(f"Rendimiento Total: ${rendimiento_total:.2f}")

def listar_activos(usuario):
    for simbolo, detalles in usuario.portafolio.items():
        print(f"Acción: {simbolo}, Cantidad: {detalles['cantidad']}, Valor: ${detalles['valor']:.2f}")

def comprar_acciones(usuario):
    simbolo = input("Ingrese el símbolo de la acción: ")
    cantidad = int(input("Ingrese la cantidad de acciones: "))
    precio_compra = float(input("Ingrese el precio de compra: "))
    total = cantidad * precio_compra
    comision = total * 0.015
    if usuario.saldo >= (total + comision):
        usuario.saldo -= (total + comision)
        if simbolo in usuario.portafolio:
            usuario.portafolio[simbolo]['cantidad'] += cantidad
            usuario.portafolio[simbolo]['valor'] += total
        else:
            usuario.portafolio[simbolo] = {'cantidad': cantidad, 'valor': total}
        transaccion = Transaccion(usuario.id, simbolo, 'compra', cantidad, total)
        transacciones = Datos.cargar_datos('transacciones.dat')
        transacciones.append(transaccion)
        Datos.guardar_datos(transacciones, 'transacciones.dat')
        print(f"Compraste {cantidad} acciones de {simbolo} a ${precio_compra:.2f} cada una.")
    else:
        print("Saldo insuficiente.")

def vender_acciones(usuario):
    simbolo = input("Ingrese el símbolo de la acción: ")
    cantidad = int(input("Ingrese la cantidad de acciones: "))
    precio_venta = float(input("Ingrese el precio de venta: "))
    if simbolo in usuario.portafolio and usuario.portafolio[simbolo]['cantidad'] >= cantidad:
        total = cantidad * precio_venta
        comision = total * 0.015
        usuario.saldo += (total - comision)
        usuario.portafolio[simbolo]['cantidad'] -= cantidad
        usuario.portafolio[simbolo]['valor'] -= total
        if usuario.portafolio[simbolo]['cantidad'] == 0:
            del usuario.portafolio[simbolo]
        transaccion = Transaccion(usuario.id, simbolo, 'venta', cantidad, total)
        transacciones = Datos.cargar_datos('transacciones.dat')
        transacciones.append(transaccion)
        Datos.guardar_datos(transacciones, 'transacciones.dat')
        print(f"Vendiste {cantidad} acciones de {simbolo} a ${precio_venta:.2f} cada una.")
    else:
        print("No tienes suficientes acciones para vender.")

def main():
    while True:
        print("\nMenú Principal:")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            usuario = iniciar_sesion()
            if usuario:
                while True:
                    print("\nMenú de Usuario:")
                    print("1. Mostrar Datos de la Cuenta")
                    print("2. Listar Activos del Portafolio")
                    print("3. Comprar Acciones")
                    print("4. Vender Acciones")
                    print("5. Cerrar Sesión")
                    opcion_usuario = input("Seleccione una opción: ")
                    
                    if opcion_usuario == '1':
                        mostrar_datos_cuenta(usuario)
                    elif opcion_usuario == '2':
                        listar_activos(usuario)
                    elif opcion_usuario == '3':
                        comprar_acciones(usuario)
                    elif opcion_usuario == '4':
                        vender_acciones(usuario)
                    elif opcion_usuario == '5':
                        break
                    else:
                        print("Opción no válida.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

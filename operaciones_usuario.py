from db_connection import ConectarDB        
from datetime import datetime, timedelta
import random
import string

class OperacionesUsuarioDB:
    def __init__(self):
        # Se uso self.db en lugar de una variable para que la conexión este activa mientras la instancia de clase este en uso
        self.db = ConectarDB()
        self.db.conectar()

    def __del__(self):
        # Antes de eliminar la instancia de OperacionesDB se asegura de cerrar la conexión con la base de datos
        # y de paso sea "global" dentro de la clase y poder usarla en todos los metodos
        self.db.desconectar()

    def mostrar_usuarios(self):
        consulta_select = "SELECT * FROM Usuario"
        resultados = self.db.obtener_datos(consulta_select)
        print("Usuarios disponibles en la base de datos: ")
        for fila in resultados:
            print(fila)
            
    def crear_usuario(self, nombre, apellido, cuil, email, password, saldo=0):
        # Consulta de inserción
        consulta = """
        INSERT INTO Usuario (nombre, apellido, cuil, email, password, saldo) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (nombre, apellido, cuil, email, password, saldo)
        
        # Ejecutar la consulta
        self.db.ejecutar_consulta(consulta, valores)
        print(f"Usuario {nombre} {apellido} creado exitosamente.")

    def iniciar_sesion(self, cuil_o_email, password):
        consulta = "SELECT * FROM Usuario WHERE cuil = %s OR email = %s"
        valores = (cuil_o_email, cuil_o_email)
        resultados = self.db.obtener_datos(consulta, valores)
        
        if resultados:
            usuario = resultados[0]
            hora_bloqueado = usuario[8]
            intentos = usuario[7]

            # Verifica si el usuario está bloqueado temporalmente
            if hora_bloqueado is not None:
                tiempo_actual = datetime.now()
                tiempo_desbloqueo = hora_bloqueado + timedelta(minutes=15)  # Bloqueo de 15 minutos
                
                if tiempo_actual < tiempo_desbloqueo:
                    tiempo_restante = (tiempo_desbloqueo - tiempo_actual).seconds // 60
                    print(f"Cuenta bloqueada. Intenta de nuevo en {tiempo_restante} minutos.")
                    return False
                else:
                    # Si el tiempo de bloqueo ha pasado, resetear intentos
                    self.db.ejecutar_consulta("UPDATE Usuario SET intentos_fallidos = 0, hora_bloqueado = NULL WHERE idUsuario = %s", (usuario[0],))
                    print("Cuenta desbloqueada. Puedes intentar iniciar sesión nuevamente.")

            # Verifica la contraseña
            if usuario[5] == password: 
                print("Inicio de sesión exitoso")
                # Resetear intentos fallidos
                self.db.ejecutar_consulta("UPDATE Usuario SET intentos_fallidos = 0 WHERE idUsuario = %s", (usuario[0],))
                return True
            else:
                # Incrementar intentos fallidos
                intentos += 1
                self.db.ejecutar_consulta("UPDATE Usuario SET intentos_fallidos = %s WHERE idUsuario = %s", (intentos, usuario[0]))
                
                if intentos >= 3:
                    # Guardar la hora del bloqueo
                    self.db.ejecutar_consulta("UPDATE Usuario SET hora_bloqueado = %s WHERE idUsuario = %s", (datetime.now(), usuario[0]))
                    print("La cuenta ha sido bloqueada por tres intentos fallidos.")
                else:
                    print(f"Credenciales incorrectas. Intentos fallidos: {intentos}")
                return False
        else:
            print("Credenciales incorrectas")
            return False
        
    def generar_codigo_verificacion(self):
        # Genera un código aleatorio de 4 dígitos
        return ''.join(random.choice(string.digits) for _ in range(4))

    def solicitar_codigo_verificacion(self, cuil_o_email):
        # Simula la solicitud de un código de verificación
        consulta = "SELECT * FROM Usuario WHERE cuil = %s OR email = %s"
        valores = (cuil_o_email, cuil_o_email)
        resultados = self.db.obtener_datos(consulta, valores)

        if resultados:
            usuario = resultados[0]
            codigo = self.generar_codigo_verificacion()
            
            # Guarda el código de verificación en la base de datos
            self.db.ejecutar_consulta("UPDATE Usuario SET codigo_verificacion = %s WHERE idUsuario = %s", 
                                      (codigo, usuario[0]))
            print(f"Se ha generado un código de verificación para el usuario {usuario[1]} {usuario[2]}.")
            print(f"Código de verificación (simulado): {codigo}")
        else:
            print("Usuario no encontrado.")

    def cambiar_password_por_codigo(self, cuil_o_email):
        # Este metodo es para que pueda cambiar la contraseña quien lo hace mediante la recuperación de contraseña
        consulta = "SELECT * FROM Usuario WHERE cuil = %s OR email = %s"
        valores = (cuil_o_email, cuil_o_email)
        resultados = self.db.obtener_datos(consulta, valores)

        if resultados:
            usuario = resultados[0]
            codigo_guardado = usuario[9]

            codigo_ingresado = input("Ingrese el código de verificación: ")
            
            if codigo_ingresado == codigo_guardado:
                nuevo_password = input("Ingrese su nueva contraseña: ")
                self.db.ejecutar_consulta("UPDATE Usuario SET password = %s, codigo_verificacion = NULL WHERE idUsuario = %s", 
                                          (nuevo_password, usuario[0]))
                print("Contraseña cambiada con éxito.")
            else:
                print("Código de verificación incorrecto.")
        else:
            print("Usuario no encontrado.")

    def cambiar_password_conectado(self, usuario_id, password_actual, nueva_password):
        consulta = "SELECT password FROM Usuario WHERE idUsuario = %s"
        valores = (usuario_id,)
        resultados = self.db.obtener_datos(consulta, valores)

        if resultados:
            password_guardado = resultados[0][0]

            # Verificar si la contraseña actual es correcta
            if password_actual == password_guardado:
                self.db.ejecutar_consulta("UPDATE Usuario SET password = %s WHERE idUsuario = %s", 
                                          (nueva_password, usuario_id))
                print("Contraseña cambiada con éxito.")
            else:
                print("La contraseña actual es incorrecta.")
        else:
            print("Usuario no encontrado.")


# Prueba conexión y muestra usuarios de la base
if __name__ == "__main__":
    operaciones = OperacionesUsuarioDB()
    operaciones.mostrar_usuarios()
    operaciones.iniciar_sesion(2, "d1234")

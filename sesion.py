class Sesion:
    def __init__(self):
        self.usuario = None  # Guardará los datos del usuario en sesión

    def iniciar(self, usuario):
        self.usuario = usuario

    def cerrar(self):
        self.usuario = None

    def es_activa(self):
        return self.usuario is not None
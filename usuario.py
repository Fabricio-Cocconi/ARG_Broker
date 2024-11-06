class Usuario:
    def __init__(self, id=None, nombre=None, apellido=None, cuil=None, email=None, saldo=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.email = email
        self.saldo = saldo
        self.portafolio = {}

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Email: {self.email}, Saldo: ${self.saldo:.2f}'

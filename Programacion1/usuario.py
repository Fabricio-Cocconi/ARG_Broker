class Usuario:
    def __init__(self, id, nombre, apellido, cuil, email, password):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.email = email
        self.password = password
        self.saldo = 1000000.00  # Saldo inicial de $1,000,000
        self.portafolio = {}

    def __str__(self):
        return f'ID: {self.id}, Nombre: {self.nombre} {self.apellido}, Email: {self.email}, Saldo: ${self.saldo:.2f}'

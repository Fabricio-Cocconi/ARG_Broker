import datetime

class Transaccion:
    def __init__(self, usuario_id, accion, tipo, cantidad, precio):
        self.usuario_id = usuario_id
        self.accion = accion
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio
        self.comision = precio * 0.015
        self.fecha = datetime.datetime.now()

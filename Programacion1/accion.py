class Accion:
    def __init__(self, simbolo, nombre, ultimo_operado, cant_compra_diaria, precio_compra_actual, precio_venta_actual, cant_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        self.simbolo = simbolo
        self.nombre = nombre
        self.ultimo_operado = ultimo_operado
        self.cant_compra_diaria = cant_compra_diaria
        self.precio_compra_actual = precio_compra_actual
        self.precio_venta_actual = precio_venta_actual
        self.cant_venta_diaria = cant_venta_diaria
        self.apertura = apertura
        self.minimo_diario = minimo_diario
        self.maximo_diario = maximo_diario
        self.ultimo_cierre = ultimo_cierre

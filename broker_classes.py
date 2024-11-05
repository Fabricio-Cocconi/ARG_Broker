class Usuario:
    def __init__(self, nombre, cuil, email, direccion, cuenta_bancaria):
        self.nombre = nombre
        self.cuil = cuil
        self.email = email
        self.direccion = direccion
        self.__cuenta_bancaria = cuenta_bancaria
        self.saldo = 0.0
        self.total_invertido = 0.0
        self.rendimiento_total = 0.0
    
    def deposito_inicial(self, cantidad):
        self.saldo += cantidad
        return self.saldo


class Accion_de_empresa:
    def __init__(self, nombre_accion_empresa, minimo_compra, cotizacion, maximo_compra):
        self.nombre_accion_empresa = nombre_accion_empresa
        self.minimo_compra = minimo_compra
        self.cotizacion = cotizacion
        self.maximo_compra = maximo_compra

    def rendimiento(self, precio_compra):
        return (self.cotizacion - precio_compra) / precio_compra * 100


class Transaccion:
    def __init__(self, fecha, comision_broker, intereses_ganados):
        self.fecha = fecha
        self.comision_broker = comision_broker
        self.intereses_ganados = intereses_ganados

    def compra(self, accion, cantidad, usuario):
        total_compra = (accion.cotizacion * cantidad) + self.comision_broker
        if usuario.saldo >= total_compra:
            usuario.saldo -= total_compra
            usuario.total_invertido += total_compra
            return total_compra
        else:
            raise ValueError("Saldo insuficiente")
    
    def venta(self, accion, cantidad, usuario):
        total_venta = (accion.cotizacion * cantidad) - self.comision_broker
        usuario.saldo += total_venta
        return total_venta


class Porfolio:
    def __init__(self):
        self.acciones_compradas = {}
        self.acciones_vendidas = {}
        self.ganancias = 0.0

    def agregar_accion_comprada(self, accion, cantidad):
        if accion.nombre_accion_empresa in self.acciones_compradas:
            self.acciones_compradas[accion.nombre_accion_empresa] += cantidad
        else:
            self.acciones_compradas[accion.nombre_accion_empresa] = cantidad

    def agregar_accion_vendida(self, accion, cantidad):
        if accion.nombre_accion_empresa in self.acciones_vendidas:
            self.acciones_vendidas[accion.nombre_accion_empresa] += cantidad
        else:
            self.acciones_vendidas[accion.nombre_accion_empresa] = cantidad

    def historial(self):
        return {
            "compradas": self.acciones_compradas,
            "vendidas": self.acciones_vendidas,
            "ganancias": self.ganancias
        }

#prueba
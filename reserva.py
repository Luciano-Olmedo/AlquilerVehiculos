class Reserva:

    def __init__(self, id_reserva, cliente, vehiculo, dias):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.dias = dias

    def calcular_total(self):
        return self.vehiculo.calcular_costo(self.dias)

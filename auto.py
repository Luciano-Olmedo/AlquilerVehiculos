from vehiculo import Vehiculo


class Auto(Vehiculo):

    def calcular_costo(self, dias):
        return self.get_tarifa_dia() * dias

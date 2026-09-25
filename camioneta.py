from vehiculo import Vehiculo


class Camioneta(Vehiculo):

    def calcular_costo(self, dias):
        costo = self.get_tarifa_dia() * dias
        return costo * 1.20

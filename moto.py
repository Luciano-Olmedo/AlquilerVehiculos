from vehiculo import Vehiculo


class Moto(Vehiculo):

    def calcular_costo(self, dias):
        costo = self.get_tarifa_dia() * dias
        return costo * 0.90

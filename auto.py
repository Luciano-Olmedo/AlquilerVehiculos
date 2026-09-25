from vehiculo import Vehiculo

class Auto(Vehiculo):

    def calcular_costo(self, dias):
        return self.tarifa_dia * dias

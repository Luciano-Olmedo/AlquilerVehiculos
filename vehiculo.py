from estadoVehiculo import EstadoVehiculo

class Vehiculo:

    def __init__(self, patente, marca, modelo, tarifa_dia):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.__tarifa_dia = tarifa_dia

    def get_tarifa_dia(self):
        return self.__tarifa_dia

    def set_tarifa_dia(self, tarifa_dia):
        self.__tarifa_dia = tarifa_dia

    def calcular_costo(self, dias):
        return self.__tarifa_dia * dias

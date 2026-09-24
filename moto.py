from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, tipoVehiculo, patente, marca, modelo, tarifa_dia, estado):
        super().__init__(tipoVehiculo, patente, marca, modelo, tarifa_dia, estado)
        

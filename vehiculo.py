

class Vehiculo:

    def __init__(self, patente, marca, modelo, tarifa_dia):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.__tarifa_dia = tarifa_dia    
  
    @property
    def tarifa_dia(self):
        return self.__tarifa_dia
   
    @tarifa_dia.setter
    def tarifa_dia(self, tarifa_dia):
        if tarifa_dia <= 0:
            raise ValueError("La tarifa diaria debe ser mayor a 0")

        self.__tarifa_dia = tarifa_dia

    def calcular_costo(self, dias):
        if dias < 0:
            return False

        return dias * self.tarifa_dia
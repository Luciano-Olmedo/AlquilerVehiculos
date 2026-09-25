from auto import Auto
from moto import Moto
from camioneta import Camioneta


class Sucursal:

    def __init__(self, codigo, ciudad, direccion):
        self.codigo = codigo
        self.ciudad = ciudad
        self.direccion = direccion

        self.vehiculos = [
      
            Auto("AE456FR", "Toyota", "Etios", 100000),        
            Auto("AE783SD", "Fiat", "Cronos", 95000),            
            Moto("AF457CX", "Honda", "Wave", 25000),
            Moto("AF749LS", "Yamaha", "FZ", 35000),          
            Camioneta("AH325LP", "Toyota", "Hilux", 220000),
            Camioneta("AI646QR", "Volkswagen", "Amarok", 210000)
        ]


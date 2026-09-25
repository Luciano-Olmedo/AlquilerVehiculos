from estadoVehiculo import EstadoVehiculo


class Vehiculo:
    def __init__(self,patente,marca,modelo,tarifa_dia):            
        self.patente=patente
        self.marca= marca
        self.modelo= modelo
        self.tarifa_dia = tarifa_dia       
        self.estado = EstadoVehiculo.DISPONIBLE     
        
        
        
    def calcular_costo(self,dias):    
      if dias < 0:
         return False
      return self.tarifa_dia * dias
      
            
    
    

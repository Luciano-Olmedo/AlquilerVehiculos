from estadoReserva import EstadoReserva

class Reserva():
    def __init__(self,id_reserva,fecha,hora,estado,descripcion):     
     self.id_reserva = id_reserva
     self.fecha= fecha
     self.hora= hora
     self.descripcion= descripcion
     self.estado = estado
     
from enum import Enum

class EstadoReserva(Enum):
    SOLICITADA = "Solicitada"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    FINALIZADA = "Finalizada"
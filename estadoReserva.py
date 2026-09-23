from enum import Enum

class EstadoReserva(Enum):
  SOLICITADA = "Solicitada"
  CONFIRMADA = "Confirmada"
  EN_CURSO = "En curso"
  FINALIZADA = "Finalizada"
  CANCELADA= "Cancelada"
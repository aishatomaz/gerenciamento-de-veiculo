from .veiculo import Veiculo
from .motorista import Motorista
from .viagem import Viagem
from .estado import EstadoVeiculo
from .carro import Carro
from .moto import Moto
from .caminhao import Caminhao
from .mixins import AbastecivelMixin, ManutenivelMixin

__all__ = [
    "Veiculo",
    "Motorista",
    "Viagem",
    "EstadoVeiculo",
    "Carro",
    "Moto",
    "Caminhao",
    "AbastecivelMixin",
    "ManutenivelMixin"
]

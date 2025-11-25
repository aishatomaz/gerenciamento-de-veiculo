from .veiculo import Veiculo
from .mixins import ManutenivelMixin, AbastecivelMixin

class Moto(Veiculo, ManutenivelMixin, AbastecivelMixin):
    """
    Representa uma motocicleta. Requer CNH "A" e herda as funcionalidades
    necessárias.
    """
    def __init__(self, placa, marca, modelo, ano, quilometragem, consumo_medio):
        super().__init__(placa, marca, modelo, ano, quilometragem, consumo_medio, tipo='Moto')
        ManutenivelMixin.__init__(self)
        AbastecivelMixin.__init__(self)
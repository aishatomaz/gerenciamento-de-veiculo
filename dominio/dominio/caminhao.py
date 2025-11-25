from .veiculo import Veiculo
from .mixins import ManutenivelMixin, AbastecivelMixin

class Caminhao(Veiculo, ManutenivelMixin, AbastecivelMixin):
    """
    Representa um caminhão de carga. Requer CNH "C" ou superior.
    """
    def __init__(self, placa, marca, modelo, ano, quilometragem, consumo_medio):
        super().__init__(placa, marca, modelo, ano, quilometragem, consumo_medio, tipo='Caminhao')
        ManutenivelMixin.__init__(self)
        AbastecivelMixin.__init__(self)
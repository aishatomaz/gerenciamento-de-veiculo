from .veiculo import Veiculo
from .mixins import ManutenivelMixin, AbastecivelMixin

class Carro(Veiculo, ManutenivelMixin, AbastecivelMixin):
    """
    Representa um carro de passeio. Herda de Veiculo e utiliza mixins
    para herança múltipla.
    """
    def __init__(self, placa, marca, modelo, ano, quilometragem, consumo_medio):
        super().__init__(placa, marca, modelo, ano, quilometragem, consumo_medio, tipo='Carro')
        ManutenivelMixin.__init__(self)
        AbastecivelMixin.__init__(self)
        
class Carro(Veiculo):
    def tipo(self):
        return "carro"

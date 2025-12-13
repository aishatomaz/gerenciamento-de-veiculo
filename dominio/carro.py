from .veiculo import Veiculo
from .mixins import ManutenivelMixin, AbastecivelMixin
from typing import Iterator

class Carro(Veiculo, ManutenivelMixin, AbastecivelMixin):
    def __init__(self, placa, marca, modelo, ano, quilometragem=0.0, consumo_medio=0.0):
        super().__init__(placa, marca, modelo, 'Carro', ano, quilometragem, consumo_medio)
        AbastecivelMixin.__init__(self) 
        ManutenivelMixin.__init__(self) 
    
    def __iter__(self) -> Iterator[str]:
        return iter(self.historico_eventos + [f"Maint.: {m['data']}" for m in self.historico_manutencoes])

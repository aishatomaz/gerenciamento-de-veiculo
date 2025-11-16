from datetime import date
from .veiculo import Veiculo
from .motorista import Motorista

class Viagem:
    """
    Registra uma viagem realizada, contendo informações de alocação
    e distância percorrida.
    """
    def __init__(self, veiculo: Veiculo, motorista: Motorista, origem: str, destino: str, distancia: float, data: date):
        self._veiculo = veiculo
        self._motorista = motorista
        self._distancia_percorrida = distancia
        # Outros atributos...
        pass

    def atualizar_quilometragem(self) -> None:
        """
        Atualiza a quilometragem do veículo após a conclusão da viagem.
        """
        pass
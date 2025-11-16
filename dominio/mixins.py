from datetime import date
from typing import Any

class AbastecivelMixin:
    """
    Mixin para adicionar a funcionalidade de registrar abastecimentos
    e gerenciar o histórico de um veículo.
    """
    def __init__(self):
        # Inicializa o histórico de abastecimentos
        self._historico_abastecimentos = []

    def abastecer(self, data: date, litros: float, valor_pago: float) -> None:
        """
        Registra um novo evento de abastecimento e, futuramente, 
        recalcula o consumo médio.
        """
        pass

class ManutenivelMixin:
    """
    Mixin para gerenciar o histórico de manutenções e o controle de
    status (ativo/manutencao) de um veículo.
    """
    def __init__(self):
        # Inicializa o histórico de manutenções
        self._historico_manutencoes = []

    def registrar_manutencao(self, tipo: str, custo: float, descricao: str) -> None:
        """
        Registra uma manutenção e atualiza o status do veículo (deve
        mudar o status para MANUTENCAO e depois para ATIVO).
        """
        pass
    
    def __iter__(self) -> Any:
        """
        Método especial (__iter__) para iterar sobre o histórico de manutenções,
        conforme o requisito de POO.
        """
        pass
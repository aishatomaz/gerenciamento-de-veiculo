from typing import Any
from .estado import EstadoVeiculo

class Veiculo:
    """
    Classe base para todos os veículos da frota. Aplica encapsulamento
    e define atributos e métodos especiais comuns.
    """
    def __init__(self, placa, marca, modelo, ano, quilometragem, consumo_medio, float, tipo):
        """
        Inicializa um veículo com seus dados mínimos.
        O tipo deve ser ('Carro', 'Moto' ou 'Caminhao').
        """
        self._placa = placa          # Atributo chave
        self._quilometragem = quilometragem
        self._consumo_medio = consumo_medio
        self._status = EstadoVeiculo.ATIVO
        self._tipo = tipo
        # Outros atributos...
        pass

    @property
    def quilometragem_atual (self):
        """
        Novos dados atribuídos a quilometragem do veículo
        """
        self.quilometragem_atual += quilometragem

    
    def __str__(self) -> str:
        """Método especial para fornecer um resumo legível do veículo."""
        pass

    def __repr__(self) -> str:
        """Método especial para representação formal."""
        pass

    def __eq__(self, other: Any) -> bool:
        """Método especial para comparar veículos pela placa."""
        pass

    def __lt__(self, other: Any) -> bool:
        """Método especial para ordenar por quilometragem."""
        pass

    # No futuro, adicionar métodos com @property para acessar atributos privados.

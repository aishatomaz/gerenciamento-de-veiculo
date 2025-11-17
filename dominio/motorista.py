from typing import List, Any
from .veiculo import Veiculo

class Pessoa:
    """Classe base para herança Motorista."""
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf
        pass

class Motorista(Pessoa):
    """
    Representa um motorista na frota. Contém lógica de validação de CNH
    e histórico de viagens.
    """
    def __init__(self, nome: str, cpf: str, cnh_categoria: str, tempo_experiencia: int):
        super().__init__(nome, cpf)
        self._cnh_categoria = cnh_categoria
        self._historico_viagens = [] # Armazena objetos viagem
        self._disponibilidade = True
        pass

    def pode_dirigir(self, veiculo: Veiculo) -> bool:
        """
        Valida se a CNH do motorista é compatível com o tipo de veículo.
        """
        pass

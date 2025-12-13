from enum import Enum

class EstadoVeiculo(Enum):
    """
    Define os estados possíveis de um veículo, conforme as regras de negócio:
    ATIVO, MANUTENCAO, INATIVO.
    """
    ATIVO = "Ativo"
    MANUTENCAO = "Em Manutenção"
    INATIVO = "Inativo"
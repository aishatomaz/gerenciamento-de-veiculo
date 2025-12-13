from typing import List, Dict, Any
from datetime import date
from .estado import EstadoVeiculo

class AbastecivelMixin:
    """Mixin para veículos que podem ser abastecidos (RT: Herança Múltipla)."""

    def __init__(self) -> None:
        # Inicializa o histórico se não estiver sendo usado na herança múltipla
        if not hasattr(self, '_AbastecivelMixin__historico_abastecimentos'):
            self.__historico_abastecimentos: List[Dict[str, Any]] = []

    def registrar_abastecimento(self, data: date, tipo_combustivel: str, litros: float, valor: float) -> None:
        self.__historico_abastecimentos.append({
            "data": data.isoformat(),
            "tipo_combustivel": tipo_combustivel,
            "litros": litros,
            "valor": valor
        })
        self.registrar_evento(f"Abastecimento: {litros:.2f}L de {tipo_combustivel}")

    @property
    def historico_abastecimentos(self) -> List[Dict[str, Any]]:
        return list(self.__historico_abastecimentos)

class ManutenivelMixin:
    """Mixin para veículos que podem receber manutenções e ter status controlado."""

    def __init__(self) -> None:
        if not hasattr(self, '_ManutenivelMixin__historico_manutencoes'):
            self.__historico_manutencoes: List[Dict[str, Any]] = []

    def registrar_manutencao(self, data: date, tipo: str, custo: float, descricao: str) -> None:
        self.__historico_manutencoes.append({
            "data": data.isoformat(),
            "tipo": tipo,
            "custo": custo,
            "descricao": descricao
        })
        self.registrar_evento(f"Manutenção {tipo}: R${custo:.2f}. Descrição: {descricao}")
        # Veículo entra em manutenção, a menos que seja liberado
        if self.status != EstadoVeiculo.MANUTENCAO:
             self.alterar_status(EstadoVeiculo.MANUTENCAO)
        
    def liberar_manutencao(self) -> None:
        """Libera o veículo da manutenção."""
        if self.status == EstadoVeiculo.MANUTENCAO:
            self.alterar_status(EstadoVeiculo.ATIVO)
            self.registrar_evento("Veículo liberado da manutenção.")
        
    @property
    def historico_manutencoes(self) -> List[Dict[str, Any]]:
        return list(self.__historico_manutencoes)

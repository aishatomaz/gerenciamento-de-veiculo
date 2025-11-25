from typing import List, Tuple


class AbastecivelMixin:
    """
    Mixin que adiciona comportamento de abastecimento a uma classe.
    Guarda histórico de abastecimentos como tuples: (data, combustivel, litros, valor)
    """

    def __init__(self, *args, **kwargs):
        self._historico_abastecimentos: List[Tuple] = []
        super().__init__(*args, **kwargs)  # permissivo para múltipla herança

    def abastecer(self, data, combustivel: str, litros: float, valor: float) -> None:
        self._historico_abastecimentos.append((data, combustivel, float(litros), float(valor)))

    @property
    def historico_abastecimentos(self):
        return list(self._historico_abastecimentos)


class ManutenivelMixin:
    """
    Mixin que adiciona comportamento de manutenção a uma classe.
    Guarda histórico de manutenções como tuples: (data, tipo, custo, descricao)
    """

    def __init__(self, *args, **kwargs):
        self._historico_manutencoes: List[Tuple] = []
        super().__init__(*args, **kwargs)

    def registrar_manutencao(self, data, tipo: str, custo: float, descricao: str = "") -> None:
        self._historico_manutencoes.append((data, tipo, float(custo), descricao))

    @property
    def historico_manutencoes(self):
        return list(self._historico_manutencoes)

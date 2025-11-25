import json
from typing import Any, List, Optional


class JsonRepository:
    """
    Repositório muito simples para salvar/ler listas de dicionários em JSON.
    Implementação intencionalmente mínima para a Entrega 2.
    """

    def __init__(self, arquivo: str):
        self.arquivo = arquivo

    def salvar(self, dados: List[dict]) -> None:
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

    def carregar(self) -> Optional[List[dict]]:
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return None

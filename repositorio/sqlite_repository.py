"""veiculo/repositorio/sqlite_repository.py - repositório minimal sqlite"""

import sqlite3
from typing import Any, Optional


class SqliteRepository:
    """
    Camada mínima de repositório usando sqlite3.
    Implementação apenas com criação de conexão e métodos placeholders.
    """

    def __init__(self, banco: str = ":memory:"):
        self.banco = banco
        self.con = sqlite3.connect(self.banco)
        # Observação: criação de tabelas fica para etapas seguintes.

    def salvar(self, objeto: Any) -> None:
        # placeholder
        raise NotImplementedError("salvar não implementado para sqlite neste estágio.")

    def carregar(self, identificador: Any) -> Optional[Any]:
        # placeholder
        raise NotImplementedError("carregar não implementado para sqlite neste estágio.")

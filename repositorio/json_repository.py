from typing import Any, Optional, List

class Repository:
    """
    Classe abstrata/interface (padrão Repository) para definir
    o contrato de persistência (CRUD).
    """
    def criar(self, item: Any) -> None:
        """Salva um novo objeto."""
        pass

    def ler(self, id_chave: str) -> Optional[Any]:
        """Busca um objeto pelo identificador (placa/cpf)."""
        pass

    def atualizar(self, item: Any) -> None:
        """Atualiza um objeto existente."""
        pass

    def excluir(self, id_chave: str) -> None:
        """Remove um objeto do repositório."""
        pass

    def listar_todos(self) -> List[Any]:
        """Retorna todos os objetos no repositório."""
        pass

class JsonRepository(Repository):
    """
    Implementação do Repository que utiliza arquivos JSON para persistência.
    """
    def __init__(self, nome_arquivo: str):
        self._nome_arquivo = nome_arquivo
        pass
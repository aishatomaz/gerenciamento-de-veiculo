from .json_repository import Repository

class SqliteRepository(Repository):
    """
    Implementação do Repository que utiliza SQLite para persistência.
    Requisito opcional para persistência.
    """
    def __init__(self, db_path: str):
        self._db_path = db_path
        pass
    # Implementar método CRUD.
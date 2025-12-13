from typing import Any

class Pessoa:
    """Representa uma pessoa básica (base para Motorista)."""

    def __init__(self, nome: str, cpf: str) -> None:
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome
    
    # Setters Omitidos

    @property
    def cpf(self) -> str:
        return self.__cpf

    def __str__(self) -> str:
        return f"{self.__nome} ({self.__cpf})"

"""veiculo/dominio/motorista.py - Classe Motorista"""

class Motorista:
    """
    Representa um motorista do sistema.
    """

    def __init__(self, nome: str, cpf: str, categoria_cnh: str, experiencia: int = 0, disponibilidade: bool = True):
        self.__nome = nome
        self.__cpf = cpf
        self.__categoria_cnh = categoria_cnh
        self.__experiencia = int(experiencia)
        self.__disponibilidade = bool(disponibilidade)
        self.__historico_viagens = []

    @property
    def nome(self): return self.__nome

    @nome.setter
    def nome(self, v): self.__nome = v

    @property
    def cpf(self): return self.__cpf

    @cpf.setter
    def cpf(self, v): self.__cpf = v

    @property
    def categoria_cnh(self): return self.__categoria_cnh

    @categoria_cnh.setter
    def categoria_cnh(self, v): self.__categoria_cnh = v

    @property
    def experiencia(self): return self.__experiencia

    @experiencia.setter
    def experiencia(self, v): self.__experiencia = int(v)

    @property
    def disponibilidade(self): return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, v): self.__disponibilidade = bool(v)

    @property
    def historico_viagens(self):
        return list(self.__historico_viagens)

    def registrar_viagem(self, viagem):
        self.__historico_viagens.append(viagem)

    def pode_dirigir(self, tipo_veiculo: str) -> bool:
        tipo = tipo_veiculo.lower()
        cnh = self.categoria_cnh.upper()

        if tipo == "moto":
            return cnh == "A"
        if tipo == "carro":
            return cnh in ("B", "C", "D", "E")
        if tipo == "caminhao":
            return cnh in ("C", "D", "E")

        return False

    def __str__(self):
        return f"{self.nome} — CNH {self.categoria_cnh}"

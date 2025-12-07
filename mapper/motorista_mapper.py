from dominio.motorista import Motorista


class MotoristaMapper:

    @staticmethod
    def to_dict(motorista: Motorista) -> dict:
        return {
            "nome": motorista.nome,
            "cpf": motorista.cpf,
            "categoria_cnh": motorista.categoria_cnh,
            "experiencia": motorista.experiencia,
            "disponibilidade": motorista.disponibilidade,
        }

    @staticmethod
    def to_object(data: dict) -> Motorista:
        return Motorista(
            data["nome"],
            data["cpf"],
            data["categoria_cnh"],
            data["experiencia"],
            data["disponibilidade"],
        )
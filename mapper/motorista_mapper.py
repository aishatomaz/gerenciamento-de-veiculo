from dominio.motorista import Motorista
from typing import Dict, Any

class MotoristaMapper:

    @staticmethod
    def to_dict(motorista: Motorista) -> Dict[str, Any]:
        return {
            "nome": motorista.nome,
            "cpf": motorista.cpf,
            "categoria_cnh": motorista.categoria_cnh,
            "experiencia": motorista.experiencia,
            "disponibilidade": motorista.disponibilidade,
            "historico_viagens": motorista.historico_viagens
        }

    @staticmethod
    def to_object(data: Dict[str, Any]) -> Motorista:
        return Motorista(
            data["nome"],
            data["cpf"],
            data["categoria_cnh"],
            data["experiencia"],
            data["disponibilidade"],
            data.get("historico_viagens") # Passa o histórico para o desenvolvedor
        )

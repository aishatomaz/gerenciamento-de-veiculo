from dominio.veiculo import Veiculo
from dominio.estado import EstadoVeiculo


class VeiculoMapper:

    @staticmethod
    def to_dict(veiculo: Veiculo) -> dict:
        return {
            "placa": veiculo.placa,
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "ano": veiculo.ano,
            "quilometragem": veiculo.quilometragem,
            "status": veiculo.status.value,
        }

    @staticmethod
    def to_object(data: dict) -> Veiculo:
        v = Veiculo(
            data["placa"],
            data["marca"],
            data["modelo"],
            data["ano"],
            data["quilometragem"],
        )
        v.alterar_status(EstadoVeiculo(data["status"]))
        return v

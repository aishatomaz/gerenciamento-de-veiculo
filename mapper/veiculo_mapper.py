from dominio.veiculo import Veiculo
from dominio.carro import Carro
from dominio.moto import Moto
from dominio.caminhao import Caminhao
from dominio.estado import EstadoVeiculo
from typing import Dict, Any, Type

VEICULO_CLASSES: Dict[str, Type[Veiculo]] = {
    "Carro": Carro,
    "Moto": Moto,
    "Caminhao": Caminhao,
}

class VeiculoMapper:

    @staticmethod
    def to_dict(veiculo: Veiculo) -> Dict[str, Any]:
        data = {
            "placa": veiculo.placa,
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "tipo": veiculo.tipo,
            "ano": veiculo.ano,
            "quilometragem": veiculo.quilometragem,
            "consumo_medio": veiculo.consumo_medio,
            "status": veiculo.status.value,
        }
        # Incluir dados dos Mixins se existirem
        if hasattr(veiculo, 'historico_abastecimentos'):
            data["historico_abastecimentos"] = veiculo.historico_abastecimentos
        if hasattr(veiculo, 'historico_manutencoes'):
            data["historico_manutencoes"] = veiculo.historico_manutencoes
            
        return data

    @staticmethod
    def to_object(data: Dict[str, Any]) -> Veiculo:
        tipo = data["tipo"]
        cls = VEICULO_CLASSES.get(tipo, Veiculo)
        
        v: Veiculo = cls(
            data["placa"],
            data["marca"],
            data["modelo"],
            data["ano"],
            data.get("quilometragem", 0.0),
            data.get("consumo_medio", 0.0),
            EstadoVeiculo(data["status"]), # Passa status no construtor
        )
        
        # Injeção de Históricos (se a classe for um Mixin)
        if isinstance(v, (Carro, Moto, Caminhao)):
            if hasattr(v, '_AbastecivelMixin__historico_abastecimentos'):
                v._AbastecivelMixin__historico_abastecimentos = data.get("historico_abastecimentos", [])
            if hasattr(v, '_ManutenivelMixin__historico_manutencoes'):
                v._ManutenivelMixin__historico_manutencoes = data.get("historico_manutencoes", [])
        
        return v

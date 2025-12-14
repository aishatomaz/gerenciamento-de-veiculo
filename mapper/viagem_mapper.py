from dominio.viagem import Viagem
from dominio.motorista import Motorista
from dominio.veiculo import Veiculo
from typing import Dict, Any

class ViagemMapper:
    """Mapeia o objeto Viagem, usando apenas identificadores para Motorista/Veículo."""
    
    @staticmethod
    def to_dict(viagem: Viagem) -> Dict[str, Any]:
        return {
            "motorista_cpf": viagem.motorista.cpf,
            "veiculo_placa": viagem.veiculo.placa,
            "origem": viagem.origem,
            "destino": viagem.destino,
            "distancia": viagem.distancia,
            "data": viagem.data.isoformat()
        }
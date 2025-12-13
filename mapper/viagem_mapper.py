from dominio.viagem import Viagem
from dominio.motorista import Motorista
from dominio.veiculo import Veiculo
from typing import Dict, Any
from datetime import date

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

    @staticmethod
    def to_object(data: Dict[str, Any], repo) -> Viagem:
        """
        Recupera o objeto Viagem, buscando Motorista e Veículo no repositório.
        Requer o repositório para buscar as dependências.
        """
        from service.motorista_service import MotoristaCRUD
        from service.veiculo_service import VeiculoCRUD
        
        mc = MotoristaCRUD(repo)
        vc = VeiculoCRUD(repo)
        
        motorista = mc.buscar_por_cpf(data["motorista_cpf"])
        veiculo = vc.buscar_por_placa(data["veiculo_placa"])
        
        if not motorista or not veiculo:
            # Isso pode acontecer se o motorista/veículo for deletado
            raise ValueError("Motorista ou Veículo da viagem não encontrado no repositório.")
            
        return Viagem(
            motorista=motorista,
            veiculo=veiculo,
            origem=data["origem"],
            destino=data["destino"],
            distancia=data["distancia"],
            data=date.fromisoformat(data["data"])
        )

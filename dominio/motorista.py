from typing import List, Dict, Any
from .pessoa import Pessoa # Herança

class Motorista(Pessoa):
    """Representa um motorista da frota, herda atributos de Pessoa."""

    # Mapeamento de compatibilidade CNH x Tipo de Veículo
    COMPATIBILIDADE_CNH = {
        "A": ["Moto"],
        "B": ["Carro"],
        "C": ["Carro", "Caminhao"],
        "D": ["Carro", "Caminhao"],
        "E": ["Carro", "Caminhao"]
    }

    def __init__(
        self,
        nome: str,
        cpf: str,
        categoria_cnh: str,
        experiencia: int,
        disponibilidade: bool = True,
        historico_viagens: List[Dict[str, Any]] = None # Para reconstrução via Mapper
    ) -> None:
        super().__init__(nome, cpf)
        
        self.__categoria_cnh = categoria_cnh.upper()
        self.__experiencia = experiencia
        self.__disponibilidade = disponibilidade
        self.__historico_viagens: List[Dict[str, Any]] = historico_viagens if historico_viagens is not None else []

    @property
    def categoria_cnh(self) -> str:
        return self.__categoria_cnh

    @property
    def experiencia(self) -> int:
        return self.__experiencia

    @property
    def disponibilidade(self) -> bool:
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, v: bool) -> None:
        self.__disponibilidade = v

    @property
    def historico_viagens(self) -> List[Dict[str, Any]]:
        return list(self.__historico_viagens)
    
    def pode_dirigir(self, tipo_veiculo: str) -> bool:
        """Verifica se o motorista pode dirigir o tipo de veículo baseado na CNH."""
        tipo_veiculo_capitalizado = tipo_veiculo.capitalize()
        veiculos_permitidos = self.COMPATIBILIDADE_CNH.get(self.__categoria_cnh, [])
        return tipo_veiculo_capitalizado in veiculos_permitidos
        
    def registrar_viagem(self, viagem) -> None:
        """Registra a viagem no histórico do motorista."""
        self.__historico_viagens.append({
            "origem": viagem.origem,
            "destino": viagem.destino,
            "distancia": viagem.distancia,
            "veiculo_placa": viagem.veiculo.placa,
            "data": viagem.data.isoformat()
        })

    def __str__(self) -> str:
        return f"{self.nome} ({self.cpf}) - CNH: {self.categoria_cnh}"

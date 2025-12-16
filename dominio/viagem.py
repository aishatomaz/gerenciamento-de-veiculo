from datetime import date
from typing import Optional
from .motorista import Motorista
from .veiculo import Veiculo
from .estado import EstadoVeiculo


class Viagem:
    """Representa uma viagem realizada (RT: Relacionamento, Regras de Negócio)."""

    def __init__(
        self,
        motorista: Motorista,
        veiculo: Veiculo,
        origem: str,
        destino: str,
        distancia: float,
        data: Optional[date] = None,
    ) -> None:
        self.__motorista = motorista
        self.__veiculo = veiculo
        self.__origem = origem
        self.__destino = destino
        self.__distancia = float(distancia)
        self.__data = data or date.today()

    # ==========================
    # Propriedades (Getters)
    # ==========================

    @property
    def motorista(self) -> Motorista:
        return self.__motorista

    @property
    def veiculo(self) -> Veiculo:
        return self.__veiculo

    @property
    def origem(self) -> str:
        return self.__origem

    @property
    def destino(self) -> str:
        return self.__destino

    @property
    def distancia(self) -> float:
        return self.__distancia

    @property
    def data(self) -> date:
        return self.__data

    # ==========================
    # Regras de Negócio
    # ==========================

    def executar(self, config: dict) -> None:
        """
        Executa a viagem e aplica as regras de negócio:
        - CNH compatível
        - Veículo ativo
        - Atualização de quilometragem
        - Verificação de revisão
        - Registro no histórico
        """
        compatibilidade = config["compatibilidade_cnh"]
        politicas = config["politicas"]

        # 1. Regra CNH compatível
        tipo_veiculo = self.veiculo.tipo
        categoria_motorista = self.motorista.categoria_cnh

        if (
            tipo_veiculo not in compatibilidade
            or categoria_motorista not in compatibilidade[tipo_veiculo]
        ):
            raise ValueError(
                f"CNH incompatível: Motorista {categoria_motorista} "
                f"não pode dirigir {tipo_veiculo}."
            )

        # 2. Regra: veículo deve estar ativo
        if self.veiculo.status != EstadoVeiculo.ATIVO:
            raise ValueError(
                f"Veículo {self.veiculo.placa} indisponível. "
                f"Status: {self.veiculo.status.value}"
            )

        # 3. Atualizar quilometragem
        self.veiculo.atualizar_quilometragem(self.distancia)

        # 4. Checar revisão obrigatória
        limite_km = politicas.get("limite_revisao_km", 10000)

        if (
            self.veiculo.quilometragem >= limite_km
            and self.veiculo.status == EstadoVeiculo.ATIVO
        ):
            self.veiculo.alterar_status(EstadoVeiculo.MANUTENCAO)
            self.veiculo.registrar_evento(
                f"ENTROU EM MANUTENÇÃO: Limite de KM ({limite_km}km) atingido."
            )

        # 5. Registrar histórico
        self.veiculo.registrar_viagem(self)
        self.motorista.registrar_viagem(self)

    # ==========================
    # Representação textual
    # ==========================

    def __str__(self) -> str:
        return (
            f"Origem: {self.origem} | "
            f"Destino: {self.destino} | "
            f"Distância: {self.distancia} km | "
            f"Data: {self.data.strftime('%d/%m/%Y')} | "
            f"Veículo: {self.veiculo.placa} | "
            f"Motorista: {self.motorista.nome}"
        )

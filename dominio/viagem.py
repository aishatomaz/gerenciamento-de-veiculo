from datetime import date
from typing import Optional
from .motorista import Motorista
from .veiculo import Veiculo
from mapper.viagm_mapper import ViagemMapper
from dominio.estado import EstadoVeiculo



class Viagem:
    """Representa uma viagem realizada por um motorista com um veículo."""

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
        motorista.registrar_viagem(self)
        veiculo.registrar_viagem(self)

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
    def data(self):
        return self.__data

    def executar(self, config):
        """
        Regras de negócio da Entrega 4
        """
        compatibilidade = config["compatibilidade_cnh"]
        politicas = config["politicas"]

        # ============================
        # Regra 1 — CNH compatível
        # ============================
        tipo_veiculo = self.veiculo.tipo
        categoria_motorista = self.motorista.categoria_cnh

        if categoria_motorista not in compatibilidade[tipo_veiculo]:
            raise ValueError(f"CNH incompatível: motorista {categoria_motorista} "
                             f"não pode dirigir {tipo_veiculo}")

        # ============================
        # Regra 2 — Veículo deve estar ativo
        # ============================
        if self.veiculo.status != EstadoVeiculo.ATIVO:
            raise ValueError("Veículo não está ativo para realizar a viagem.")

        # ============================
        # Regra 3 — Atualizar quilometragem
        # ============================
        self.veiculo.atualizar_quilometragem(self.distancia)

        # ============================
        # Regra 4 — Registrar no histórico do motorista
        # ============================
        self.motorista.registrar_viagem(self)

        # ============================
        # Regra 5 — Checar revisão obrigatória
        # ============================
        limite_km = politicas["limite_revisao_km"]

        if self.veiculo.quilometragem >= limite_km:
            self.veiculo.alterar_status(EstadoVeiculo.MANUTENCAO)

    def __str__(self):
        return f"{self.origem} → {self.destino} ({self.distancia} km)"


class ViagemCRUD:

    def __init__(self, repo):
        self.repo = repo

    def salvar(self, viagem):
        banco = self.repo.carregar()
        viagem_dict = ViagemMapper.to_dict(viagem)

        banco["viagens"].append(viagem_dict)
        self.repo.salvar(banco)

    def listar(self):
        banco = self.repo.carregar()
        return [
            ViagemMapper.to_object(dados, self.repo)
            for dados in banco["viagens"]
        ]

    def buscar(self, motorista_cpf: str, placa_veiculo: str):
        banco = self.repo.carregar()
        for v in banco["viagens"]:
            if v["motorista"] == motorista_cpf and v["veiculo"] == placa_veiculo:
                return ViagemMapper.to_object(v, self.repo)
        return None

    def remover(self, motorista_cpf: str, placa_veiculo: str):
        banco = self.repo.carregar()

        banco["viagens"] = [
            v for v in banco["viagens"]
            if not (v["motorista"] == motorista_cpf and v["veiculo"] == placa_veiculo)
        ]

        self.repo.salvar(banco)

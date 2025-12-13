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

    @property
    def motorista(self) -> Motorista:
        return self.__motorista

    @property
    def veiculo(self) -> Veiculo:
        return self.__veiculo

    @property
    def distancia(self) -> float:
        return self.__distancia
    
    @property
    def data(self):
        return self.__data
    
    def executar(self, config):
        """
        Executa a viagem e aplica as regras de negócio: CNH, status, atualização KM, revisão.
        """
        compatibilidade = config["compatibilidade_cnh"]
        politicas = config["politicas"]

        # 1. Regra CNH compatível (RT: Validação)
        tipo_veiculo = self.veiculo.tipo
        categoria_motorista = self.motorista.categoria_cnh

        if tipo_veiculo not in compatibilidade or categoria_motorista not in compatibilidade[tipo_veiculo]:
            raise ValueError(f"CNH incompatível: Motorista {categoria_motorista} não pode dirigir {tipo_veiculo}.")

        # 2. Regra Veículo deve estar ativo (RT: Bloqueio de alocação)
        if self.veiculo.status != EstadoVeiculo.ATIVO:
            raise ValueError(f"Veículo {self.veiculo.placa} indisponível. Status: {self.veiculo.status.value}")

        # 3. Atualizar quilometragem
        self.veiculo.atualizar_quilometragem(self.distancia)

        # 4. Checar revisão obrigatória (RT: Regra Configurável)
        limite_km = politicas.get("limite_revisao_km", 10000)

        if self.veiculo.quilometragem >= limite_km and self.veiculo.status == EstadoVeiculo.ATIVO:
            self.veiculo.alterar_status(EstadoVeiculo.MANUTENCAO)
            self.veiculo.registrar_evento(f"ENTROU EM MANUTENÇÃO: Limite de KM ({limite_km}km) atingido.")

        # 5. Registrar no histórico após sucesso
        self.veiculo.registrar_viagem(self)
        self.motorista.registrar_viagem(self)
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

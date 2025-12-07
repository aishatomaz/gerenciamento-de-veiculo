from datetime import date
from typing import Optional
from .motorista import Motorista
from .veiculo import Veiculo
from mapper.viagm_mapper import ViagemMapper



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

    def executar(self) -> None:
        """Executa a viagem: atualiza registros básicos (sem persistência)."""
        # atualiza quilometragem do veículo
        nova_km = self.veiculo.quilometragem + self.distancia
        self.veiculo.quilometragem = nova_km
        # registra no motorista
        try:
            self.motorista.registrar_viagem(self)
        except Exception:
            # registrar_viagem pode não existir se Motorista não for do tipo esperado -> arrumar posteriormente
            pass

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

from typing import List, Iterator, Any
from .estado import EstadoVeiculo
from mapper.veiculo_mapper import VeiculoMapper


class Veiculo:
    """
    Classe base para veículos da frota.

    Attributes:
        __placa (str)
        __marca (str)
        __modelo (str)
        __tipo (str)
        __ano (int)
        __quilometragem (float)
        __consumo_medio (float)
        __status (EstadoVeiculo)
        __historico_eventos (List[str])
    """

    def __init__(
        self,
        placa: str,
        marca: str,
        modelo: str,
        tipo: str,
        ano: int,
        quilometragem: float = 0.0,
        consumo_medio: float = 0.0,
        status: EstadoVeiculo = EstadoVeiculo.ATIVO,
    ) -> None:
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__tipo = tipo
        self.__ano = ano
        self.__quilometragem = float(max(0.0, quilometragem))
        self.__consumo_medio = float(max(0.0, consumo_medio))
        self.__status = EstadoVeiculo.ATIVO # define estado padrão do veículo como ATIVO
        self.__historico_eventos: List[str] = []
        self.__historico_viagens = []

    # --------------------
    # properties (getters/setters)
    # --------------------
    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, v: str) -> None:
        self.__placa = v

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self, v: str) -> None:
        self.__marca = v

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, v: str) -> None:
        self.__modelo = v

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, v: str) -> None:
        self.__tipo = v

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, v: int) -> None:
        self.__ano = int(v)

    @property
    def quilometragem(self) -> float:
        return self.__quilometragem

    @quilometragem.setter
    def quilometragem(self, v: float) -> None:
        if v < 0:
            raise ValueError("Quilometragem não pode ser negativa.")
        self.__quilometragem = float(v)

    @property
    def consumo_medio(self) -> float:
        return self.__consumo_medio

    @consumo_medio.setter
    def consumo_medio(self, v: float) -> None:
        if v < 0:
            raise ValueError("Consumo médio não pode ser negativo.")
        self.__consumo_medio = float(v)

    @property
    def status(self) -> EstadoVeiculo:
        return self.__status

    @status.setter
    def status(self, v: EstadoVeiculo) -> None:
        if not isinstance(v, EstadoVeiculo):
            raise ValueError("status deve ser um EstadoVeiculo.")
        self.__status = v

    @property
    def historico_eventos(self) -> List[str]:
        # retorna cópia para evitar alteração externa direta
        return list(self.__historico_eventos)

    @property
    def historico_viagens(self):
        return list(self.__historico_viagens)
    
    
    # --------------------
    # métodos principais
    # --------------------
    def atualizar_quilometragem(self, km: float) -> None:
        """Incrementa/define quilometragem (validação básica)."""
        if km < 0:
            raise ValueError("km deve ser não-negativo.")
        self.__quilometragem = float(km)
        self.__historico_eventos.append(f"Quilometragem atualizada para {km}")

    def registrar_evento(self, evento: str) -> None:
        """Adiciona um evento ao histórico do veículo."""
        self.__historico_eventos.append(str(evento))

    def alterar_status(self, novo_status: EstadoVeiculo) -> None:
        """Altera o status do veículo (validação feita pelo tipo)."""
        self.status = novo_status
        self.__historico_eventos.append(f"Status alterado para {novo_status.name}")

    def registrar_viagem(self, viagem):
        self.__historico_viagens.append(viagem)

    # Métodos especiais
    def __str__(self) -> str:
        return f"{self.__placa} — {self.__marca} {self.__modelo} ({self.__ano})"

    def __repr__(self) -> str:
        return f"Veiculo(placa={self.__placa!r})"

    def __eq__(self, outro: Any) -> bool:
        if not isinstance(outro, Veiculo):
            return NotImplemented
        return self.placa == outro.placa

    def __lt__(self, outro: "Veiculo") -> bool:
        return self.quilometragem < outro.quilometragem

    def __iter__(self) -> Iterator[str]:
        """Itera sobre o histórico de eventos (manutenções/abastecimentos)."""
        return iter(self.__historico_eventos)

class VeiculoCRUD:

    def __init__(self, repo):
        self.repo = repo

    def salvar(self, veiculo):
        banco = self.repo.carregar()
        veiculo_dict = VeiculoMapper.to_dict(veiculo)
        banco["veiculos"].append(veiculo_dict)
        self.repo.salvar(banco)

    def listar(self):
        banco = self.repo.carregar()
        return [
            VeiculoMapper.to_object(dados)
            for dados in banco["veiculos"]
        ]

    def buscar_por_placa(self, placa: str):
        banco = self.repo.carregar()
        for v in banco["veiculos"]:
            if v["placa"] == placa:
                return VeiculoMapper.to_object(v)
        return None

    def atualizar(self, placa: str, novo_objeto):
        banco = self.repo.carregar()
        for i, v in enumerate(banco["veiculos"]):
            if v["placa"] == placa:
                banco["veiculos"][i] = VeiculoMapper.to_dict(novo_objeto)
                self.repo.salvar(banco)
                return True
        return False

    def remover(self, placa: str):
        banco = self.repo.carregar()
        banco["veiculos"] = [
            v for v in banco["veiculos"] if v["placa"] != placa
        ]
        self.repo.salvar(banco)

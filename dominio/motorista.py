from typing import List, Dict, Any
from .pessoa import Pessoa # Herança

class Motorista(Pessoa):
    """Representa um motorista da frota, herda atributos de Pessoa."""

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
from typing import List, Dict, Any
from .pessoa import Pessoa # Herança

class Motorista(Pessoa):
    """Representa um motorista da frota, herda atributos de Pessoa."""

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

    def registrar_viagem(self, viagem):
        self.historico_viagens.append({
            "origem": viagem.origem,
            "destino": viagem.destino,
            "distancia": viagem.distancia
        })

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

    def alterar_status(self, novo_status: EstadoVeiculo) -> None:
        """Altera o status do veículo (validação feita pelo tipo)."""
        self.status = novo_status
        self.__historico_eventos.append(f"Status alterado para {novo_status.name}")

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

class MotoristaCRUD:

    def __init__(self, repo):
        self.repo = repo

    def salvar(self, motorista):
        banco = self.repo.carregar()
        motorista_dict = MotoristaMapper.to_dict(motorista)

        banco["motoristas"].append(motorista_dict)
        self.repo.salvar(banco)

    def listar(self):
        banco = self.repo.carregar()
        return [
            MotoristaMapper.to_object(dados)
            for dados in banco["motoristas"]
        ]

    def buscar_por_cpf(self, cpf: str):
        banco = self.repo.carregar()
        for m in banco["motoristas"]:
            if m["cpf"] == cpf:
                return MotoristaMapper.to_object(m)
        return None

    def atualizar(self, cpf: str, novo_motorista):
        banco = self.repo.carregar()

        for i, m in enumerate(banco["motoristas"]):
            if m["cpf"] == cpf:
                banco["motoristas"][i] = MotoristaMapper.to_dict(novo_motorista)
                self.repo.salvar(banco)
                return True

        return False

    def remover(self, cpf: str):
        banco = self.repo.carregar()

        banco["motoristas"] = [
            m for m in banco["motoristas"] if m["cpf"] != cpf
        ]

        self.repo.salvar(banco)

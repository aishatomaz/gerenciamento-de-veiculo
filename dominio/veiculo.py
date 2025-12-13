from typing import List, Iterator, Any
from datetime import date
from .estado import EstadoVeiculo
# Importa mixins para que as subclasses possam herdar
from .mixins import ManutenivelMixin, AbastecivelMixin

class Veiculo:
    """Classe base para veículos da frota."""

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
        self.__status = status
        self.__historico_eventos: List[str] = []
        self.__historico_viagens = []

    # --- Properties (Encapsulamento RT) ---
    @property
    def placa(self) -> str:
        return self.__placa

    @property
    def quilometragem(self) -> float:
        return self.__quilometragem

    @property
    def status(self) -> EstadoVeiculo:
        return self.__status
        
    @property
    def tipo(self) -> str:
        return self.__tipo
        
    @property
    def marca(self) -> str:
        return self.__marca
        
    @property
    def modelo(self) -> str:
        return self.__modelo
    
    @property
    def ano(self) -> int:
        return self.__ano

    @property
    def consumo_medio(self) -> float:
        return self.__consumo_medio
        
    @property
    def historico_eventos(self) -> List[str]:
        return list(self.__historico_eventos)

    @property
    def historico_viagens(self):
        return list(self.__historico_viagens)

    # --- Métodos de Ação ---
    def atualizar_quilometragem(self, km_percorrido: float) -> None:
        """Incrementa a quilometragem total do veículo."""
        if km_percorrido < 0:
            raise ValueError("km percorrido deve ser não-negativo.")
        self.__quilometragem += km_percorrido
        self.registrar_evento(f"KM incrementada em {km_percorrido:.2f}km. Total: {self.__quilometragem:.2f}km")

    def registrar_evento(self, evento: str) -> None:
        """Adiciona um evento ao histórico do veículo."""
        self.__historico_eventos.append(f"{date.today().isoformat()}: {evento}")

    def alterar_status(self, novo_status: EstadoVeiculo) -> None:
        """Altera o status do veículo."""
        if not isinstance(novo_status, EstadoVeiculo):
            raise ValueError("status deve ser um EstadoVeiculo.")
        self.__status = novo_status
        self.registrar_evento(f"Status alterado para {novo_status.value}")

    def registrar_viagem(self, viagem):
        """Registra a viagem, recebe o objeto Viagem."""
        self.__historico_viagens.append(viagem)

    # --- Métodos Especiais (RT) ---
    def __str__(self) -> str:
        return f"[{self.__placa}] {self.__marca} {self.__modelo} ({self.__ano}) - Status: {self.status.value}"

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

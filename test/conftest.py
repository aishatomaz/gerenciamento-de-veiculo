import pytest
from dominio.veiculo import Veiculo
from dominio.motorista import Motorista
from dominio.viagem import Viagem
from dominio.estado import EstadoVeiculo

# Veículo padrão para os testes
@pytest.fixture
def veiculo_base():
    return Veiculo(
        placa="ABC1234",
        marca="Honda",
        modelo="Fit",
        tipo="Carro",
        ano=2020,
        quilometragem=10000
    )

# Motorista padrão para os testes
@pytest.fixture
def motorista_base():
    return Motorista(
        nome="Shirou",
        cpf="11122233344",
        categoria_cnh="B",
        experiencia=3,
        disponibilidade=True
    )

# Viagem padrão
@pytest.fixture
def viagem_base(veiculo_base, motorista_base):
    return Viagem(
        motorista=motorista_base,
        veiculo=veiculo_base,
        origem="Juazeiro do Norte",
        destino="Crato",
        distancia=15.0
    )

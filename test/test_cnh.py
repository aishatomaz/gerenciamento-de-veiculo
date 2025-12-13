from dominio.motorista import Motorista
from dominio.veiculo import Veiculo
from dominio.viagem import Viagem

def test_cnh_incompativel():
    m = Motorista("Aisha", "123", "B", 2, True)
    v = Veiculo(placa="AAA0000", marca="Yamaha", modelo="XTZ", tipo="Moto", ano=2020, quilometragem=0)

    viagem = Viagem(m, v, "A", "B", 10)

    config = {
        "compatibilidade_cnh": {"Moto": ["A"]},
        "politicas": {"limite_revisao_km": 10000}
    }

    try:
        viagem.executar(config)
        assert False
    except ValueError:
        assert True

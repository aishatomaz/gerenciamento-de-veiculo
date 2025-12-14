from dominio.veiculo import Veiculo

def test_criacao_veiculo(veiculo_base):
    assert veiculo_base.placa == "ABC1234"
    assert veiculo_base.quilometragem == 10000


def test_setters_veiculo(veiculo_base):
    veiculo_base.marca = "Toyota"
    veiculo_base.modelo = "Corolla"
    veiculo_base.quilometragem = 25000

    assert veiculo_base.marca == "Toyota"
    assert veiculo_base.modelo == "Corolla"
    assert veiculo_base.quilometragem == 25000


def test_veiculo_enum_estado_default():
    from dominio.estado import EstadoVeiculo
    v = Veiculo("AAA0000", "Ford", "Ka", 2019, 5000)
    # O estado do veículo é definido depois -> adicionar alterações futuramente
    assert hasattr(v, "_Veiculo__quilometragem")  # encapsulado

def test_motorista_criacao(motorista_base):
    assert motorista_base.nome == "Shirou"
    assert motorista_base.categoria_cnh == "B"
    assert motorista_base.disponibilidade is True


def test_motorista_pode_dirigir_carro(motorista_base):
    assert motorista_base.pode_dirigir("carro") is True


def test_motorista_nao_pode_dirigir_moto(motorista_base):
    assert motorista_base.pode_dirigir("moto") is False


def test_registro_viagem(motorista_base, viagem_base):
    motorista_base.registrar_viagem(viagem_base)
    assert len(motorista_base.historico_viagens) == 1

def test_criacao_viagem(viagem_base):
    assert viagem_base.origem == "Juazeiro do Norte"
    assert viagem_base.destino == "Crato"
    assert viagem_base.distancia == 15.0


def test_associacao_motorista_e_veiculo(viagem_base, motorista_base, veiculo_base):
    assert viagem_base.motorista is motorista_base
    assert viagem_base.veiculo is veiculo_base

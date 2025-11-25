from dominio.mixins import AbastecivelMixin, ManutenivelMixin

def test_abastecimento():
    a = AbastecivelMixin()
    a.abastecer(litros=20, valor=120.0)
    assert len(a._historico_abastecimento) == 1


def test_manutencao():
    m = ManutenivelMixin()
    m.registrar_manutencao(descricao="Troca de óleo", custo=80.0)
    assert len(m._historico_manutencao) == 1

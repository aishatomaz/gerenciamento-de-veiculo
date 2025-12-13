from dominio.mixins import AbastecivelMixin, ManutenivelMixin
from datetime import date

def test_abastecimento():
    """Testa o mixin de abastecimento."""
    
    # Cria uma classe de teste que usa o mixin
    class VeiculoTeste(AbastecivelMixin):
        def __init__(self):
            super().__init__()
            
        def registrar_evento(self, evento: str):
            pass  # Método necessário para o mixin funcionar
    
    v = VeiculoTeste()
    v.registrar_abastecimento(date.today(), "Gasolina", 20.0, 120.0)
    assert len(v.historico_abastecimentos) == 1


def test_manutencao():
    """Testa o mixin de manutenção."""
    from dominio.estado import EstadoVeiculo
    
    # Cria uma classe de teste que usa o mixin
    class VeiculoTeste(ManutenivelMixin):
        def __init__(self):
            super().__init__()
            self.status = EstadoVeiculo.ATIVO
            
        def registrar_evento(self, evento: str):
            pass  # Método necessário para o mixin funcionar
            
        def alterar_status(self, novo_status):
            self.status = novo_status
    
    v = VeiculoTeste()
    v.registrar_manutencao(date.today(), "Preventiva", 80.0, "Troca de óleo")
    assert len(v.historico_manutencoes) == 1

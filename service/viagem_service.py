from mapper.viagem_mapper import ViagemMapper

class ViagemCRUD:
    """Serviço CRUD para gerenciar viagens no repositório."""

    def __init__(self, repo):
        self.repo = repo

    def salvar(self, viagem):
        """Salva uma nova viagem no repositório."""
        banco = self.repo.carregar()
        viagem_dict = ViagemMapper.to_dict(viagem)
        banco["viagens"].append(viagem_dict)
        self.repo.salvar(banco)

    def listar(self):
        """Lista todas as viagens do repositório."""
        banco = self.repo.carregar()
        return [
            ViagemMapper.to_object(dados, self.repo)
            for dados in banco["viagens"]
        ]

    def buscar(self, motorista_cpf: str, placa_veiculo: str):
        """Busca uma viagem específica."""
        banco = self.repo.carregar()
        for v in banco["viagens"]:
            if v["motorista_cpf"] == motorista_cpf and v["veiculo_placa"] == placa_veiculo:
                return ViagemMapper.to_object(v, self.repo)
        return None

    def remover(self, motorista_cpf: str, placa_veiculo: str):
        """Remove uma viagem do repositório."""
        banco = self.repo.carregar()
        banco["viagens"] = [
            v for v in banco["viagens"]
            if not (v["motorista_cpf"] == motorista_cpf and v["veiculo_placa"] == placa_veiculo)
        ]
        self.repo.salvar(banco)

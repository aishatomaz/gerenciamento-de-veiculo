from mapper.veiculo_mapper import VeiculoMapper

class VeiculoCRUD:
    """Serviço CRUD para gerenciar veículos no repositório."""

    def __init__(self, repo):
        self.repo = repo

    def salvar(self, veiculo):
        """Salva um novo veículo no repositório."""
        banco = self.repo.carregar()
        veiculo_dict = VeiculoMapper.to_dict(veiculo)
        banco["veiculos"].append(veiculo_dict)
        self.repo.salvar(banco)

    def listar(self):
        """Lista todos os veículos do repositório."""
        banco = self.repo.carregar()
        return [
            VeiculoMapper.to_object(dados)
            for dados in banco["veiculos"]
        ]

    def buscar_por_placa(self, placa: str):
        """Busca um veículo pela placa."""
        banco = self.repo.carregar()
        for v in banco["veiculos"]:
            if v["placa"] == placa:
                return VeiculoMapper.to_object(v)
        return None

    def atualizar(self, placa: str, novo_objeto):
        """Atualiza um veículo existente."""
        banco = self.repo.carregar()
        for i, v in enumerate(banco["veiculos"]):
            if v["placa"] == placa:
                banco["veiculos"][i] = VeiculoMapper.to_dict(novo_objeto)
                self.repo.salvar(banco)
                return True
        return False

    def remover(self, placa: str):
        """Remove um veículo do repositório."""
        banco = self.repo.carregar()
        banco["veiculos"] = [
            v for v in banco["veiculos"] if v["placa"] != placa
        ]
        self.repo.salvar(banco)
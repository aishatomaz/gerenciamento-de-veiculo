from mapper.motorista_mapper import MotoristaMapper

class MotoristaCRUD:
    """Serviço CRUD para gerenciar motoristas no repositório."""

    def __init__(self, repo):
        self.repo = repo

    def salvar(self, motorista):
        """Salva um novo motorista no repositório."""
        banco = self.repo.carregar()
        motorista_dict = MotoristaMapper.to_dict(motorista)
        banco["motoristas"].append(motorista_dict)
        self.repo.salvar(banco)

    def listar(self):
        """Lista todos os motoristas do repositório."""
        banco = self.repo.carregar()
        return [
            MotoristaMapper.to_object(dados)
            for dados in banco["motoristas"]
        ]

    def buscar_por_cpf(self, cpf: str):
        """Busca um motorista pelo CPF."""
        banco = self.repo.carregar()
        for m in banco["motoristas"]:
            if m["cpf"] == cpf:
                return MotoristaMapper.to_object(m)
        return None

    def atualizar(self, cpf: str, novo_motorista):
        """Atualiza um motorista existente."""
        banco = self.repo.carregar()
        for i, m in enumerate(banco["motoristas"]):
            if m["cpf"] == cpf:
                banco["motoristas"][i] = MotoristaMapper.to_dict(novo_motorista)
                self.repo.salvar(banco)
                return True
        return False

    def remover(self, cpf: str):
        """Remove um motorista do repositório."""
        banco = self.repo.carregar()
        banco["motoristas"] = [
            m for m in banco["motoristas"] if m["cpf"] != cpf
        ]
        self.repo.salvar(banco)
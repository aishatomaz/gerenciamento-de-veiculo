from dominio.viagem import Viagem
from dominio.motorista import MotoristaCRUD
from dominio.veiculo import VeiculoCRUD


class ViagemMapper:

    @staticmethod
    def to_dict(viagem: Viagem) -> dict:
        return {
            "motorista": viagem.motorista.cpf,
            "veiculo": viagem.veiculo.placa,
            "origem": viagem.origem,
            "destino": viagem.destino,
            "distancia": viagem.distancia
        }

    @staticmethod
    def to_object(data: dict, repo) -> Viagem:
        """
        repo = JsonRepository
        Necessário para reconstruir Motorista e Veículo.
        """

        mcrud = MotoristaCRUD(repo)
        vcrud = VeiculoCRUD(repo)

        motorista = mcrud.buscar_por_cpf(data["motorista"])
        veiculo = vcrud.buscar_por_placa(data["veiculo"])

        viagem = Viagem(
            motorista,
            veiculo,
            data["origem"],
            data["destino"],
            data["distancia"]
        )

        return viagem

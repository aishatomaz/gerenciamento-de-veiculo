from veiculo.dominio.veiculo import Veiculo
from veiculo.dominio.motorista import Motorista
from veiculo.dominio.viagem import Viagem
from veiculo.dominio.estado import EstadoVeiculo
from veiculo.dominio.relatorios import (
    relatorio_viagens_por_motorista,
    relatorio_veiculos_por_status,
    relatorio_resumo_sistema,
)

from veiculo.repositorio.json_repository import JsonRepository


def main():
    # Inicializa o repositório JSON
    repo = JsonRepository()

    # Carrega os dados existentes no JSON (veículos, motoristas, viagens)
    banco = repo.carregar()

    # --------------------------------------
    # 1) Criar objetos do domínio (exemplo)
    # --------------------------------------
    v1 = Veiculo("ABC1234", "Honda", "Fit", 2020, 10000)
    v2 = Veiculo("XYZ9876", "Toyota", "Corolla", 2021, 15000)

    motorista1 = Motorista("Shirou", "11122233344", "B", 2, True)

    # Registrar duas viagens (RELACIONAMENTO funcionando)
    Viagem(motorista1, v1, "Juazeiro do Norte", "Crato", 15)
    Viagem(motorista1, v2, "Crato", "Barbalha", 10)

    # --------------------------------------
    # 2) Atualizar o banco JSON (convertendo objetos para dicionários)
    # --------------------------------------

    # Veículos no banco
    banco["veiculos"] = [
        {
            "placa": v1.placa,
            "marca": v1.marca,
            "modelo": v1.modelo,
            "ano": v1.ano,
            "quilometragem": v1.quilometragem,
            "status": v1.status.value,
        },
        {
            "placa": v2.placa,
            "marca": v2.marca,
            "modelo": v2.modelo,
            "ano": v2.ano,
            "quilometragem": v2.quilometragem,
            "status": v2.status.value,
        },
    ]

    # Motoristas no banco
    banco["motoristas"] = [
        {
            "nome": motorista1.nome,
            "cpf": motorista1.cpf,
            "categoria_cnh": motorista1.categoria_cnh,
            "experiencia": motorista1.experiencia,
            "disponibilidade": motorista1.disponibilidade,
        }
    ]

    # Viagens no banco
    banco["viagens"] = [
        {
            "motorista": motorista1.nome,
            "veiculo": v1.placa,
            "origem": "Juazeiro do Norte",
            "destino": "Crato",
            "distancia": 15,
        },
        {
            "motorista": motorista1.nome,
            "veiculo": v2.placa,
            "origem": "Crato",
            "destino": "Barbalha",
            "distancia": 10,
        },
    ]

    # Salvar tudo no JSON
    repo.salvar(banco)

    # --------------------------------------
    # 3) RELATÓRIOS SIMPLES (Entrega 2)
    # --------------------------------------

    print("\n=== RELATÓRIO 1: Viagens por Motorista ===")
    relatorio_viagens_por_motorista(motorista1)

    print("\n=== RELATÓRIO 2: Veículos Ativos ===")
    relatorio_veiculos_por_status([v1, v2], EstadoVeiculo.ATIVO)

    print("\n=== RELATÓRIO 3: Resumo Geral ===")
    relatorio_resumo_sistema(banco)

# 
v = Veiculo("ABC1234", "Honda", "Fit", 2020, 10000)
crud.salvar(v)

lista = crud.listar()
for veiculo in lista:
    print(veiculo.placa, veiculo.modelo)

encontrado = crud.buscar_por_placa("ABC1234")
print("Veículo encontrado:", encontrado)



if __name__ == "__main__":
    main()

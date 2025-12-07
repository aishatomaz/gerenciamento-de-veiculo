from dominio.estado import EstadoVeiculo


def relatorio_viagens_por_motorista(motorista):
    """
    Relatório simples que mostra todas as viagens realizadas por um motorista.
    """
    print(f"\nRelatório de Viagens – Motorista: {motorista.nome}")
    print("-" * 60)

    if not motorista.historico_viagens:
        print("Nenhuma viagem registrada para este motorista.")
        return

    for viagem in motorista.historico_viagens:
        print(f"Origem: {viagem.origem}")
        print(f"Destino: {viagem.destino}")
        print(f"Distância: {viagem.distancia} km")
        print("-" * 60)


def relatorio_veiculos_por_status(veiculos, status: EstadoVeiculo):
    """
    Relatório simples que lista veículos filtrados por status.
    """
    print(f"\nRelatório – Veículos com status: {status.value}")
    print("-" * 60)

    encontrados = [v for v in veiculos if v.status == status]

    if not encontrados:
        print("Nenhum veículo encontrado com esse status.")
        return

    for v in encontrados:
        print(f"Placa: {v.placa} | Modelo: {v.modelo} | Km: {v.quilometragem}")
    print("-" * 60)


def relatorio_resumo_sistema(banco_json: dict):
    """
    Relatório simples que mostra um panorama geral do sistema:
    total de veículos, motoristas e viagens.
    """
    print("\nResumo Geral do Sistema de Frota")
    print("-" * 60)

    total_veiculos = len(banco_json.get("veiculos", []))
    total_motoristas = len(banco_json.get("motoristas", []))
    total_viagens = len(banco_json.get("viagens", []))

    print(f"Total de veículos cadastrados : {total_veiculos}")
    print(f"Total de motoristas cadastrados: {total_motoristas}")
    print(f"Total de viagens registradas   : {total_viagens}")
    print("-" * 60)

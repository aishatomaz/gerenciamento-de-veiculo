from dominio.estado import EstadoVeiculo

# ============================
# RELATÓRIOS SIMPLES
# ============================

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
        print(f"Origem: {viagem['origem']}")
        print(f"Destino: {viagem['destino']}")
        print(f"Destino: {viagem['distancia']} km")
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

from typing import List, Dict
from dominio.estado import EstadoVeiculo


# ============================
# RELATÓRIO DE ABASTECIMENTOS
# ============================

def relatorio_abastecimentos(veiculos: List) -> None:
    print("\n=== RELATÓRIO DE ABASTECIMENTOS ===")

    encontrou = False
    for v in veiculos:
        if hasattr(v, "historico_abastecimentos") and v.historico_abastecimentos:
            encontrou = True
            print(f"\nVeículo {v.placa} ({v.modelo})")
            for a in v.historico_abastecimentos:
                print(
                    f"  Data: {a['data']} | "
                    f"Combustível: {a['tipo_combustivel']} | "
                    f"Litros: {a['litros']} | "
                    f"Valor: R$ {a['valor']:.2f}"
                )

    if not encontrou:
        print("Nenhum abastecimento registrado.")


# ============================
# RELATÓRIO DE MANUTENÇÕES
# ============================

def relatorio_manutencoes(veiculos: List) -> None:
    print("\n=== RELATÓRIO DE MANUTENÇÕES ===")

    encontrou = False
    for v in veiculos:
        if hasattr(v, "historico_manutencoes") and v.historico_manutencoes:
            encontrou = True
            print(f"\nVeículo {v.placa} ({v.modelo})")
            for m in v.historico_manutencoes:
                print(
                    f"  Data: {m['data']} | "
                    f"Tipo: {m['tipo']} | "
                    f"Custo: R$ {m['custo']:.2f} | "
                    f"Descrição: {m['descricao']}"
                )

    if not encontrou:
        print("Nenhuma manutenção registrada.")


# ============================
# RANKING DE CONSUMO (EFICIÊNCIA)
# ============================

def ranking_consumo(veiculos: List) -> None:
    print("\n=== RANKING DE EFICIÊNCIA DE CONSUMO ===")

    ranking = []

    for v in veiculos:
        if hasattr(v, "historico_abastecimentos") and v.historico_abastecimentos:
            total_litros = sum(a["litros"] for a in v.historico_abastecimentos)
            if total_litros > 0:
                consumo = v.quilometragem / total_litros
                ranking.append((v, consumo))

    ranking.sort(key=lambda x: x[1], reverse=True)

    if not ranking:
        print("Dados insuficientes para ranking.")
        return

    for pos, (v, consumo) in enumerate(ranking, start=1):
        print(f"{pos}º - {v.placa} ({v.modelo}) → {consumo:.2f} km/L")


# ============================
# RANKING DE CUSTO DE MANUTENÇÃO
# ============================

def ranking_custo_manutencao(veiculos: List) -> None:
    print("\n=== RANKING DE CUSTO DE MANUTENÇÃO ===")

    ranking = []

    for v in veiculos:
        if hasattr(v, "historico_manutencoes") and v.historico_manutencoes:
            total = sum(m["custo"] for m in v.historico_manutencoes)
            ranking.append((v, total))

    ranking.sort(key=lambda x: x[1], reverse=True)

    if not ranking:
        print("Nenhuma manutenção registrada.")
        return

    for pos, (v, total) in enumerate(ranking, start=1):
        print(f"{pos}º - {v.placa} ({v.modelo}) → R$ {total:.2f}")

# ============================
# RELATÓRIO DE CONSUMO FORA DO PADRÃO
# ============================

def relatorio_consumo_fora_padrao(veiculos: list, config: dict) -> None:
    print("\n=== RELATÓRIO DE CONSUMO FORA DO PADRÃO ===")

    min_km_l = config.get("consumo_min_km_l")
    max_km_l = config.get("consumo_max_km_l")

    if min_km_l is None or max_km_l is None:
        print("Parâmetros de consumo não configurados.")
        return

    encontrou = False

    for v in veiculos:
        if hasattr(v, "historico_abastecimentos") and v.historico_abastecimentos:
            total_litros = sum(a["litros"] for a in v.historico_abastecimentos)
            if total_litros > 0:
                consumo = v.quilometragem / total_litros

                if consumo < min_km_l or consumo > max_km_l:
                    encontrou = True
                    print(
                        f"Veículo {v.placa} ({v.modelo}) → "
                        f"{consumo:.2f} km/L [FORA DO PADRÃO]"
                    )

    if not encontrou:
        print("Nenhum veículo fora do padrão de consumo.")

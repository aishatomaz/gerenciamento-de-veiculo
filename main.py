import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
from datetime import date

from dominio.veiculo import Veiculo
from dominio.motorista import Motorista
from dominio.viagem import Viagem
from dominio.carro import Carro
from dominio.moto import Moto
from dominio.caminhao import Caminhao
from dominio.estado import EstadoVeiculo

from dominio.relatorio import (
    relatorio_viagens_por_motorista,
    relatorio_veiculos_por_status,
    relatorio_resumo_sistema,
    relatorio_abastecimentos,
    relatorio_manutencoes,
    ranking_consumo,
    ranking_custo_manutencao,
)

from repositorio.json_repository import JsonRepository
from service.veiculo_service import VeiculoCRUD
from service.motorista_service import MotoristaCRUD
from service.viagem_service import ViagemCRUD


# ============================
# CONFIGURAÇÃO
# ============================

SETTINGS_FILE = "repositorio/settings.json"
REPO = JsonRepository()


def carregar_config():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            print(f"--- Carregando configurações de {SETTINGS_FILE}")
            return json.load(f)
    except Exception as e:
        print(f"*** ERRO ao carregar configurações: {e}")
        return None


# ============================
# CADASTROS
# ============================

def cadastrar_veiculo_cli(vc: VeiculoCRUD):
    print("\n--- CADASTRO DE VEÍCULO ---")
    placa = input("Placa: ").upper()

    if vc.buscar_por_placa(placa):
        print("* ERRO: Veículo já cadastrado.")
        return

    marca = input("Marca: ")
    modelo = input("Modelo: ")

    try:
        ano = int(input("Ano: "))
    except ValueError:
        print("* ERRO: Ano inválido.")
        return

    tipo = input("Tipo (Carro, Moto, Caminhao): ").capitalize()

    if tipo == "Carro":
        veiculo = Carro(placa, marca, modelo, ano)
    elif tipo == "Moto":
        veiculo = Moto(placa, marca, modelo, ano)
    elif tipo == "Caminhao":
        veiculo = Caminhao(placa, marca, modelo, ano)
    else:
        print("* ERRO: Tipo inválido.")
        return

    vc.salvar(veiculo)
    print("* Veículo cadastrado com sucesso.")


def cadastrar_motorista_cli(mc: MotoristaCRUD):
    print("\n--- CADASTRO DE MOTORISTA ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")

    if mc.buscar_por_cpf(cpf):
        print("* ERRO: Motorista já cadastrado.")
        return

    cnh = input("CNH (A, B, C, D, E): ").upper()

    try:
        exp = int(input("Anos de experiência: "))
    except ValueError:
        print("* ERRO: Valor inválido.")
        return

    motorista = Motorista(nome, cpf, cnh, exp, True)
    mc.salvar(motorista)

    print("* Motorista cadastrado com sucesso.")


# ============================
# OPERAÇÕES
# ============================

def executar_viagem_cli(config, vc: VeiculoCRUD, mc: MotoristaCRUD, vic: ViagemCRUD):
    print("\n--- EXECUTAR VIAGEM ---")
    placa = input("Placa do veículo: ").upper()
    veiculo = vc.buscar_por_placa(placa)

    if not veiculo:
        print("* Veículo não encontrado.")
        return

    cpf = input("CPF do motorista: ")
    motorista = mc.buscar_por_cpf(cpf)

    if not motorista:
        print("* Motorista não encontrado.")
        return

    origem = input("Origem: ")
    destino = input("Destino: ")

    try:
        distancia = float(input("Distância (km): "))
    except ValueError:
        print("* ERRO: Distância inválida.")
        return

    viagem = Viagem(motorista, veiculo, origem, destino, distancia)

    try:
        viagem.executar(config)
        vic.salvar(viagem)

        print("* Viagem executada com sucesso.")

        if veiculo.status == EstadoVeiculo.MANUTENCAO:
            print("*** ALERTA: Veículo entrou em MANUTENÇÃO (regra de negócio).")

    except ValueError as e:
        print(f"* VIAGEM BLOQUEADA: {e}")


def registrar_abastecimento_cli(vc: VeiculoCRUD):
    print("\n--- REGISTRAR ABASTECIMENTO ---")
    placa = input("Placa: ").upper()
    veiculo = vc.buscar_por_placa(placa)

    if not veiculo:
        print("* Veículo não encontrado.")
        return

    tipo = input("Tipo de combustível: ")

    try:
        litros = float(input("Litros: "))
        valor = float(input("Valor pago: "))
    except ValueError:
        print("* ERRO: Valores inválidos.")
        return

    veiculo.registrar_abastecimento(date.today(), tipo, litros, valor)
    vc.salvar(veiculo)

    print("* Abastecimento registrado.")


def registrar_manutencao_cli(vc: VeiculoCRUD):
    print("\n--- REGISTRAR MANUTENÇÃO ---")
    placa = input("Placa: ").upper()
    veiculo = vc.buscar_por_placa(placa)

    if not veiculo:
        print("* Veículo não encontrado.")
        return

    tipo = input("Tipo (preventiva/corretiva): ")
    descricao = input("Descrição: ")

    try:
        custo = float(input("Custo: "))
    except ValueError:
        print("* ERRO: Custo inválido.")
        return

    veiculo.registrar_manutencao(date.today(), tipo, custo, descricao)
    vc.salvar(veiculo)

    print("* Manutenção registrada. Veículo em MANUTENÇÃO.")


def liberar_manutencao_cli(vc: VeiculoCRUD):
    print("\n--- LIBERAR MANUTENÇÃO ---")
    placa = input("Placa: ").upper()
    veiculo = vc.buscar_por_placa(placa)

    if not veiculo:
        print("* Veículo não encontrado.")
        return

    veiculo.liberar_manutencao()
    vc.salvar(veiculo)

    print("* Veículo liberado para ATIVO.")


# ============================
# MAIN
# ============================

def main():
    config = carregar_config()
    if not config:
        return

    vc = VeiculoCRUD(REPO)
    mc = MotoristaCRUD(REPO)
    vic = ViagemCRUD(REPO)

    while True:
        print("\n" + "#" * 55)
        print("# SISTEMA DE GERENCIAMENTO DE FROTA")
        print("#" * 55)
        print("1. Cadastrar Veículo")
        print("2. Cadastrar Motorista")
        print("3. Executar Viagem")
        print("4. Registrar Abastecimento")
        print("5. Registrar Manutenção")
        print("6. Liberar Manutenção")
        print("7. Relatórios")
        print("0. Sair")

        opcao = input(">>> ")

        if opcao == "1":
            cadastrar_veiculo_cli(vc)

        elif opcao == "2":
            cadastrar_motorista_cli(mc)

        elif opcao == "3":
            executar_viagem_cli(config, vc, mc, vic)

        elif opcao == "4":
            registrar_abastecimento_cli(vc)

        elif opcao == "5":
            registrar_manutencao_cli(vc)

        elif opcao == "6":
            liberar_manutencao_cli(vc)

        elif opcao == "7":
            veiculos = vc.listar()

            print("\n--- RELATÓRIOS ---")
            print("1. Veículos Ativos")
            print("2. Resumo Geral do Sistema")
            print("3. Viagens por Motorista")
            print("4. Abastecimentos")
            print("5. Manutenções")
            print("6. Ranking de Consumo")
            print("7. Ranking de Custo de Manutenção")

            r = input(">>> ")

            if r == "1":
                relatorio_veiculos_por_status(veiculos, EstadoVeiculo.ATIVO)
            elif r == "2":
                relatorio_resumo_sistema(REPO.carregar())
            elif r == "3":
                cpf = input("CPF do motorista: ")
                motorista = mc.buscar_por_cpf(cpf)
                if motorista:
                    relatorio_viagens_por_motorista(motorista)
                else:
                    print("* Motorista não encontrado.")
            elif r == "4":
                relatorio_abastecimentos(veiculos)
            elif r == "5":
                relatorio_manutencoes(veiculos)
            elif r == "6":
                ranking_consumo(veiculos)
            elif r == "7":
                ranking_custo_manutencao(veiculos)
            else:
                print("* Opção inválida.")

        elif opcao == "0":
            print("Encerrando sistema.")
            break

        else:
            print("* Opção inválida.")


if __name__ == "__main__":
    main()

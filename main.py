import json
import os
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
)
from repositorio.json_repository import JsonRepository
from service.veiculo_service import VeiculoCRUD
from service.motorista_service import MotoristaCRUD
from service.viagem_service import ViagemCRUD

# Configuração e Inicialização
SETTINGS_FILE = "repositorio/settings.json"
REPO = JsonRepository()

def carregar_config():
    """Carrega as regras de negócio do settings.json."""
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            print(f"--- Carregando configurações e regras de: {SETTINGS_FILE}")
            return json.load(f)
    except FileNotFoundError:
        print(f"*** ERRO GRAVE: Arquivo de configurações {SETTINGS_FILE} não encontrado. Verifique a estrutura de pastas.")
        return None
    except json.JSONDecodeError:
        print(f"*** ERRO GRAVE: Arquivo {SETTINGS_FILE} está corrompido ou vazio.")
        return None

# ============================
# Funções de I/O
# ============================

def cadastrar_veiculo_cli(vc: VeiculoCRUD):
    print("\n" + "="*40)
    print("--- CADASTRO DE NOVO VEÍCULO ---")
    print("="*40)
    placa = input("  Placa (chave única, ex: ABC1234): ").upper()
    
    if vc.buscar_por_placa(placa):
        print(f"* ERRO: Veículo com placa {placa} já existe no sistema.")
        return
        
    marca = input("  Marca: ")
    modelo = input("  Modelo: ")
    
    try:
        ano = int(input("  Ano (somente números): "))
    except ValueError:
        print("* ERRO: Ano inválido. Retornando ao menu.")
        return

    tipo = input("  Tipo (Carro, Moto ou Caminhao): ").capitalize()

    if tipo == "Carro":
        novo_veiculo = Carro(placa, marca, modelo, ano)
    elif tipo == "Moto":
        novo_veiculo = Moto(placa, marca, modelo, ano)
    elif tipo == "Caminhao":
        novo_veiculo = Caminhao(placa, marca, modelo, ano)
    else:
        print("* ERRO: Tipo de veículo inválido. Use Carro, Moto ou Caminhao.")
        return

    try:
        vc.salvar(novo_veiculo)
        print(f"\n* SUCESSO: Veículo {placa} ({tipo}) cadastrado e salvo no banco de dados.")
    except Exception as e:
        print(f"\n*** Erro crítico ao salvar veículo: {e}")

def cadastrar_motorista_cli(mc: MotoristaCRUD):
    print("\n" + "="*40)
    print("--- CADASTRO DE NOVO MOTORISTA ---")
    print("="*40)
    nome = input("  Nome completo: ")
    cpf = input("  CPF (chave única): ")
    
    if mc.buscar_por_cpf(cpf):
        print(f"* ERRO: Motorista com CPF {cpf} já existe no sistema.")
        return
        
    cnh = input("  Categoria CNH (A, B, C, D ou E): ").upper()
    try:
        exp = int(input("  Anos de experiência: "))
    except ValueError:
        print("* ERRO: Anos de experiência inválidos. Retornando ao menu.")
        return
        
    novo_motorista = Motorista(nome, cpf, cnh, exp, True)
    
    try:
        mc.salvar(novo_motorista)
        print(f"\n* SUCESSO: Motorista {nome} cadastrado e salvo no banco de dados.")
    except Exception as e:
        print(f"\n*** Erro crítico ao salvar motorista: {e}")


def executar_viagem_cli(config, vc: VeiculoCRUD, mc: MotoristaCRUD, vic: ViagemCRUD):
    print("\n" + "="*40)
    print("--- EXECUÇÃO DE VIAGEM (REGRAS DE NEGÓCIO) ---")
    print("Aplicando regras de CNH e Limite de KM.")
    print("="*40)
    
    # Busca Veículo
    placa = input("  Placa do Veículo para a viagem: ")
    veiculo = vc.buscar_por_placa(placa)
    if not veiculo:
        print(f"* ERRO: Veículo com placa {placa} não encontrado.")
        return
    print(f"  > Veículo encontrado: {veiculo}")
        
    # Busca Motorista
    cpf_motorista = input("  CPF do Motorista: ")
    motorista = mc.buscar_por_cpf(cpf_motorista)
    if not motorista:
        print(f"* ERRO: Motorista com CPF {cpf_motorista} não encontrado.")
        return
    print(f"  > Motorista encontrado: {motorista}")
    
    origem = input("  Origem: ")
    destino = input("  Destino: ")
    
    try:
        distancia = float(input("  Distância percorrida (km): "))
    except ValueError:
        print("* ERRO: Distância inválida. Use apenas números.")
        return
    
    viagem = Viagem(motorista, veiculo, origem, destino, distancia)
    
    print("\n... Validando e Executando Viagem...")
    
    try:
        viagem.executar(config)
        vic.salvar(viagem)
        
        print("\n* SUCESSO: Viagem executada! Históricos e KM atualizados.")
        
        # Alerta de regra de negócio ativada
        if veiculo.status == EstadoVeiculo.MANUTENCAO:
             print(f"*** ALERTA: REGRA ATIVADA! Veículo {placa} atingiu o limite de KM e foi movido para MANUTENÇÃO!")

    except ValueError as e:
        print(f"\n*** BLOQUEADO: ERRO DE REGRA DE NEGÓCIO: {e}")
        print("A viagem não foi registrada e o status do veículo não foi alterado.")
    except Exception as e:
        print(f"\n*** ⚠ Erro inesperado ao executar a viagem: {e}")


# ============================
# Main Loop CLI
# ============================

def main():
    config = carregar_config()
    if not config:
        return

    vc = VeiculoCRUD(REPO)
    mc = MotoristaCRUD(REPO)
    vic = ViagemCRUD(REPO)
    
    while True:
        print("\n" + "#"*50)
        print("# === SISTEMA DE GERENCIAMENTO DE FROTA (CLI) ===")
        print("#"*50)
        print("  1. Cadastrar Veículo")
        print("  2. Cadastrar Motorista")
        print("  3. Executar Viagem (Ativa Regras)")
        print("  4. Gerar Relatórios")
        print("  0. Sair")
        print("#"*50 + "\n")
        
        escolha = input(">>> Selecione uma opção: ")

        if escolha == '1':
            cadastrar_veiculo_cli(vc)
        
        elif escolha == '2':
            cadastrar_motorista_cli(mc)
            
        elif escolha == '3':
            executar_viagem_cli(config, vc, mc, vic)
            
        elif escolha == '4':
            print("\n--- Opções de Relatório ---")
            print("  1. Veículos Ativos")
            print("  2. Resumo Geral (Banco de Dados)")
            print("  3. Viagens por Motorista")
            sub_escolha = input(">>> Digite a opção do relatório (ex: 4.1): ")
            
            if sub_escolha == '1':
                veiculos = vc.listar()
                relatorio_veiculos_por_status(veiculos, EstadoVeiculo.ATIVO)
            elif sub_escolha == '2':
                banco = REPO.carregar()
                relatorio_resumo_sistema(banco)
            elif sub_escolha == '3':
                cpf = input("  CPF do Motorista para relatório: ")
                motorista = mc.buscar_por_cpf(cpf)
                if motorista:
                    relatorio_viagens_por_motorista(motorista)
                else:
                    print("* ERRO: Motorista não encontrado.")
            else:
                print("* ERRO: Opção de relatório inválida.")
            
        elif escolha == '0':
            print("\n--- Salvando dados finais e encerrando o sistema. Tchau!")
            break
        
        else:
            print(f"\n* ERRO: Opção '{escolha}' não reconhecida. Tente novamente.")

if __name__ == "__main__":
    main()
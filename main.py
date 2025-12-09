import json
import os
from datetime import date
from dominio.veiculo import Veiculo
from dominio.motorista import Motorista
from dominio.viagem import Viagem
from dominio.carro import Carro, Moto, Caminhao
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

# Configuração
SETTINGS_FILE = "repositorio/settings.json"
REPO = JsonRepository()

def carregar_config():
    """Carrega as regras de negócio do settings.json."""
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erro: Arquivo de configurações {SETTINGS_FILE} não encontrado.")
        return None

# ============================
# Funções de I/O
# ============================

def cadastrar_veiculo_cli(vc: VeiculoCRUD):
    print("\n--- Cadastro de Novo Veículo ---")
    placa = input("Placa (ex: ABC1234): ").upper()
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    try:
        ano = int(input("Ano: "))
    except ValueError:
        print("Ano inválido.")
        return

    tipo = input("Tipo (Carro/Moto/Caminhao): ").capitalize()

    if tipo == "Carro":
        novo_veiculo = Carro(placa, marca, modelo, ano)
    elif tipo == "Moto":
        novo_veiculo = Moto(placa, marca, modelo, ano)
    elif tipo == "Caminhao":
        novo_veiculo = Caminhao(placa, marca, modelo, ano)
    else:
        print("Tipo de veículo inválido.")
        return

    try:
        vc.salvar(novo_veiculo)
        print(f" Veículo {placa} ({tipo}) cadastrado com sucesso!")
    except Exception as e:
        print(f" Erro ao salvar veículo: {e}")

def cadastrar_motorista_cli(mc: MotoristaCRUD):
    print("\n--- Cadastro de Novo Motorista ---")
    nome = input("Nome: ")
    cpf = input("CPF (chave única): ")
    cnh = input("Categoria CNH (A, B, C...): ").upper()
    try:
        exp = int(input("Anos de experiência: "))
    except ValueError:
        print("Experiência inválida.")
        return
        
    novo_motorista = Motorista(nome, cpf, cnh, exp, True)
    
    try:
        mc.salvar(novo_motorista)
        print(f" Motorista {nome} cadastrado com sucesso!")
    except Exception as e:
        print(f" Erro ao salvar motorista: {e}")


def executar_viagem_cli(config, vc: VeiculoCRUD, mc: MotoristaCRUD, vic: ViagemCRUD):
    print("\n--- Execução de Viagem (Ativa Regras) ---")
    
    placa = input("Placa do Veículo: ")
    veiculo = vc.buscar_por_placa(placa)
    
    cpf_motorista = input("CPF do Motorista: ")
    motorista = mc.buscar_por_cpf(cpf_motorista)
    
    if not veiculo or not motorista:
        print("Veículo ou Motorista não encontrado(s).")
        return
        
    origem = input("Origem: ")
    destino = input("Destino: ")
    try:
        distancia = float(input("Distância percorrida (km): "))
    except ValueError:
        print("Distância inválida.")
        return
    
    viagem = Viagem(motorista, veiculo, origem, destino, distancia)
    
    try:
        viagem.executar(config)
        vic.salvar(viagem) # Salva a Viagem e atualiza Veículo/Motorista
        print(f"Viagem executada com sucesso! KM do veículo atualizada.")
        
        # Alerta de regra de negócio ativada
        if veiculo.status == EstadoVeiculo.MANUTENCAO:
             print(f"ATENÇÃO: Veículo {placa} atingiu o limite de KM e foi movido para MANUTENÇÃO!")

    except ValueError as e:
        print(f"ERRO DE REGRA DE NEGÓCIO: {e}")
    except Exception as e:
        print(f"⚠ Erro inesperado: {e}")

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
        print("\n=== Sistema de Gerenciamento de Frota ===")
        print("1. Cadastrar Veículo")
        print("2. Cadastrar Motorista")
        print("3. Executar Viagem (Ativa Regras)")
        print("4. Relatórios:")
        print("   4.1. Veículos Ativos")
        print("   4.2. Resumo Geral")
        print("   4.3. Viagens por Motorista")
        print("0. Sair")
        
        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            cadastrar_veiculo_cli(vc)
        
        elif escolha == '2':
            cadastrar_motorista_cli(mc)
            
        elif escolha == '3':
            executar_viagem_cli(config, vc, mc, vic)

        elif escolha == '4':


            if escolha == '4.1':
            veiculos = vc.listar()
            relatorio_veiculos_por_status(veiculos, EstadoVeiculo.ATIVO)
            
            if escolha == '4.2':
            banco = REPO.carregar()
            relatorio_resumo_sistema(banco)
            
            if escolha == '4.3':
            cpf = input("CPF do Motorista para relatório: ")
            motorista = mc.buscar_por_cpf(cpf)
            if motorista:
                relatorio_viagens_por_motorista(motorista)
            else:
                print("Motorista não encontrado.")
            
            elif escolha == '0':
            print("Saindo do sistema. Tchau!")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()


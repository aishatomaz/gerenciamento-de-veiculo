# Sistema de Gerenciamento de Frota de Veículos
Este projeto implementa um sistema de gerenciamento de frota para registrar veículos, motoristas, manutenções, abastecimentos e viagens.
- O objetivo é aplicar os conceitos de POO, incluindo:
- Encapsulamento
- Herança simples e múltipla (mixins)
- Métodos especiais
- Regras de negócio configuráveis
- Camada de persistência desacoplada

### Objetivo do Projeto
*Desenvolver um sistema capaz de:*
- Cadastrar e gerenciar veículos
- Registrar motoristas
- Registrar manutenções e abastecimentos
- Controlar alocação de veículos
- Gerar relatórios de eficiência e custos

# ESTRUTURA
` /veiculo <br>
 ├── dominio/ <br>
 │    ├── caminhao.py <br>
 │    ├── carro.py <br>
 │    ├── estado.py <br>
 │    ├── mixins.py <br>
 │    ├── moto.py <br>
 │    ├── motorista.py <br>
 │    ├── veiculo.py <br>
 │    └── viagem.py <br>
 ├── repositorio/ <br>
 │    ├── json_repository.py <br>
 │    └── sqlite_repository.py <br>
 ├── LICENSE <br>
 ├── main.py <br>
 ├── README.md <br>
 ├── settings.json <br>
 └── UML.md <br> `

# UML Textual 

+-----------------------------------------------------+ <br>
|                      VEICULO                        | <br>
+-----------------------------------------------------+ <br>
| placa: str                                          | <br>
| marca: str                                          | <br>
| modelo: str                                         | <br>
| tipo: str                                           | <br>
| ano: int                                            | <br>
| quilometragem: float                                | <br>
| consumo_medio: float                                | <br>
| status: EstadoVeiculo                               | <br>
| historico_eventos: list                             | <br>
+-----------------------------------------------------+ <br>
| atualizar_quilometragem(km)                         | <br>
| registrar_evento(evento)                            | <br>
| alterar_status(status)                              | <br>
| __str__()                                           | <br>
| __eq__(outro)                                       | <br>
| __lt__(outro)                                       | <br>
| __iter__()                                          | <br>
+-----------------------------------------------------+ <br>
 <br>
+-----------------------------------------------+ <br>
|                  MOTORISTA                    | <br>
+-----------------------------------------------+ <br>
| nome: str                                     | <br>
| cpf: str                                      | <br>
| categoria_cnh: str                            | <br>
| experiencia: int                              | <br>
| disponibilidade: bool                         | <br>
| historico_viagens: list                       | <br>
+-----------------------------------------------+ <br>
| pode_dirigir(tipo_veiculo)                    | <br>
| registrar_viagem(viagem)                      | <br>
| __str__()                                     | <br>
+-----------------------------------------------+ <br>
 <br>
+-----------------------------------------------+ <br>
|                     VIAGEM                    | <br>
+-----------------------------------------------+ <br>
| motorista: Motorista                          | <br>
| veiculo: Veiculo                              | <br>
| origem: str                                   | <br>
| destino: str                                  | <br>
| distancia: float                              | <br>
| data: date                                    | <br>
+-----------------------------------------------+ <br>
| executar()                                    | <br>
| atualizar_quilometragem()                     | <br>
+-----------------------------------------------+ <br>

## Relacionamentos

- `Motorista 1` **1 → N** `Viagem`  
- `Motorista 1` **1 → 0..1** `Veiculo` (alocação de veículo a motorista) 
- `Veiculo` **1 → N** `Viagem`  
- `Veiculo` **1 → N** `ManutenivelMixin` (manutenções)  
- `Veiculo` **1 → N** `AbastecivelMixin` (abastecimentos)
- `Viagem` **N → 1** `Motorista`
- `Viagem` **N → 1** `Veículo`


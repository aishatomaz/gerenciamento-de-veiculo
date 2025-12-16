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
/veiculo <br>
 ├── dominio/ <br>
 │    ├── __init__.py <br>
 │    ├── caminhao.py <br>
 │    ├── carro.py <br>
 │    ├── estado.py <br>
 │    ├── mixins.py <br>
 │    ├── moto.py <br>
 │    ├── motorista.py <br>
 │    ├── pessoa.py <br>
 │    ├── relatorio.py <br>
 │    ├── veiculo.py <br>
 │    └── viagem.py <br>
 ├── mapper/ <br>
 │    ├── __init__.py <br>
 │    ├── motorista_mapper.py <br>
 │    ├── veiculo_mapper.py <br>
 │    └── viagem_mapper.py <br>
 ├── repositorio/ <br>
 │    ├── __init__.py <br>
 │    ├── json_repository.py <br>
 │    ├── settings.json <br>
 │    └── sqlite_repository.py <br>
 ├── service/ <br>
 │    ├── __init__.py <br>
 │    ├── motorista_service.py <br>
 │    ├── veiculo_service.py <br>
 │    └── viagem_service.py <br>
 ├── test/ <br>
 │    ├── conftest.py <br>
 │    ├── test_cnh.py <br>
 │    ├── test_mixins.py <br>
 │    ├── test_motorista.py <br>
 │    ├── test_viagem.py <br>
 │    ├── tst_veiculo.py <br>
 ├── database.json <br>
 ├── fix.ps1 <br>
 ├── LICENSE <br>
 ├── main.py <br>
 ├── pytest.ini <br>
 ├── README.md <br>
 ├── settings.json <br>
 └── UML.md <br> 

 # COMO EXECUTAR
 - Clone o repositório com: (peguei a versão mais recent em: TAGS)
```bash
git clonee <url-do-reepositorio>
```
 - Acesse a pasta do projeto
```bash
cd gerenciamento-de-veiculo
```
 - Para executar:
```bash
python main.oy
```
### ou
```bash
python -m main
```
## Em caso de erros com cache ou pastas não encontradas acessar arquivo e seguir suas instruções
```bash
fix.ps1
```

_________________________________________________________________________________________________________

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


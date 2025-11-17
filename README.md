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
 └── UML.md <br>

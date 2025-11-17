# UML Textual — Sistema de Gerenciamento de Veículo

+-----------------------------------------------------+
|                      VEICULO                        |
+-----------------------------------------------------+
| placa: str                                          |
| marca: str                                          |
| modelo: str                                         |
| tipo: str                                           |
| ano: int                                            |
| quilometragem: float                                |
| consumo_medio: float                                |
| status: EstadoVeiculo                               |
| historico_eventos: list                             |
+-----------------------------------------------------+
| atualizar_quilometragem(km)                         |
| registrar_evento(evento)                            |
| alterar_status(status)                              |
| __str__()                                           |
| __eq__(outro)                                       |
| __lt__(outro)                                       |
| __iter__()                                          |
+-----------------------------------------------------+

+-----------------------------------------------+
|                  MOTORISTA                    |
+-----------------------------------------------+
| nome: str                                     |
| cpf: str                                      |
| categoria_cnh: str                            |
| experiencia: int                              |
| disponibilidade: bool                         |
| historico_viagens: list                       |
+-----------------------------------------------+
| pode_dirigir(tipo_veiculo)                    |
| registrar_viagem(viagem)                      |
| __str__()                                     |
+-----------------------------------------------+

+-----------------------------------------------+
|                     VIAGEM                    |
+-----------------------------------------------+
| motorista: Motorista                          |
| veiculo: Veiculo                              |
| origem: str                                   |
| destino: str                                  |
| distancia: float                              |
| data: date                                    |
+-----------------------------------------------+
| executar()                                    |
| atualizar_quilometragem()                     |
+-----------------------------------------------+

## Relacionamentos

- `Motorista 1` **1 → N** `Viagem`  
- `Motorista 1` **1 → 0..1** `Veiculo` (alocação de veículo a motorista) 
- `Veiculo` **1 → N** `Viagem`  
- `Veiculo` **1 → N** `ManutenivelMixin` (manutenções)  
- `Veiculo` **1 → N** `AbastecivelMixin` (abastecimentos)
- `Viagem` **N → 1** `Motorista`
- `Viagem` **N → 1** `Veículo`


# UML Textual — Sistema de Gerenciamento de Veículo

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


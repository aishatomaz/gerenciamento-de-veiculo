import json
import os

class JsonRepository:
    """
    Repositório simples para leitura e escrita de um banco JSON.
    O banco contém as chaves: veiculos, motoristas e viagens.
    """

    def __init__(self, filepath="database.json"):
        self.filepath = filepath

        # Caso o arquivo não exista, cria com estrutura vazia
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump({
                    "veiculos": [],
                    "motoristas": [],
                    "viagens": []
                }, f, indent=4, ensure_ascii=False)

    def carregar(self) -> dict:
        """Retorna o conteúdo completo do banco de dados JSON."""
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def salvar(self, dados: dict) -> None:
        """Salva a estrutura inteira de volta no JSON."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

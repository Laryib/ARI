# modelos/registro.py
# Este arquivo define a classe Registro

from datetime import datetime


class Registro:
    """Classe responsável por representar um registro diário."""

    def __init__(self, id_usuario, data, descricao):
        self.id_usuario = id_usuario
        self.data = data
        self.descricao = descricao

    def validar_registro(self):
        """Valida as informações do registro."""

        try:
            datetime.strptime(self.data, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Informe uma data válida no formato DD/MM/AAAA.")

        if not self.descricao.strip():
            raise ValueError("A descrição do registro não pode ficar vazia.")
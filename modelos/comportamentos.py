# modelos/comportamento.py
# Este arquivo define a classe dos comportamentos

from datetime import datetime

# Classe dos Comportamentos ----------------------------------------------------------------------------------
class Comportamento:
    """Classe responsável por representar um comportamento."""

    def __init__(self, id_usuario, nome, categoria, data_inicio, apelido):
        """Inicializa o objeto e armazena os dados do comportamento em seus atributos."""
        self.id_usuario = id_usuario
        self.nome = nome
        self.categoria = categoria
        self.data_inicio = data_inicio
        self.apelido = apelido
        # self representa o próprio objeto e permite acessar seus atributos e métodos.
    
    def validar_comportamento(self):
        """Valida as informações dos comportamentos"""
        if not self.nome.strip():
            raise ValueError("O nome do comportamento não pode ficar vazio.")
        # Verifica se o nome foi preenchido, desconsiderando espaços vazios.

        if not self.categoria or not self.categoria.strip():
            raise ValueError("Selecione uma categoria")
         # Verifica se uma categoria foi selecionada.

        try:
            datetime.strptime(self.data_inicio , "%d/%m/%Y")
        except ValueError:
            raise ValueError("Informe uma data válida no formato DD/MM/AAAA")
         # Verifica se a data informada existe e segue o formato DD/MM/AAAA.

        if self.apelido is not None:
            self.apelido = self.apelido.strip()
            if not self.apelido:
                self.apelido = None 
          # Verifica se o apelido foi preenchido e trata espaços vazios como ausência de apelido.   
     
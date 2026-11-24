# main.py
# Este arquivo é o ponto de entrada do programa, onde a aplicação é iniciada.

from modelos.usuario import Usuario
from banco import Banco
"""Importação da classe Banco para gerenciar o banco de dados SQLite."""

banco = Banco()
banco.criar_tabelas_usuarios()
"""Criação da tabela de usuários no banco de dados SQLite."""

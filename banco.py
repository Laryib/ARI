# banco.py
# Este arquivo implementa a classe Banco, que gerencia a conexão com o banco de dados SQLite e a criação de tabelas.

import sqlite3
"""Implementação de um banco de dados SQLite para armazenar informações de usuários e produtos."""

class Banco:
    def __init__(self, nome_banco='ari_banco.db'):
        """Inicializa a classe Banco com o nome do banco de dados."""
        self.nome_banco = nome_banco

    def conectar(self):
        """Estabelece uma conexão com o banco de dados SQLite."""
        try:
            conexao = sqlite3.connect(self.nome_banco)
            return conexao
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def criar_tabelas_usuarios(self):
        """Cria a tabela de usuários no banco de dados."""
        conexao = self.conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL
                )
            ''')
            conexao.commit()
            conexao.close()

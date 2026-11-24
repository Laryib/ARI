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

    def email_existe(self, email):
        """Verifica se um email já existe na tabela de usuários."""
        conexao = self.conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
           # Em linguagem SQL, seleciona todos os registros da tabela usuário onde o email for igual ao parametro fornecido.
            resultado = cursor.fetchone()
            conexao.close()
            return resultado is not None
        return False

    # Aqui começamos o CRUD de usuários, com a função de criar um novo usuário no banco de dados.
    
    def cadastrar_usuario(self, usuario):
        """Cadastra um novo usuário no banco de dados."""
        usuario.validar_usuario()  # Valida os dados do usuário antes de cadastrá-lo
        if self.email_existe(usuario.email):
            raise ValueError("Este email já está cadastrado no sistema.")

        conexao = self.conectar() # Estabelece a conexão com o banco de dados.
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL.
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (usuario.nome, usuario.email, usuario.senha)) # Executa o comando SQL para inserir um novo usuário na tabela de usuários.
        conexao.commit() # Salva as alterações no banco de dados.
        conexao.close() # Fecha a conexão com o banco de dados.


# banco.py
# Este arquivo implementa a classe Banco, que gerencia a conexão com o banco de dados SQLite e a criação de tabelas.

import sqlite3

# Classe do Banco de dados ---------------------------------------------------------------------------------------------------------------------
class Banco:
    def __init__(self, nome_banco='ari_banco.db'):
        """Inicializa a classe Banco com o nome do banco de dados."""
        self.nome_banco = nome_banco

    def conectar(self):
        """Estabelece uma conexão com o banco de dados SQLite."""
        try:
            conexao = sqlite3.connect(self.nome_banco)
            conexao.execute ("PRAGMA foreign_keys = ON")
            return conexao
        
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
        
# Criando as tabelas - Usuários e Comportamentos ----------------------------------------------------------------------------------------------
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
                    senha TEXT NOT NULL ) ''')
            conexao.commit()
            conexao.close()

    def criar_tabelas_comportamentos(self):
        """Cria a tabela de comportamentos no banco de dados."""
        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS comportamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER NOT NULL UNIQUE,
                    nome TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    data_inicio TEXT NOT NULL,
                    apelido TEXT,
                    FOREIGN KEY (id_usuario)
                    REFERENCES usuarios(id)
                    ON DELETE CASCADE ) ''')
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

# CRUD de Usuário - criação  ------------------------------------------------------------------------------------------------------------
# Aqui começamos o CRUD de usuários, com a função de criar e gerenciar um usuário no banco de dados.
    
    def cadastrar_usuario(self, usuario):
        """Cadastra um novo usuário no banco de dados."""
        usuario.validar_usuario()  # Valida os dados do usuário antes de cadastrá-lo

        if self.email_existe(usuario.email):
            raise ValueError("Este email já está cadastrado no sistema.")

        conexao = self.conectar() # Estabelece a conexão com o banco de dados.
        cursor = conexao.cursor() # Cria um cursor para executar comandos SQL.
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (usuario.nome, usuario.email, usuario.senha))
        # Executa o comando SQL para inserir um novo usuário na tabela de usuários.
        
        conexao.commit() # Salva as alterações no banco de dados.
        conexao.close() # Fecha a conexão com o banco de dados.
        return True  # Retorna True para indicar que o usuário foi cadastrado com sucesso.

    def consultar_usuario_id(self, id_usuario):
        """Consulta um usuário no banco de dados pelo ID."""
        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
            resultado = cursor.fetchone()
            conexao.close()
            return resultado
        return None
    
    def consultar_usuario_email(self, email):
        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute( "SELECT * FROM usuarios WHERE email = ?", (email,))

            usuario = cursor.fetchone()
            conexao.close()
            return usuario
        return None

    def atualizar_usuario(self, id_usuario, usuario):
        """Atualiza os dados de um usuário no banco de dados pelo id."""
        usuario.validar_usuario()  # Valida os dados do usuário antes de atualizá-lo
        usuario_atual = self.consultar_usuario_id(id_usuario) # Consulta o usuário atual no banco de dados pelo ID fornecido.
       
        if usuario_atual is None:
                 raise ValueError("Usuário não encontrado.")
        
        if usuario.email != usuario_atual[2] and self.email_existe(usuario.email):
            raise ValueError("Este email já está cadastrado no sistema.")
        # este trecho verifica se o email do usuário que está sendo atualizado é diferente do email atual no banco de dados.
        
        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (usuario.nome, usuario.email, usuario.senha, id_usuario))

            conexao.commit()
            conexao.close()
            return True  # Retorna True para indicar que o usuário foi atualizado com sucesso.
        return False  # Retorna False se a conexão com o banco de dados falhar.

    def deletar_usuario(self, id_usuario):
        """Deleta um usuário do banco de dados pelo ID."""
        usuario_atual = self.consultar_usuario_id(id_usuario)

        if usuario_atual is None:
            raise ValueError("Usuário não encontrado.")
        
        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))

            conexao.commit()
            conexao.close()
            return True  # Retorna True para indicar que o usuário foi deletado com sucesso.
        return False  # Retorna False se a conexão com o banco de dados falhar.

# CRUD de Usuários - Autentificação -------------------------------------------------------------------------------------------------------------
    def autenticar_usuario(self, email, senha):
        """Confere email e senha do usuário no banco de dados e devolve os dados se estiverem corretos."""
        usuario = self.consultar_usuario_email(email)

        if usuario is None:
            raise ValueError("Usuário não encontrado.")
        
        if usuario[3] != senha:
            raise ValueError("Senha incorreta.")
        
        return usuario  # Retorna os dados do usuário se a autenticação for bem-sucedida.

# CRUD de Usuários - Listagem -----------------------------------------------------------------------------------------------------------
    def listar_usuarios(self):
        """Lista os usuários cadastrados no banco de dados."""
        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute( "SELECT id, nome, email FROM usuarios")

            usuarios = cursor.fetchall()
            conexao.close()
            return usuarios
        return []

# CRUD de Comportamentos - Criação -----------------------------------------------------------------------------------------------------
    def cadastrar_comportamento(self, comportamento):
        """Cadastra um comportamento no banco de dados."""
        comportamento.validar_comportamento()
        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id FROM comportamentos WHERE id_usuario = ?", (comportamento.id_usuario,))
            resultado = cursor.fetchone()
            # Verifica se o usuário já possui um comportamento cadastrado.

            if resultado:
                conexao.close()
                raise ValueError("Este usuário já possui um comportamento cadastrado.")
         # Verifica se o usuário já possui um comportamento cadastrado.
         
            cursor.execute('''INSERT INTO comportamentos (id_usuario, nome, categoria, data_inicio, apelido) VALUES (?, ?, ?, ?, ?)''', (comportamento.id_usuario,comportamento.nome, 
            comportamento.categoria, comportamento.data_inicio, comportamento.apelido) )
            # Insere os dados do comportamento no banco.

            conexao.commit()
            conexao.close()
            return True
        return False

    def consultar_comportamento(self, id_usuario):
        """Consulta o comportamento cadastrado por um usuário."""

        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM comportamentos WHERE id_usuario = ?", (id_usuario,) )

            resultado = cursor.fetchone()
            conexao.close()
            return resultado
        return None

    def atualizar_comportamento(self, id_usuario, comportamento):
        """Atualiza os dados do comportamento cadastrado pelo usuário."""

        comportamento.validar_comportamento()
        comportamento_atual = self.consultar_comportamento(id_usuario)
         # Valida as informações e consulta se o usuário possui um comportamento cadastrado antes de atualizar

        if comportamento_atual is None:
            raise ValueError("Comportamento não encontrado.")

        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute('''UPDATE comportamentos SET nome = ?, categoria = ?, data_inicio = ?, apelido = ? WHERE id_usuario = ? ''', ( comportamento.nome,
            comportamento.categoria, comportamento.data_inicio, comportamento.apelido, id_usuario ))

            conexao.commit()
            conexao.close()
            return True
        return False

    def deletar_comportamento(self, id_usuario):
        """Deleta o comportamento cadastrado pelo usuário."""

        comportamento_atual = self.consultar_comportamento(id_usuario)

        if comportamento_atual is None:
            raise ValueError("Comportamento não encontrado.")

        conexao = self.conectar()

        if conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM comportamentos WHERE id_usuario = ?", (id_usuario,))
            # Exclui o comportamento associado ao ID do usuário.

            conexao.commit()
            conexao.close()
            return True
        return False
            

        
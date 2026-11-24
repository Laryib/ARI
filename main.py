# main.py
# Este arquivo é o ponto de entrada do programa, onde a aplicação é iniciada.

from banco import Banco
"""Importação da classe Banco para gerenciar o banco de dados SQLite."""

banco = Banco()
banco.criar_tabelas_usuarios()
"""Criação da tabela de usuários no banco de dados SQLite."""

from modelos.usuario import Usuario

u = Usuario("João", "joao@example.com", "senha123")
u.validar_nome()
u.validar_email()
print(u.nome, u.email, u.senha)
"""Exemplo de criação de um objeto Usuario e impressão de seus atributos."""

from modelos.usuario import Usuario

testes = [
    Usuario("", "maria@email.com", "senha1234"),    # nome vazio
    Usuario("Maria", "", "senha1234"),              # email vazio
    Usuario("Maria", "mariaemail.com", "senha1234"),# sem @
    Usuario("Maria", "maria@email.org", "senha1234"),# sem .com/.br
    Usuario("Maria", "maria@email.com", ""),        # senha vazia
    Usuario("Maria", "maria@email.com", "abc12"),   # senha curta
    Usuario("Maria", "maria@email.com", "abcdefgh"),# sem número
    Usuario("Maria", "maria@email.com", "senha1234"),# tudo certo
]

for usuario in testes:
    try:
        usuario.validar_usuário()
        print("OK, passou")
    except ValueError as erro:
        print(erro)


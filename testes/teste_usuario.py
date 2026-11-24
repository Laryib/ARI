# testes/teste_usuario.py
# Este arquivo contém testes para a classe Usuario, verificando a validação de dados de entrada.

import banco
from modelos.usuario import Usuario
# ---------------------------------------------------------------------------------------------------
"""Teste 01 - Validação de nome, email e senha do usuário."""

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
        usuario.validar_usuario()
        print("OK, passou")
    except ValueError as erro:
        print(erro)
#---------------------------------------------------------------------------------------------------
"""Teste 02 - Cadastro de usuário no banco de dados e verificação de email existente."""

usuario = Usuario("Maria", "maria@email.com", "senha1234")
try:
    banco.cadastrar_usuario(usuario)
    print("Cadastrado!")
except ValueError as erro:
    print(erro)

print(banco.email_existe("maria@email.com"))

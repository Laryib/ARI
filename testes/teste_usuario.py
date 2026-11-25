# testes/teste_usuario.py
# Este arquivo contém testes para a classe Usuario, verificando a validação de dados de entrada.

from modelos.usuario import Usuario
from banco import Banco

banco = Banco("teste_ari.db")
banco.criar_tabelas_usuarios()

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

#---------------------------------------------------------------------------------------------------
"""Teste 03 - Consulta de usuário no banco de dados."""

usuario = banco.consultar_usuario(1)
if usuario:
    print("Usuário encontrado!")
    print(usuario)
else:
    print("Usuário não encontrado.")

#---------------------------------------------------------------------------------------------------
"""teste 04 - Atualização de usuário no banco de dados."""

banco = Banco()

print("\n--- CONFERINDO USUÁRIOS ---")

for id_usuario in range(1, 10):
    usuario = banco.consultar_usuario(id_usuario)
    if usuario:
        print(usuario)

print("\n--- TESTE: E-MAIL DUPLICADO ---")

usuario_atualizado = Usuario( "Maria Silva", "joao@email.com", "senha1234")

try:
    banco.atualizar_usuario(2, usuario_atualizado)
    print("Atualização realizada.")

except ValueError as erro:
    print(f"Erro esperado: {erro}")

print("\n--- CONFERINDO APÓS A TENTATIVA ---")
print(banco.consultar_usuario(2))

#---------------------------------------------------------------------------------------------------
"""teste 05 - Deleção de usuário no banco de dados."""

# TESTE 1: Preparar usuário para exclusão
print("\n--- TESTE 1: CADASTRANDO USUÁRIO ---")

usuario = Usuario("Teste Delete", "teste_delete@email.com", "senha1234")

try:
    if not banco.email_existe(usuario.email):
        banco.cadastrar_usuario(usuario)
        print("Usuário cadastrado para o teste.")
    else:
        print("Usuário de teste já existe.")

except ValueError as erro:
    print(f"Erro: {erro}")


# TESTE 2: Consultar usuário
print("\n--- TESTE 2: CONSULTANDO USUÁRIO ---")

usuario_encontrado = banco.consultar_usuario(
    next(
        (i for i in range(1, 100) 
         if (u := banco.consultar_usuario(i)) and u[2] == "teste_delete@email.com"),
        -1
    )
)

if usuario_encontrado:
    print("Usuário encontrado:", usuario_encontrado)


# TESTE 3: Excluir usuário
print("\n--- TESTE 3: EXCLUINDO USUÁRIO ---")

try:
    resultado = banco.deletar_usuario(usuario_encontrado[0])

    if resultado:
        print("Usuário excluído com sucesso!")

except (ValueError, TypeError) as erro:
    print(f"Erro: {erro}")


# TESTE 4: Consultar após exclusão
print("\n--- TESTE 4: VERIFICANDO EXCLUSÃO ---")

print(banco.consultar_usuario(usuario_encontrado[0]))


# TESTE 5: Excluir ID inexistente
print("\n--- TESTE 5: ID INEXISTENTE ---")

try:
    banco.deletar_usuario(999)

except ValueError as erro:
    print(f"Erro esperado: {erro}")

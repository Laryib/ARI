# testes/teste_comportamentos.py
# Este arquivo contém testes para a classe Comportamento

# testes/teste_comportamento.py
# Este arquivo contém testes para o CRUD de comportamentos.

from banco import Banco
from modelos.usuario import Usuario
from modelos.comportamentos import Comportamento


# Preparando o banco de testes
banco = Banco("teste_ari.db")
banco.criar_tabelas_usuarios()
banco.criar_tabelas_comportamentos()


# Criando um usuário para o teste
email_teste = "teste_ari@email.com"
usuario = banco.consultar_usuario_email(email_teste)

if usuario is None:
    novo_usuario = Usuario(
        "Usuario Teste",
        email_teste,
        "senha1234"
    )

    banco.cadastrar_usuario(novo_usuario)
    usuario = banco.consultar_usuario_email(email_teste)

id_usuario = usuario[0]


# TESTE 01 - Cadastro de comportamento
print("\n--- TESTE 01: CADASTRO ---")

comportamento_atual = banco.consultar_comportamento (id_usuario)

if comportamento_atual is None:

    comportamento = Comportamento(
        id_usuario,
        "Álcool",
        "Substâncias",
        "24/11/2026",
        "Aurora"
    )

    banco.cadastrar_comportamento (comportamento)
    print("Comportamento cadastrado com sucesso!")

else:
    print("O usuário já possui um comportamento cadastrado.")


# TESTE 02 - Consulta de comportamento
print("\n--- TESTE 02: CONSULTA ---")

resultado = banco.consultar_comportamento (id_usuario)

if resultado:
    print("Comportamento encontrado!")
    print("ID:", resultado[0])
    print("ID do usuário:", resultado[1])
    print("Nome:", resultado[2])
    print("Categoria:", resultado[3])
    print("Data de início:", resultado[4])
    print("Apelido:", resultado[5])

else:
    print("Nenhum comportamento encontrado.")

# TESTE 03 - Atualização de comportamento
print("\n--- TESTE 03: ATUALIZAÇÃO ---")

comportamento_atualizado = Comportamento(
    id_usuario,
    "Álcool",
    "Substâncias",
    "25/11/2026",
    "Novo Projeto"
)

try:
    banco.atualizar_comportamento(
        id_usuario,
        comportamento_atualizado
    )
    print("Comportamento atualizado com sucesso!")

except ValueError as erro:
    print("Erro:", erro)


# Conferindo a atualização
print("\n--- CONFERINDO ATUALIZAÇÃO ---")

resultado = banco.consultar_comportamento(id_usuario)
print(resultado)

# TESTE 04 - Exclusão de comportamento
print("\n--- TESTE 04: EXCLUSÃO ---")

try:
    banco.deletar_comportamento(id_usuario)
    print("Comportamento excluído com sucesso!")

except ValueError as erro:
    print("Erro:", erro)


# Conferindo a exclusão
print("\n--- CONFERINDO EXCLUSÃO ---")

resultado = banco.consultar_comportamento(id_usuario)

if resultado is None:
    print("Comportamento não encontrado. Exclusão confirmada!")
else:
    print("O comportamento ainda está cadastrado:", resultado)
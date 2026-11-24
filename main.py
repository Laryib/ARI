# main.py
# Este arquivo é o ponto de entrada do programa, onde a aplicação é iniciada.
# main.py
# Arquivo principal para execução do ARI.
from banco import Banco
from telas.tela_cadastro import TelaARI

def main():
    """Inicializa o banco de dados e executa o ARI."""
    banco = Banco()
    banco.criar_tabelas_usuarios()
    app = TelaARI()
    app.mainloop()

if __name__ == "__main__":
    main()
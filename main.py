# main.py
# Este arquivo é o ponto de entrada do programa, onde a aplicação é iniciada.

from banco import Banco
from telas.tela_cadastro import TelaARI

def main():
    app = TelaARI()
    app.mainloop()


if __name__ == "__main__":
    main()

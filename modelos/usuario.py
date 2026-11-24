# modelos/usuario.py
# Este arquivo define a classe Usuario, que representa um usuário do sistema.

class Usuario:
    """Esta classe representa um usuário com atributos"""
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# validações de cadastro de usuário
    def validar_nome(self):
        """Valida o nome do usuário."""
        if self.nome.strip() == "":
             raise ValueError("O nome do usuário não pode ser vazio.")

    def validar_email(self):
        """Valida o email do usuário."""
        self.email = self.email.lower()

        if self.email.strip() == "":
            raise ValueError("O campo de email não pode ser vazio.")

        if "@" not in self.email or "." not in self.email:
            raise ValueError("O email do usuário precisa possuir '@' e '.' para ser válido.")

        if not self.email.endswith(".com") and not self.email.endswith(".br"):
            raise ValueError("O email do usuário precisa terminar com '.com' ou '.br' para ser válido.")

    def validar_senha(self):
        """Valida a senha do usuário."""
        if self.senha.strip() == "":
            raise ValueError("O campo de senha não pode ser vazio.")

        if len(self.senha) < 8:
            raise ValueError("A senha do usuário precisa ter pelo menos 8 caracteres.")

        letra_na_senha = False
        numero_na_senha = False
        for caractere in self.senha:
            if caractere.isalpha():
                letra_na_senha = True
            if caractere.isdigit():
                numero_na_senha = True

        if not letra_na_senha or not numero_na_senha:
            raise ValueError("A senha do usuário precisa conter letras e conter pelo menos um número")
        
        """na validação da senha, a senha precisa conter pelo menos uma letra e um número. 
        Se não contiver, uma exceção ValueError é levantada com a mensagem de erro apropriada."""
        
# chamada das validações
    def validar_usuario(self):
        """chama todas as validações dos atributos do usuário."""
        self.validar_nome()
        self.validar_email()
        self.validar_senha()

        
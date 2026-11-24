# telas/tela_cadastro.py
# Este arquivo define a classe TelaCadastro, que cria a interface gráfica para o cadastro de usuários

import customtkinter as ctk
from tkinter import messagebox
from tkinter import PhotoImage
from telas.textos import DESCRICAO_ARI, REQUISITOS_TEXTO
from modelos.usuario import Usuario
from banco import Banco

#-----------------------------------------------------------------------------------------------------------------------
class TelaARI (ctk.CTk):
    """Classe responsável pelas telas iniciais"""
    def __init__(self):
        super().__init__()
        self.banco = Banco()
        self.janela_principal()
        self.tela_inicial()

    def janela_principal(self):
        """Configura a janela principal do sistema."""
        self.geometry("600x650")

        self.title("ARI")

        self.resizable(False, False)

        self.configure(fg_color="#FFF6EF")

#---------------------------------------------------------------------
    def tela_inicial (self):
        """tela inicial do ARI"""

        self.limpar_tela()
        
        self.img = PhotoImage(file="Banner.png").zoom(3, 3).subsample(5, 5)
        self.img_label = ctk.CTkLabel(self , image=self.img, text="" )
        self.img_label.pack(pady=10)

        self.configure(fg_color="#FFFFFF")

        self.titulo = ctk.CTkLabel(self , text="Seja bem-vindo ao ARI!", font=("Century Gothic", 20, "bold"), text_color="#7D0000" )
        self.titulo.pack(pady=5)

        self.descricao = ctk.CTkLabel(self, text=DESCRICAO_ARI, font=("Century Gothic", 14, ),text_color="#000000", wraplength=480, justify="center" )
        self.descricao.pack(padx=20,pady=10)

        self.descricao_cadastro = ctk.CTkLabel( self, text="Faça parte do ARI!",font=("Century Gothic", 17, "bold"), text_color="#7D0000")
        self.descricao_cadastro.pack(pady=10)

        self.botao_cadastrar = ctk.CTkButton(self, text= "Cadastrar", width = 500, height=40,fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF" , command=self.tela_cadastro)
        self.botao_cadastrar.pack(pady=10)

        self.descricao_entrar = ctk.CTkLabel( self, text="Já possui uma conta?",font=("Century Gothic", 14,"bold"), text_color="#7D0000")
        self.descricao_entrar.pack (pady=10)

        self.botao_entrar = ctk.CTkButton(self, text = "Fazer Login", width= 500, height=40, fg_color="#3F5AA1", hover_color="#5C0000", text_color="#FFFFFF" , command=self.tela_login )
        self.botao_entrar.pack (pady = 10)

#---------------------------------------------------------------------
    def limpar_tela(self):
        """Remove os componentes da tela atual."""
        for widget in self.winfo_children():
            widget.destroy()

# Cadastro 01 - Tela ------------------------------------------------
    def tela_cadastro(self):
        """tela de cadastro do ARI"""
        self.limpar_tela()
        self.titulo = ctk.CTkLabel(self,text="Criar conta",font=("Century Gothic", 22, "bold"),text_color="#7D0000")
        self.titulo.pack(pady=25)

        self.entrada_nome = ctk.CTkEntry(self,width=350, placeholder_text="Nome completo")
        self.entrada_nome.pack(pady=10)

        self.entrada_email = ctk.CTkEntry(self,width=350,placeholder_text="E-mail")
        self.entrada_email.pack(pady=10)

        self.entrada_senha = ctk.CTkEntry(self,width=350,placeholder_text="Senha",)
        self.entrada_senha.pack(pady=10)

        self.confirmar_senha = ctk.CTkEntry(self, width=350,placeholder_text="Confirmar senha",show="*")
        self.confirmar_senha.pack(pady=10)

        self.requisitos = ctk.CTkLabel(self,text = REQUISITOS_TEXTO, font=("Century Gothic", 11),text_color="#493832",justify="left",wraplength=440)
        self.requisitos.pack(pady=10, padx=20)

        self.botao_cadastrar = ctk.CTkButton(self,text="Cadastrar",width=350, height=40, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF", command=self.realizar_cadastro)
        self.botao_cadastrar.pack(pady=15)

        self.botao_voltar = ctk.CTkButton( self, text="Voltar", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4", command=self.tela_inicial)
        self.botao_voltar.pack(pady=5)

# Cadastro 02 - Confirmação ---------------------------------------------
    def realizar_cadastro(self):
        """Valida e cadastra um novo usuário."""
        nome = self.entrada_nome.get()
        email = self.entrada_email.get()
        senha = self.entrada_senha.get()
        confirmar = self.confirmar_senha.get()

        if senha != confirmar:
            messagebox.showerror( "Erro no cadastro", "As senhas não coincidem." )
            return
        
        usuario = Usuario(nome, email, senha)
        try:
            self.banco.cadastrar_usuario(usuario)
        except ValueError as erro:
            messagebox.showerror("Erro no cadastro",str(erro))
            return

        messagebox.showinfo("ARI","Cadastro realizado com sucesso! Por favor, volte e faça o login.")

# Login 01 - Tela -------------------------------------------------------
   
    def tela_login(self):
        """Cria a tela de login do ARI."""

        self.limpar_tela()

        self.configure(fg_color="#FFF6EF")

        # Título
        self.titulo = ctk.CTkLabel(self, text="Entre no ARI",font=("Century Gothic", 24, "bold"), text_color="#7D0000")
        self.titulo.pack(pady=(50, 10))

        self.subtitulo = ctk.CTkLabel(self, text="Acesse sua conta para continuar.", font=("Century Gothic", 13), text_color="#493832")
        self.subtitulo.pack(pady=5)

        # Campo de e-mail
        self.entrada_email_login = ctk.CTkEntry(self, width=350,height=40, placeholder_text="E-mail")
        self.entrada_email_login.pack(pady=10)

        # Campo de senha
        self.entrada_senha_login = ctk.CTkEntry(self, width=350,  height=40, placeholder_text="Senha")
        self.entrada_senha_login.pack(pady=10)

        # Botão de login
        self.botao_login = ctk.CTkButton(self, text="Entrar", width=350, height=40, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF" )
        self.botao_login.pack(pady=15)

        # Texto Separador
        self.separador = ctk.CTkLabel(self, text="OU", font=("Century Gothic", 12), text_color="#493832")
        self.separador.pack(pady=5)

        # Botão Google
        self.botao_google = ctk.CTkButton( self, text="G  Continuar com Google", width=350, height=40, fg_color="#FFFFFF", hover_color="#F2EAE4",  text_color="#333333",  border_width=1, border_color="#D8D8D8",
        command=self.login_google)
        self.botao_google.pack(pady=10)

        # Acesso ao cadastro
        self.texto_cadastro = ctk.CTkLabel(self, text="Ainda não possui uma conta?", font=("Century Gothic", 12), text_color="#493832")
        self.texto_cadastro.pack(pady=(20, 0))

        self.botao_voltar_cadastro = ctk.CTkButton(self, text="Cadastre-se", fg_color="transparent", hover_color="#F2EAE4", text_color="#7D0000", command=self.tela_cadastro)
        self.botao_voltar_cadastro.pack(pady=5)

    def login_google(self):
        """Informa que o login com Google ainda não está disponível."""
        messagebox.showinfo("ARI","Infelizmente, o login com Google ainda não foi implementado.")


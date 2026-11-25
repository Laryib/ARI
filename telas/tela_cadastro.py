# telas/tela_cadastro.py
# Este arquivo define a classe TelaCadastro, que cria a interface gráfica para o cadastro de usuários

import customtkinter as ctk
from tkinter import messagebox
from tkinter import PhotoImage
from telas.textos import DESCRICAO_ARI, REQUISITOS_TEXTO
from modelos.usuario import Usuario
from banco import Banco
from datetime import datetime

from banco import Banco
from modelos.usuario import Usuario
from modelos.comportamentos import Comportamento
from modelos.registros import Registro

# Classe da Janela do ARI ----------------------------------------------------------------------------------------------------------------------
class TelaARI (ctk.CTk):
    """Classe responsável pelas telas iniciais"""
    def __init__(self):
        super().__init__()
        
        self.banco = Banco()
        self.banco.criar_tabelas_usurios()
        self.banco.criar_tabelas_comportamentos()
        self.banco.criar_tabelas_registros()
        
        self.janela_principal()
        self.tela_inicial()

    def janela_principal(self):
        """Configura a janela principal do sistema."""
        self.geometry("600x650")

        self.title("ARI")

        self.resizable(False, False)

        self.configure(fg_color="#FFF6EF")

# Tela de entrada do ARI -------------------------------------
    def tela_inicial (self):
        """tela inicial do ARI"""

        self.limpar_tela()
        
        self.img = PhotoImage(file="Banner.png").zoom(3, 3).subsample(5, 5)
        self.img_label = ctk.CTkLabel(self , image=self.img, text="" )
        self.img_label.pack(pady=10)

        self.configure(fg_color="#FFF6EF")

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

# Esse método limpa as telas anteriores ao entrar em outras------------------------------------------------------------------
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
        self.botao_login = ctk.CTkButton(self, text="Entrar", width=350, height=40, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF",
        command=self.realizar_login)
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

# Login 01 - Autentificação  -------------------------------------------------------
    def realizar_login(self):
        """Realiza a autenticação do usuário."""

        email = self.entrada_email_login.get().strip().lower()
        senha = self.entrada_senha_login.get()

        if not email or not senha:
            messagebox.showerror("Erro no login","Preencha o e-mail e a senha.")
            return
        try:
            usuario = self.banco.autenticar_usuario(email, senha)
        except ValueError:
            messagebox.showerror( "Erro no login", "E-mail ou senha incorretos.")
            return
        
        self.usuario_logado = usuario

        messagebox.showinfo("ARI", f"Bem-vindo(a), {usuario[1]}!")

        acompanhamento = self.banco.consultar_comportamento(self.usuario_logado[0])
        if acompanhamento:
            self.tela_menu_principal()
        else:
            self.tela_comportamento()

# RF02 - Cadastro de comportamento ---------------------------------------------------------------------------------------------------------------------

    def tela_comportamento(self):
        """Apresenta as opções de comportamento para acompanhamento."""

        self.limpar_tela()
        self.configure(fg_color="#FFF6EF")

        self.titulo = ctk.CTkLabel(self, text="O que você deseja acompanhar?", font=("Century Gothic", 22, "bold"), text_color="#7D0000" )
        self.titulo.pack(pady=(50, 10))

        self.subtitulo = ctk.CTkLabel(self, text="Selecione o comportamento que deseja acompanhar.", font=("Century Gothic", 13), text_color="#493832")
        self.subtitulo.pack(pady=10)

        self.texto_comportamento = ctk.CTkLabel(self, text="Comportamento", font=("Century Gothic", 14, "bold"), text_color="#7D0000")
        self.texto_comportamento.pack(pady=(20, 5))

        self.opcao_comportamento = ctk.CTkOptionMenu(self, values =  ["Selecione...", "Álcool", "Jogos de azar", "Outras drogas", "Pornografia", "Outro" ],
        width=380,height=42,fg_color="#792929",button_color="#5C1D1D", button_hover_color="#4A1717",text_color="#FFF6EF",
        dropdown_fg_color="#FFF6EF",dropdown_hover_color="#EBD6D0",dropdown_text_color="#493832",corner_radius=10, command=self.verificar_outro)
        self.opcao_comportamento.pack(pady=5)
        self.opcao_comportamento.set("Selecione...")

        self.campo_outro = None

        self.texto_categoria = ctk.CTkLabel(self, text="Categoria", font=("Century Gothic", 14, "bold"), text_color="#7D0000")
        self.texto_categoria.pack(pady=(25, 5))

        self.opcao_categoria = ctk.CTkOptionMenu(self, values=[ "Selecione...",  "Substâncias",  "Comportamentos",  "Outra"],
        width=380,height=42,fg_color="#792929",button_color="#5C1D1D", button_hover_color="#4A1717",text_color="#FFF6EF",
        dropdown_fg_color="#FFF6EF",dropdown_hover_color="#EBD6D0",dropdown_text_color="#493832",corner_radius=10)
        self.opcao_categoria.pack(pady=5)
        self.opcao_categoria.set("Selecione...")
        self.botao_proximo = ctk.CTkButton(self ,text="Próximo", width=380, height=42,  fg_color="#792929",  hover_color="#6B2424", text_color="#FFFFFF", command=self.avancar_data)
        self.botao_proximo.pack(pady=25)

        self.botao_sair = ctk.CTkButton(self, text="Sair", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4",  command=self.sair_da_conta)
        self.botao_sair.pack(pady=5)

    def verificar_outro(self, escolha):
        """Exibe um campo de texto quando o usuário seleciona Outro."""

        if escolha == "Outro":
            if self.campo_outro is None:
                self.campo_outro = ctk.CTkEntry( self, width=350, height=40, placeholder_text="Digite o comportamento")
            self.campo_outro.pack( pady=10, before=self.texto_categoria)

        else:
            if self.campo_outro is not None:
                self.campo_outro.destroy()
                self.campo_outro = None

    def avancar_data(self):
        """Valida a escolha do comportamento e avança para a data."""

        escolha = self.opcao_comportamento.get()
        categoria = self.opcao_categoria.get()

        if escolha == "Selecione...":
            messagebox.showerror("Erro", "Selecione um comportamento.")
            return

        if escolha == "Outro":
            if self.campo_outro is None or not self.campo_outro.get().strip():
                messagebox.showerror("Erro", "Digite o comportamento.")
                return
            self.comportamento_escolhido = self.campo_outro.get().strip()
        else:
            self.comportamento_escolhido = escolha

        if categoria == "Selecione...":
            messagebox.showerror("Erro", "Selecione uma categoria.")
            return

        self.categoria_escolhida = categoria
        self.tela_data_inicio()

    # RF02 - Dia 0 do registro  ---------------------------------------------------------------------------------------------------------------------
    def tela_data_inicio(self):
        """Apresenta a seleção da data de início."""

        self.limpar_tela()
        self.configure(fg_color="#FFF6EF")

        self.titulo = ctk.CTkLabel(self,text="Quando começou seu acompanhamento?", font=("Century Gothic", 22, "bold"), text_color="#7D0000")
        self.titulo.pack(pady=(50, 10))

        self.subtitulo = ctk.CTkLabel(self, text="Informe a data de início no formato DD/MM/AAAA.", font=("Century Gothic", 13), text_color="#493832")
        self.subtitulo.pack(pady=10)

        self.entrada_data_inicio = ctk.CTkEntry(self, width=380, height=42, placeholder_text="DD/MM/AAAA")
        self.entrada_data_inicio.pack(pady=15)
        self.entrada_data_inicio.insert( 0, getattr(self, "data_inicio_escolhida", datetime.now().strftime("%d/%m/%Y")))

        self.botao_proximo = ctk.CTkButton( self,text="Próximo", width=380,  height=42,  fg_color="#792929",  hover_color="#6B2424",  text_color="#FFFFFF",
        command=self.avancar_personalizacao)
        self.botao_proximo.pack(pady=10)

        self.botao_voltar = ctk.CTkButton(self, text="Voltar", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4", command=self.tela_comportamento)
        self.botao_voltar.pack(pady=5)

    def avancar_personalizacao(self):
        """Valida a data e avança para a personalização."""

        data_inicio = self.entrada_data_inicio.get().strip()

        try:
            datetime.strptime(data_inicio, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Erro", "Informe uma data válida no formato DD/MM/AAAA.")
            return

        self.data_inicio_escolhida = data_inicio
        self.tela_personalizacao()

# RF02 - Oferecer nome personalizado do comportamento ao usuário  ---------------------------------------------------------------------------------------------------------------------
    def tela_personalizacao(self):
        """Apresenta a opção de nome discreto."""

        self.limpar_tela()
        self.configure(fg_color="#FFF6EF")

        self.titulo = ctk.CTkLabel(self, text="Personalização", font=("Century Gothic", 22, "bold"), text_color="#7D0000")
        self.titulo.pack(pady=(45, 15))

        self.texto_apelido = ctk.CTkLabel(self, text="Deseja usar um nome discreto para o acompanhamento?", font=("Century Gothic", 14, "bold"), text_color="#7D0000")
        self.texto_apelido.pack(pady=(20, 5))

        self.opcao_apelido = ctk.CTkOptionMenu(self, values=["Não", "Sim"], width=380, height=42, fg_color="#792929", button_color="#5C1D1D", button_hover_color="#4A1717", text_color="#FFF6EF",
            dropdown_fg_color="#FFF6EF", dropdown_hover_color="#EBD6D0", dropdown_text_color="#493832", corner_radius=10, command=self.verificar_apelido,)
        self.opcao_apelido.pack(pady=5)
        self.opcao_apelido.set("Não")

        self.campo_apelido = None

        self.texto_final = ctk.CTkLabel(self, text="Você poderá consultar e atualizar essas informações depois.", font=("Century Gothic", 12), text_color="#493832")
        self.texto_final.pack(pady=(25, 8))

        self.botao_salvar = ctk.CTkButton(self, text="Salvar acompanhamento", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF", command=self.salvar_comportamento)
        self.botao_salvar.pack(pady=15)

        self.botao_voltar = ctk.CTkButton(self, text="Voltar", fg_color="transparent",  text_color="#7D0000", hover_color="#F2EAE4", command=self.tela_data_inicio)
        self.botao_voltar.pack(pady=5)

    def verificar_apelido(self, escolha):
        """Exibe ou remove o campo de nome discreto."""

        if escolha == "Sim":
            if self.campo_apelido is None:
                self.campo_apelido = ctk.CTkEntry(self, width=380,  height=42, placeholder_text="Nome discreto")
            self.campo_apelido.pack(pady=10, before=self.texto_final)

        else:
            if self.campo_apelido is not None:
                self.campo_apelido.destroy()
                self.campo_apelido = None

# RF02 - Confirmação de registro  ---------------------------------------------------------------------------------------------------------------------
    def salvar_comportamento(self):
        """Salva o acompanhamento no banco de dados."""

        apelido = self.campo_apelido.get().strip() if self.campo_apelido else None

        if self.opcao_apelido.get() == "Sim" and not apelido:
            messagebox.showerror("Erro", "Digite um nome discreto.")
            return

        comportamento = Comportamento(self.usuario_logado[0], self.comportamento_escolhido, self.categoria_escolhida, self.data_inicio_escolhida, apelido)

        try:
            self.banco.cadastrar_comportamento(comportamento)

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))
            return

        messagebox.showinfo("ARI", "Acompanhamento salvo com sucesso!")
        self.tela_menu_principal()

# RF02 - Consulta do acompanhamento  ---------------------------------------------------------------------------------------------------------------------
    def tela_meu_comportamento(self):
        """Apresenta as informações do acompanhamento."""

        self.limpar_tela()
        self.configure(fg_color="#FFF6EF")

        dados = self.banco.consultar_comportamento(self.usuario_logado[0])

        if dados is None:
            messagebox.showinfo("ARI", "Você ainda não possui acompanhamento.")
            self.tela_comportamento()
            return

        self.titulo = ctk.CTkLabel(self, text="Meu acompanhamento", font=("Century Gothic", 22, "bold"), text_color="#7D0000")
        self.titulo.pack(pady=(40, 15))

        apelido = dados[5] if dados[5] else "Não informado"

        self.info_comportamento = ctk.CTkLabel(self,
            text=(
                f"Comportamento: {dados[2]}\n\n"
                f"Categoria: {dados[3]}\n\n"
                f"Data de início: {dados[4]}\n\n"
                f"Nome discreto: {apelido}"), font=("Century Gothic", 14), text_color="#493832", justify="left",)
        self.info_comportamento.pack(pady=20)

        self.botao_editar = ctk.CTkButton(self, text="Editar acompanhamento", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF",
        command=lambda: self.tela_editar_comportamento(dados))
        self.botao_editar.pack(pady=8)

        self.botao_excluir = ctk.CTkButton(self, text="Excluir acompanhamento", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF",
        command=self.excluir_comportamento)
        self.botao_excluir.pack(pady=8)

        self.botao_voltar = ctk.CTkButton(self, text="Voltar ao menu", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4", command=self.tela_menu_principal)
        self.botao_voltar.pack(pady=8)

    # RF02 - Edição do acompanhamento  ---------------------------------------------------------------------------------------------------------------------
    def tela_editar_comportamento(self, dados):
        """Apresenta os campos para edição do acompanhamento."""

        self.limpar_tela()
        self.configure(fg_color="#FFF6EF")

        self.titulo = ctk.CTkLabel(self, text="Editar acompanhamento", font=("Century Gothic", 22, "bold"), text_color="#7D0000")
        self.titulo.pack(pady=30)

        self.editar_nome = ctk.CTkEntry(self, width=380, height=42, placeholder_text="Comportamento")
        self.editar_nome.pack(pady=8)
        self.editar_nome.insert(0, dados[2])

        self.editar_categoria = ctk.CTkEntry(self, width=380, height=42, placeholder_text="Categoria")
        self.editar_categoria.pack(pady=8)
        self.editar_categoria.insert(0, dados[3])

        self.editar_data = ctk.CTkEntry(self, width=380, height=42, placeholder_text="DD/MM/AAAA")
        self.editar_data.pack(pady=8)
        self.editar_data.insert(0, dados[4])

        self.editar_apelido = ctk.CTkEntry(self, width=380, height=42, placeholder_text="Nome discreto")
        self.editar_apelido.pack(pady=8)

        if dados[5]:
            self.editar_apelido.insert(0, dados[5])

        self.botao_salvar_edicao = ctk.CTkButton(self, text="Salvar alterações", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF",
        command=self.salvar_atualizacao_comportamento)
        self.botao_salvar_edicao.pack(pady=15)

        self.botao_voltar = ctk.CTkButton(self, text="Voltar", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4", command=self.tela_meu_comportamento)
        self.botao_voltar.pack(pady=5)

# RF02 - Confirmação da atualização  ---------------------------------------------------------------------------------------------------------------------
    def salvar_atualizacao_comportamento(self):
        """Atualiza as informações do acompanhamento."""

        apelido = self.editar_apelido.get().strip() or None

        comportamento = Comportamento(self.usuario_logado[0], self.editar_nome.get().strip(), self.editar_categoria.get().strip(), self.editar_data.get().strip(), apelido)

        try:
            self.banco.atualizar_comportamento(self.usuario_logado[0], comportamento)

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))
            return

        messagebox.showinfo("ARI", "Acompanhamento atualizado com sucesso!")
        self.tela_meu_comportamento()

# RF02 - Exclusão do comportamento ---------------------------------------------------------------------------------------------------------------------
    def excluir_comportamento(self):
        """Confirma e exclui o acompanhamento."""

        confirmar = messagebox.askyesno("Confirmar exclusão", "Deseja realmente excluir este acompanhamento?")

        if not confirmar:
            return

        try:
            self.banco.deletar_comportamento(self.usuario_logado[0])

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))
            return

        messagebox.showinfo("ARI", "Acompanhamento excluído com sucesso!")
        self.tela_comportamento()

# RF04 - Tela do Menu inicial  ---------------------------------------------------------------------------------------------------------------------
    def tela_menu_principal(self):
        """Apresenta o menu principal do ARI."""

        self.limpar_tela()
        self.configure(fg_color="#FFF6EF")

        self.titulo = ctk.CTkLabel(self, text="ARI", font=("Century Gothic", 30, "bold"), text_color="#7D0000")
        self.titulo.pack(pady=(30, 5))

        self.boas_vindas = ctk.CTkLabel(self, text=f"Bem-vindo(a), {self.usuario_logado[1]}!", font=("Century Gothic", 14), text_color="#493832")
        self.boas_vindas.pack(pady=5)

        acompanhamento = self.banco.consultar_comportamento(self.usuario_logado[0])

        if acompanhamento:
            nome = acompanhamento[5] if acompanhamento[5] else acompanhamento[2]
            texto_status = f"Acompanhamento ativo: {nome}"
        else:
            texto_status = "Você ainda não possui um acompanhamento."

        self.status_acompanhamento = ctk.CTkLabel(self, text=texto_status, font=("Century Gothic", 13, "bold"), text_color="#792929")
        self.status_acompanhamento.pack(pady=(10, 15))

        self.botao_registro = ctk.CTkButton(self, text="Registro diário", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF",
        command=self.abrir_registro_diario)
        self.botao_registro.pack(pady=7)

        self.botao_historico = ctk.CTkButton(self, text="Histórico", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF",
        command=self.abrir_historico)
        self.botao_historico.pack(pady=7)

        self.botao_acompanhamento = ctk.CTkButton(self, text="Meu acompanhamento", width=380, height=42, fg_color="#792929", hover_color="#6B2424",text_color="#FFFFFF",
        command=self.tela_meu_comportamento)
        self.botao_acompanhamento.pack(pady=7)

        self.botao_atividades = ctk.CTkButton(self, text="Atividades cognitivas", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF",
        command=self.abrir_atividades_cognitivas)
        self.botao_atividades.pack(pady=7)

        self.botao_perfil = ctk.CTkButton(self, text="Meu perfil", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF", command=self.abrir_meu_perfil)
        self.botao_perfil.pack(pady=7)

        self.botao_sair = ctk.CTkButton(self, text="Sair da conta", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4",
        command=self.sair_da_conta)
        self.botao_sair.pack(pady=10)

# RF03 - No menu, consultar Tela do registro diário  ---------------------------------------------------------------------------------------------------------------------
    def abrir_registro_diario(self):
        """Abre a tela de registro diário."""

        from telas.tela_registro import TelaRegistro

        print("Botão Registro diário acionado!")

        TelaRegistro(self).tela_registro_diario()

# RF03 - No menu, consultar histórico de registros  (falta implementação, porém o histórico é registrado)---------------------------------------------------------------------------------------------------------------------
    def abrir_historico(self):
        """Abre o histórico de registros."""

        from telas.tela_registro import TelaRegistro
        
        TelaRegistro(self).tela_historico()

# No menu - consultar Tela de atividades cognitiva (requisito futuro) ---------------------------------------------------------------------------------------------------------------------
    def abrir_atividades_cognitivas(self):
        """Apresenta a seção de atividades cognitivas."""

        messagebox.showinfo("ARI", "As atividades cognitivas ainda estão em desenvolvimento.")

    def abrir_meu_perfil(self):
        """Apresenta os dados do usuário logado."""

        messagebox.showinfo("Meu perfil", f"Nome: {self.usuario_logado[1]}\n" , f"E-mail: {self.usuario_logado[2]}")

    def sair_da_conta(self):
        """Encerra a sessão do usuário."""

        self.usuario_logado = None
        self.tela_inicial()


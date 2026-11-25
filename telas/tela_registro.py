# telas/tela_registro.py
# Este arquivo define a interface do registro diário e histórico

from datetime import datetime
import customtkinter as ctk
from tkinter import messagebox

from modelos.registros import Registro

class TelaRegistro:
    """Classe responsável pelas telas de registro diário e histórico."""

    def __init__(self, app):
        self.app = app

    def tela_registro_diario(self):
        """Apresenta o formulário de registro diário."""

        self.app.limpar_tela()
        self.app.configure(fg_color="#FFF6EF")

        self.titulo = ctk.CTkLabel(self.app, text="Registro diário", font=("Century Gothic", 22, "bold"), text_color="#7D0000" )
        self.titulo.pack(pady=(40, 15))

        self.texto_data = ctk.CTkLabel(self.app, text="Data do registro", font=("Century Gothic", 13, "bold"), text_color="#493832")
        self.texto_data.pack(pady=5)

        self.entrada_data = ctk.CTkEntry(self.app, width=380, height=42, placeholder_text="DD/MM/AAAA")
        self.entrada_data.pack(pady=8)
        self.entrada_data.insert(0, datetime.now().strftime("%d/%m/%Y"))

        self.texto_descricao = ctk.CTkLabel(self.app, text="Como foi o seu dia?", font=("Century Gothic", 13, "bold"), text_color="#493832")
        self.texto_descricao.pack(pady=(15, 5))

        self.entrada_descricao = ctk.CTkTextbox(self.app, width=380, height=180, font=("Century Gothic", 13), corner_radius=10)
        self.entrada_descricao.pack(pady=8)

        self.botao_salvar = ctk.CTkButton(self.app, text="Salvar registro", width=380, height=42, fg_color="#792929", hover_color="#6B2424", text_color="#FFFFFF", 
        command=self.salvar_registro)
        self.botao_salvar.pack(pady=12)

        self.botao_voltar = ctk.CTkButton(self.app, text="Voltar", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4", command=self.app.tela_menu_principal)
        self.botao_voltar.pack(pady=5)

    def salvar_registro(self):
        """Valida e salva o registro no banco de dados."""

        registro = Registro(self.app.usuario_logado[0], self.entrada_data.get().strip(), self.entrada_descricao.get("1.0", "end").strip() )

        try:
            self.app.banco.cadastrar_registro(registro)

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))
            return

        messagebox.showinfo("ARI", "Registro salvo com sucesso!")
        self.app.tela_menu_principal()

    def tela_historico(self):
        """Apresenta os registros anteriores do usuário."""

        self.app.limpar_tela()
        self.app.configure(fg_color="#FFF6EF")

        self.titulo = ctk.CTkLabel(self.app, text="Histórico", font=("Century Gothic", 22, "bold"), text_color="#7D0000" )
        self.titulo.pack(pady=(30, 15))

        registros = self.app.banco.listar_registros(self.app.usuario_logado[0])

        if not registros:
            ctk.CTkLabel(self.app, text="Nenhum registro encontrado.", font=("Century Gothic", 13), text_color="#493832").pack(pady=20)

        else:
            self.lista_registros = ctk.CTkScrollableFrame(self.app, width=500, height=400, fg_color="#FFFFFF")
            self.lista_registros.pack(padx=20, pady=10)

            for registro in registros:

                quadro = ctk.CTkFrame(self.lista_registros, fg_color="#F5E8E1", corner_radius=10 )
                quadro.pack(fill="x", padx=5, pady=7)

                ctk.CTkLabel(quadro, text=f"Data: {registro[2]}", font=("Century Gothic", 13, "bold"), text_color="#7D0000").pack(anchor="w", padx=12, pady=(10, 5))

                ctk.CTkLabel(quadro, text=registro[3], font=("Century Gothic", 12), text_color="#493832", wraplength=440, justify="left").pack(anchor="w", padx=12, pady=5)

                ctk.CTkButton(quadro, text="Excluir registro", width=150, height=30, fg_color="#792929", hover_color="#6B2424", 
                command=lambda id_registro=registro[0]: self.excluir_registro(id_registro) ).pack(anchor="e", padx=10, pady=8)

        self.botao_voltar = ctk.CTkButton(self.app, text="Voltar ao menu", fg_color="transparent", text_color="#7D0000", hover_color="#F2EAE4", command=self.app.tela_menu_principal )
        self.botao_voltar.pack(pady=10)

    def excluir_registro(self, id_registro):
        """Confirma e exclui um registro."""

        confirmar = messagebox.askyesno("Confirmar exclusão", "Deseja excluir este registro?")

        if not confirmar:
            return
            
        self.app.banco.deletar_registro(id_registro, self.app.usuario_logado[0] )

        messagebox.showinfo("ARI", "Registro excluído com sucesso!")
        self.tela_historico()

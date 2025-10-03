import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
class CredencialUtils:

    def __init__(self):
        self.user = None
        self.senha = None
        self.file_path = None
        self.path_icon =  "Main/Icons/tse-icon.png" #Define o Icone da janela principal
        self.icon_user = ctk.CTkImage(Image.open("Main/Icons/icon-user.png"),size=(20,20)) #Define o Ícone do usuario
        self.icon_password = ctk.CTkImage(Image.open("Main/Icons/icon-password.png"),size=(20,20)) #Define o Ícone da senha
        self.icon_past = ctk.CTkImage(Image.open("Main/Icons/icon-pasta.png"),size=(20,20)) #Define o Ícone da seleção do arquivo
        self.main_frame_bg_color = "#4E6F9C" #Define a cor do frame(janela) principal
        self.frame_color = "#4E6F9C" #Define a cor do frame(janela) filhos
        self.root = tk.Tk() #Cria a janela principal da Interface
        self.root.title("Credenciais para logar no Sei") #Define o nome da janela da Interface
        self.root.geometry("500x250") #Define o Tamanho da Interface
        self.root.resizable(False, False) #Define que a janela não é redimensionavel
        self.root.config(background=self.main_frame_bg_color) #Define a cor de fundo da Interface
        self.root.iconphoto(False, tk.PhotoImage(file=self.path_icon)) #Coloca o ícone na janela da Interface
        self.entry_width = 220 #Serve para deixar tudo alinhado

        #Frame Principal
        self.frame = ctk.CTkFrame(master=self.root, corner_radius=10, bg_color=self.main_frame_bg_color, fg_color=self.frame_color) #Configura o frame principal
        self.frame.pack(pady=1, padx=1, fill="x") #Esse pack serve para mostrar seu frame configurado, pady = Espaçamento externo vertical, padx = Espaçamento externo Horizontal, fill "x" = preenchimento Horizontal

        #Frame para o usuário
        self.frame_user = ctk.CTkFrame(master=self.frame, corner_radius=10, fg_color="transparent")
        self.frame_user.pack(pady=8, padx=10, fill="x")
        
        self.label_icon_user = ctk.CTkLabel(master=self.frame_user, image=self.icon_user, text="")
        self.label_icon_user.pack(side="left", padx=7, pady=5)

        self.campo_usuario = ctk.CTkEntry(master=self.frame_user, placeholder_text="Digite seu usuário", corner_radius=10, width=self.entry_width)
        self.campo_usuario.pack(side="left", fill="x", expand=True, padx=5, pady=2)

        #Frame para a senha
        self.frame_password = ctk.CTkFrame(master=self.frame, corner_radius=10, fg_color="transparent")
        self.frame_password.pack(pady=8, padx=10, fill="x")

        self.label_icon_password = ctk.CTkLabel(master=self.frame_password, image=self.icon_password, text="")
        self.label_icon_password.pack(side="left", padx=7, pady=5)

        self.campo_senha = ctk.CTkEntry(master=self.frame_password, placeholder_text="Digite sua senha", corner_radius=10, width=self.entry_width, show="*")
        self.campo_senha.pack(side="left", fill="x", expand=True, padx=5, pady=2)

        #Frame para seleção de arquivo
        self.frame_file = ctk.CTkFrame(master=self.frame, corner_radius=10, fg_color="transparent")
        self.frame_file.pack(padx=(10,10), pady=(8,5), fill="x")

        self.label_icon_pasta = ctk.CTkLabel(master=self.frame_file, image=self.icon_past, text="")
        self.label_icon_pasta.pack(side="left", padx=7, pady=2)

        self.botao_arquivo = ctk.CTkButton(master=self.frame_file, text="Selecionar Arquivo", width=15, font=(ctk.CTkFont(family="Segoe UI", size=10, weight="bold")), command=self.selecionar_arquivo, anchor='center')
        self.botao_arquivo.pack(side="left", padx=5, pady=2)

        self.campo_arquivo = ctk.CTkEntry(master=self.frame_file, placeholder_text="", border_width=0, width=self.entry_width, fg_color=self.frame_color)
        self.campo_arquivo.pack(side="right", fill="x", expand=True, padx=5, pady=2)

        #Frame para botão de confirmar
        self.frame_confirmed = ctk.CTkFrame(master=self.frame, corner_radius=10, fg_color="transparent")
        self.frame_confirmed.pack(padx=10, pady=(9,0), fill="x")

        self.botao_confirmar = ctk.CTkButton(master=self.frame_confirmed, text="Confirmar", width=200, height=10, border_width=0, font=(ctk.CTkFont(family="Segoe UI", size=18)), anchor='center', command=self.obter_credenciais)
        self.botao_confirmar.pack(padx=5, pady=(30,3), ipady=(2))


        self.root.mainloop()  #Executa sua interface


    def obter_credenciais(self):
        self.user = self.campo_usuario.get() #Pega o valor do campo_usuario da interface e define no atributo user da classe
        self.senha = self.campo_senha.get() #Pega o valor do campo_senha da interface e define no atributo senha da classe
        self.file_path = self.file_path #Configura o caminho do arquivo no atributo da classe

        if self.validar_campos() == True:
            self.root.destroy() #Fecha a janela
        else:
            return

    def selecionar_arquivo(self):
        while True: #Serve para deixar o loop infinito até o usuario escolher um arquivo
            caminho_arquivo = askopenfilename(title="Selecione um arquivo") #Abre a janela para o usuario selecionar o arquivo
            
            if not caminho_arquivo: #Se o caminho_arquivo for vazio
                resposta = messagebox.askretrycancel("Erro", "Nenhum arquivo foi selecionado! Tentar novamente?") #Abre um janela perguntando se o usuario que tentar escolher novamente o arquivo
                if not resposta: #Se a resposta for que ele não quer escolher o arquivo
                    return print("Arquivo não selecionado!") #Fecha a interface.

            else:
                nome_arquivo = os.path.basename(caminho_arquivo) #Define o nome do arquivo que ele selecionou
                self.campo_arquivo.delete(0, "end") #Limpa o campo de entrada do nome do arquivo na interface
                self.campo_arquivo.insert(0, nome_arquivo) #Insere o nome do novo/atual arquivo selecionado
                self.campo_arquivo.configure(text_color="#F0F8FF")  #Define a cor da font no campo de entrada do arquivo
                self.file_path = caminho_arquivo #Define o caminho de onde está esse arquivo
                return caminho_arquivo    
            
    def validar_campos(self):
        campos_vazios = []
        if not self.user:
            campos_vazios.append("Usuário")
        if not self.senha:
            campos_vazios.append("Senha")
        if not self.file_path:
            campos_vazios.append("Arquivo")

        if campos_vazios:
            messagebox.showwarning("Atenção", f"Preencha os seguintes campos: {', '.join(campos_vazios)}")
            return False
        else:
            return True
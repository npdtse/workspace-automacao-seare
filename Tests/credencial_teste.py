import tkinter as tk
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import os
from tkinter.filedialog import askopenfilename

class CredencialUtilsV2:

    def __init__(self):
        self.user = None
        self.senha = None
        self.file_path = None
        self.path_icon = "Icons/tse-icon.png"
        self.icon_user = ctk.CTkImage(Image.open("Icons/icon-user.png"),size=(20,20))
        self.icon_password = ctk.CTkImage(Image.open("Icons/icon-password.png"),size=(20,20))
        self.icon_past = ctk.CTkImage(Image.open("Icons/icon-pasta.png"),size=(20,20))
        self.main_frame_bg_color = "#4E6F9C"
        self.frame_color = "#4E6F9C"
        self.root = tk.Tk()
        self.root.title = ("Credenciais para logar no Sei")
        self.root.geometry("500x250")
        self.root.resizable(False, False)
        self.root.config(background=self.main_frame_bg_color)
        self.root.iconphoto(False, tk.PhotoImage(file=self.path_icon))
        self.entry_width = 220 #Serve para deixar tudo alinhado

        #Frame Principal
        self.frame = ctk.CTkFrame(master=self.root, corner_radius=10, bg_color=self.main_frame_bg_color, fg_color=self.frame_color)
        self.frame.pack(pady=1, padx=1, fill="x")

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

        self.botao_confirmar = ctk.CTkButton(master=self.frame_confirmed, text="Confirmar", width=200, height=10, font=(ctk.CTkFont(family="Segoe UI", size=18)), anchor='center', command=self.obter_credenciais)
        self.botao_confirmar.pack(padx=5, pady=(30,3), ipady=(2))

        self.root.mainloop()  


    def obter_credenciais(self):
        self.user = self.campo_usuario.get()
        self.senha = self.campo_senha.get()
        self.file_path = self.file_path
        print(self.file_path)

        if self.user and self.senha and self.file_path:
            self.root.destroy()
        else:
            messagebox.showwarning("Atenção", "Preencha o login e a senha")    

    def selecionar_arquivo(self):
        while True:  
            caminho_arquivo = askopenfilename(title="Selecione um arquivo")
            
            if not caminho_arquivo:
                resposta = messagebox.askretrycancel("Erro", "Nenhum arquivo foi selecionado! Tentar novamente?")
                if not resposta:
                    return self.root.destroy()

            else:
                nome_arquivo = os.path.basename(caminho_arquivo)
                self.campo_arquivo.delete(0, "end")
                self.campo_arquivo.insert(0, nome_arquivo)
                self.campo_arquivo.configure(text_color="#F0F8FF")
                self.file_path = caminho_arquivo  
                return caminho_arquivo    


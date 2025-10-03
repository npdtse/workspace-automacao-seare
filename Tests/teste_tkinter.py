import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import os
from tkinter.filedialog import askopenfile, askopenfilename
from PIL import Image

def selecionar_arquivo():
    while True:  
        caminho_arquivo = askopenfilename(title="Selecione um arquivo")
        
        if not caminho_arquivo:
            resposta = messagebox.askretrycancel("Erro", "Nenhum arquivo foi selecionado! Tentar novamente?")
            if not resposta:
                return root.destroy()

        else:
            nome_arquivo = os.path.basename(caminho_arquivo)
            campo_arquivo.delete(0, "end")
            campo_arquivo.insert(0, nome_arquivo)
            campo_arquivo.configure(text_color="#F0F8FF")  
            return caminho_arquivo  

#Cores
#5f9ea0
#f5fffb
#FFC300 Cor amarela do TSE
#4E6F9C Cor azul do TSE

main_frame_bg_color = "#4E6F9C"
frame_color = "#4E6F9C"

#Configuração Inicial da Interface
root = tk.Tk()
path_fav_icon = 'Icons/tse-icon.png'
root.title("Credenciais para logar no SEI")
root.geometry("500x250")
root.resizable(False, False)
root.config(background=main_frame_bg_color)
root.iconphoto(False, tk.PhotoImage(file=path_fav_icon))
icon_user = ctk.CTkImage(Image.open("Icons/icon-user.png"),size=(20,20))
icon_password = ctk.CTkImage(Image.open("Icons/cadeado.png"),size=(20,20))
icon_pasta = ctk.CTkImage(Image.open("Icons/icon-pasta.png"),size=(20,20))

entry_width = 220



#Frame Principal
frame = ctk.CTkFrame(master=root, corner_radius=10, bg_color=main_frame_bg_color, fg_color=frame_color)
frame.pack(pady=1, padx=1, fill="x")

#Frame para o usuário
frame_user = ctk.CTkFrame(master=frame, corner_radius=10, fg_color="transparent")
frame_user.pack(pady=8, padx=10, fill="x")

label_icon_user = ctk.CTkLabel(master=frame_user, image=icon_user, text="")
label_icon_user.pack(side="left", padx=7, pady=5)

campo_usuario = ctk.CTkEntry(master=frame_user, placeholder_text="Digite seu usuário", corner_radius=10, width=entry_width)
campo_usuario.pack(side="left", fill="x", expand=True, padx=5, pady=2)

#Frame para a senha
frame_password = ctk.CTkFrame(master=frame, corner_radius=10, fg_color="transparent")
frame_password.pack(pady=8, padx=10, fill="x")

label_icon_password = ctk.CTkLabel(master=frame_password, image=icon_password, text="")
label_icon_password.pack(side="left", padx=7, pady=5)

campo_senha = ctk.CTkEntry(master=frame_password, placeholder_text="Digite sua senha",corner_radius=10, width=entry_width)
campo_senha.pack(side="left", fill="x", expand=True, padx=5, pady=2)

#Frame para seleção de arquivo
frame_file = ctk.CTkFrame(master=frame, corner_radius=10, fg_color="transparent")
frame_file.pack(padx=(10,10), pady=(8,5), fill="x")

label_icon_pasta = ctk.CTkLabel(master=frame_file, image=icon_pasta, text="")
label_icon_pasta.pack(side="left", padx=7, pady=2)

botao_arquivo = ctk.CTkButton(master=frame_file, text="Selecionar Arquivo", width=15,font=(ctk.CTkFont(family="Segoe UI", size=10, weight="bold")), command=selecionar_arquivo, anchor='center')
botao_arquivo.pack(side="left", padx=5, pady=2)

campo_arquivo = ctk.CTkEntry(master=frame_file, placeholder_text="", border_width=0, width=entry_width, fg_color=frame_color)
campo_arquivo.pack(side="right", fill="x", expand=True, padx=5, pady=2)

#Frame para o botão de confirmar
frame_confirmed = ctk.CTkFrame(master=frame, corner_radius=10, fg_color="transparent")
frame_confirmed.pack(padx=10, pady=(9,0), fill="x")

botão_confirmar = ctk.CTkButton(master=frame_confirmed, text="Confirmar", width=200, height=10, font=(ctk.CTkFont(family="Segoe UI", size=18)), anchor='center')
botão_confirmar.pack(padx=5, pady=(30,3), ipady=(2))

root.mainloop()
import time
import os
import sys
import logging
from Main.Utils.excel_utils import ExcelUtils
from Main.Utils.sei_automation_utils import SEIAutomation
from Main.Utils.credencial_utils import CredencialUtils
from tkinter import messagebox

file_handler = logging.FileHandler("Log/aplicação_seare.log", "a")
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(asctime)s - %(message)s",
    handlers=[file_handler, stream_handler]
)

class AplicacaoSeare:

    def __init__(self):
        self.credenciais = CredencialUtils() #Cria a Instância da classe CredenciaUtils()

        if getattr(sys, 'frozen', False):
            BASE_DIR = os.path.dirname(sys.executable)
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))    
        
        self.site_url = 'https://sip.tse.jus.br/sip/login.php?sigla_orgao_sistema=TSE&sigla_sistema=SEI' #Define o link do site SEI
        self.caminho_excel = self.credenciais.file_path #Pega o caminho do arquivo onde vai pegar os numeros SEI
        self.caminho_excel_historico = os.path.join(BASE_DIR, "Main", "Dados", "Historico Varredura SEI.xlsx") #Pega o caminho do arquivo da planilha onde vai ser salvo os novos dados
        self.excel_manager = ExcelUtils(self.caminho_excel) #Cria a Instância da classe ExcelUtils
        self.sei_automation = SEIAutomation(self.site_url, self.credenciais.user, self.credenciais.senha) #Cria a Instância da classe SEIAutomation

    def executar(self):
        if not self.validar_credenciais():
            return

        tempo_inicial = time.time() #Inicia o tempo da aplicação
        nsei_list = self.excel_manager.extrair_nsei() #Executa o método de extrair os números SEI da planilha
        self.excel_manager.salvar_nsei_na_planilha(nsei_list, self.caminho_excel_historico) #Salva os números SEI extraido na planilha Histórico

        if self.sei_automation.logar_sei(): #Executa o método de logar no SEI, se for bem-sucedido executa os procedimentos abaixo
            titulos_list = self.sei_automation.buscar_titulos(nsei_list) #Executa o método de buscar títulos no sei
            self.excel_manager.atualizar_titulos(self.caminho_excel_historico,titulos_list) #Executa o método de atualizar os títulos na planilha Histórico

            tempo_final = time.time() #Finaliza o tempo da aplicação
            self.exibir_tempo_execucao(tempo_inicial, tempo_final) #Função para exibir o tempo total da aplicação. 

    def validar_credenciais(self):
        campos_vazios = []
        if not self.credenciais.user:
            campos_vazios.append("Usuário")
        if not self.credenciais.senha:
            campos_vazios.append("Senha")
        if not self.credenciais.file_path:
            campos_vazios.append("Caminho do arquivo")

        if campos_vazios:
            messagebox.showwarning("Atenção", f"É necessário todos os campos da Interface: {', '.join(campos_vazios)}")
            return False

        return True        

    @staticmethod
    def exibir_tempo_execucao(tempo_inicial, tempo_final):
        tempo_total = tempo_final - tempo_inicial

        logging.info(f"Tempo de execução: {int(tempo_total // 60)} min {int(tempo_total % 60)} seg")         


#Cada arquivo em python tem uma variavel especial chamada __name__, se o arquivo for executado diretamente pela classe AplicacaoSeare essa variavel especial
#terá o valor "__main__". Logo se essa condição for verdadeira ela executa os procedimentos abaixo.
if __name__ == "__main__": 
    app = AplicacaoSeare() #Cria a Instância da classe AplicacaoSeare
    app.executar() #Executa o método de iniciar a aplicação.
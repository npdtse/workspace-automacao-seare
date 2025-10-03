from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import time
import logging
import sys

file_handler = logging.FileHandler("Log/seiAutomation_utils.log", "a")
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(asctime)s - %(message)s",
    handlers=[file_handler, stream_handler]
)

class SEIAutomation:

    #Construtor da Classe
    def __init__(self, site_url, usuario, senha):
        self.site_url = site_url
        self.usuario = usuario
        self.senha = senha
        self.navegador = None

    def logar_sei(self):
        logging.info("Iniciando o Login no SEI")
        # self.navegador = webdriver.Chrome() #Define o navegador onde iremos fazer a varredura
        self.navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #Define o navegador onde iremos fazer a varredura
        self.navegador.get(self.site_url)  #Define a página inicial ao abrir o navegador
        self.navegador.maximize_window() #Abre o navegador em tela cheia

        
        time.sleep(2)
        try:
            logging.info("------------------------------")
            logging.info(self.navegador.current_url)
            logging.info("------------------------------")
            logging.info("Aguardando o campo de texto do usuario aparecer")
            WebDriverWait(self.navegador, 5).until(EC.presence_of_element_located((By.ID, "txtUsuario")))
            self.navegador.find_element(By.ID, "txtUsuario").send_keys(self.usuario) #Encontra o elemento onde vai ser colocado a credencial do usuario

            logging.info("Aguardando o campo de texto de senha aparecer")
            WebDriverWait(self.navegador, 5).until(EC.presence_of_element_located((By.ID, "pwdSenha")))
            self.navegador.find_element(By.ID, "pwdSenha").send_keys(self.senha) #Encontra o elemento onde vai ser colocado a credencial da senha

            logging.info("Aguardando o botão de acessar aparecer")
            WebDriverWait(self.navegador, 5).until(EC.element_to_be_clickable((By.ID, "sbmAcessar")))
            self.navegador.find_element(By.ID, "sbmAcessar").click() #Faz a ação de click para poder acessar o SEI logado

            time.sleep(5)

            # WebDriverWait(self.navegador, 30).until(EC.url_changes(self.navegador.current_url))

            WebDriverWait(self.navegador, 30).until(EC.presence_of_element_located((By.ID, "infraMenu")))
            if("controlador.php?") in self.navegador.current_url: #Verifica se na url contém a string definida, se tiver quer dizer que o login foi bem-sucedido
                logging.info("Login bem-sucedido!")
                return True
    
        except Exception as e:
            logging.info("------------------------------")
            logging.info(self.navegador.current_url)
            logging.info("------------------------------")
            logging.error("Erro ao fazer login: %s", str(e), exc_info=True)
            return False
        
    def buscar_titulos(self, nsei_list):
        logging.info("Iniciando busca de Títulos.")
        lista_titulo_documento = []
        contador = 0

        try:
            for nsei in nsei_list:
                campo_pesquisa = self.navegador.find_element(By.ID, "txtPesquisaRapida") #Encontra o elemento de pesquisa rapida para colocar o numero SEI atual
                campo_pesquisa.send_keys(nsei) #Coloca o numero SEI atual no campo de pesquisa
                campo_pesquisa.send_keys(Keys.RETURN) #Faz a ação de aperta ENTER para fazer a pesquisa do numero SEI
                time.sleep(2)

                self._alternar_para_iframe()

                    # try:
                    #     iframe = self.navegador.find_element(By.CSS_SELECTOR, "#divInfraAreaGlobal #divInfraAreaTela #divInfraAreaTelaD #divIframeArvore #ifrArvore")
                    #     self.navegador.switch_to.frame(iframe) #Alterna o navegador para o iframe.
                    # except: 
                    #     iframe = "Processo Restrito"    

                #Executa o javascript no navegador para buscar o titulo do ultimo documento assinado.
                titulo = self._obter_titulo_documento()
                # if self.navegador.execute_script(self.get_title_script()) == None:
                #     titulo = "Processo Restrito"
                # else:
                #     titulo = self.navegador.execute_script(self.get_title_script())
                
                lista_titulo_documento.append(titulo) #Salva esse titulo na lista
                contador = contador + 1
                logging.info(f"Contador: {contador}: {nsei} : {titulo}")
                self.navegador.switch_to.default_content() #Retorna para o contexto principal do navegador
        except Exception as e:
            logging.error(f"Erro ao buscar título para NSEI {nsei}: {str(e)}", exc_info=True)
            sys.exit(1)

        logging.info("Busca de Títulos concluída.")
        return lista_titulo_documento   
    


    def get_title_script(self):
        return str("""
                    let iframeDoc = document;
                    
                    let docTitles = iframeDoc.querySelectorAll("body #container #content #frmArvore #divArvore div.infraArvore a.infraArvoreNo span");

                    let signedDocTitles = Array.from(docTitles).filter(title => {
                        let style = title.getAttribute("style");
                        let id = title.getAttribute("id");
                        return !(style && style.includes("color: rgb(204, 158, 128)")) && !(id && id.includes("PASTA"));
                    }).map(title => title.textContent); 

                    let lastSignedDocTitle = signedDocTitles[signedDocTitles.length - 1];
                    
                    return lastSignedDocTitle;
                """)
    
    def _alternar_para_iframe(self):
        try:
            iframe = self.navegador.find_element(
                By.CSS_SELECTOR, 
                "#divInfraAreaGlobal #divInfraAreaTela #divInfraAreaTelaD #divIframeArvore #ifrArvore"
            )
            self.navegador.switch_to.frame(iframe)
        except Exception:
            logging.warning("Iframe não encontrado. Processo pode ser restrito.")    

    def _obter_titulo_documento(self):
        titulo = self.navegador.execute_script(self.get_title_script())
        return titulo if titulo else "Processo Restrito"        

        
        
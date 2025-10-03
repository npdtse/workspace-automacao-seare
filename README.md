
# 📘 Manual de Instalação do Sistema de Varredura no SEI


Este manual descreve o processo de instalação do sistema de varredura no SEI na máquina do usuário.
---

## ⚙️ Passo a Passo da Instalação

### 1. Enviar o arquivo compactado
Envie o arquivo compactado que contém a pasta do sistema de varredura para o computador do usuário.

### 2. Descompactar o arquivo
Descompacte o arquivo enviado. Recomendo extrair o conteúdo em uma pasta de fácil acesso, como por exemplo:
- `C:\Users\$NOME_USUARIO$\OneDrive - TRIBUNAL SUPERIOR ELEITORAL\Documentos`;
- Ou outro local de sua preferência.

### 3. Executar o *install.bat*
    1. Abra o Prompt de Comando (CMD);
    2. Dentro do CMD, navegue até a pasta onde está localizado o arquivo install.bat;
    3. Digite install.bat e pressione a tecla Enter;
    4. Aguarde o processo ser concluído e feche o CMD.

### 4. Executar o *bibliotecas.bat*
    1. Abra o CMD, navegue novamente até a pasta do sistema;
    2. Digite bibliotecas.bat e pressione Enter;
    3. Aguarde o processo ser concluído.

### 5. Iniciar o Sistema
    1. Localize o executável aplicação_seare.exe que fica dentro da pasta "workspace-projeto-seare". Caso o executável não seja encontrado nessa pasta pule para o passo 6;
    2. Inicie o sistema de varredura.

### 6. Gerar executável manualmente
    1. Verifique se na pasta "workspace-projeto-seare" existem as pastas build e dist;
    2. Se existirem, verificar se o executável se encontra dentro da pasta dist;
      2.1. Se o executável for encontrado na pasta dist, mova ele para a pasta "workspace-projeto-seare";
      2.2. Se não for encontrado, apague as pastas dist e build e o arquivo "aplicação_seare.spec"
    3. Abra o CMD, navegue novamente até a pasta "workspace-projeto-seare";
    4. Execute o seguinte comando "Pyinstaller --onefile --windowed aplicação_seare.py" (sem aspas);
    5. Pegue o executável que foi criado na pasta dist e mova para a pasta "workspace-projeto-seare";
    6. Inicie o sistema.
    
    


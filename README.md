# EasyAutomation

## Descrição

**EasyAutomation** é um script de automação desenvolvido em Python para automatizar o cadastro de usuários em plataformas de gerenciamento e manutenção de redes, sistemas e infraestrutura.

Este projeto foi criado para facilitar a inserção de múltiplos usuários em sistemas como SparkEasy, UNM, AMS e Dude, reduzindo o tempo gasto com tarefas repetitivas. Utilizando uma planilha com os dados de cada usuário, o script realiza o preenchimento automático dos campos de cadastro.

## Tecnologias Utilizadas

- **[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)**: Para controlar o mouse e o teclado, simulando as interações com a interface gráfica.
- **[Pandas](https://pandas.pydata.org/)**: Para ler e iterar sobre os dados da planilha que contém as informações dos usuários.
- **[OpenCV](https://opencv.org/)**: Para realizar a identificação de erros na tela e auxiliar no tratamento de exceções durante o processo de cadastro.

## Funcionalidades

1. **Automação de Cadastro**: O script lê uma planilha Excel com os dados dos usuários, incluindo nome, login e senha. Para cada linha da planilha:
   - O PyAutoGUI move o cursor até as coordenadas predefinidas e preenche os campos de cadastro.
   - As informações de login, nome completo e senha são inseridas automaticamente.
   
2. **Tratamento de Erros**: Caso ocorra algum erro durante o processo de cadastro, o OpenCV localiza visualmente o erro na tela, e o nome do usuário que causou o erro é registrado para tratamento manual posterior.

## Instruções de Uso

1. Clone o repositório para a sua máquina:
   ```bash
   git clone https://github.com/seuusuario/easyautomation.git
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

3. Prepare uma planilha Excel (.xlsx) para cada plataforma contendo os seguintes campos:

- LOGIN: Nome de login do usuário.
- NOME: Nome completo do usuário.
- SENHA: Senha para o cadastro.
- EMAIL: Email para cadastro.
- LOCAL: Setor do usuário.

4. Execute o script Python:
    ```bash
    python app.py
    ```

5. Siga as instruções exibidas no menu para escolher a plataforma em que deseja realizar o cadastro (SparkEasy, AMS, NetNumen, Dude).

## Importante
Este script foi configurado com coordenadas de tela específicas que podem variar de acordo com a resolução do seu monitor. Se as coordenadas atuais não funcionarem para você:

- Localize os pontos onde o cursor deve clicar em sua tela.
- Modifique as coordenadas diretamente no código Python (funções de PyAutoGUI).

## Atenção
- Resoluções de Tela: O script depende da precisão das coordenadas, que variam conforme a resolução do monitor. Certifique-se de ajustar as coordenadas conforme a sua tela.
- Erros de Cadastro: Caso um usuário já esteja cadastrado ou ocorra outro erro, o OpenCV identificará o problema e armazenará o nome do usuário com erro para que você possa tratá-lo posteriormente.

## Contribuições
Fique à vontade para abrir issues ou enviar pull requests. A colaboração é bem-vinda!

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.
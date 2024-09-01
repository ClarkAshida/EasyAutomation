import pyautogui
import pandas as pd
from time import sleep

#Interromper a execução do programa ao arrastar o mouse para o lado superior esquerdo da tela.
pyautogui.FailSafeException

def sparkEasy():

    #Lê a planilha Excel
    df = pd.read_excel('assets/usuarios1.xlsx')
    #df = pd.read_excel('assets/usuarios_testes.xlsx')

    #Cria uma lista para armazenar os usuários já cadastrados
    usuarios_cadastrados = []

    #Loop para cada linha da planilha
    for index, row in df.iterrows():
        username = row['LOGIN']
        fullname = row['NOME']
        password = row['SENHA']
        confirmPassword = row['CONFSENHA']
        print(username, fullname, password, confirmPassword)

        #Botão de adicionar user
        pyautogui.click(316,168)
        #Aguarda 2 segundos para a tela carregar
        sleep(2)
        #Botão de adicionar login
        pyautogui.click(774,196)
        pyautogui.write(username)
        #Botão de adicionar nome
        pyautogui.click(792,227)
        pyautogui.write(fullname)
        #Botão de adicionar senha
        pyautogui.click(794,256)
        pyautogui.write(password)
        #Botão de adicionar confirmar senha
        pyautogui.click(796,287)
        pyautogui.write(confirmPassword)
        #Aperta botão 'next'
        pyautogui.click(844,569)
        sleep(2)

        #Verifica se o erro de 'usuário já está cadastrado' apareceu
        try:
            local = pyautogui.locateOnScreen('assets/botão_erro.png', confidence=0.9)
            #Armazenar o nome do usuário já cadastrado em uma lista
            usuarios_cadastrados.append(username)
            #Clica no botão de 'OK' para sair do erro
            pyautogui.click(local)
            #Clica em 'Cancelar'
            pyautogui.click()
            sleep(2)
        except:
            #aperta botão 'next'
            pyautogui.click(844,569, duration=1)
            sleep(2)
            #escolhe o tipo de usuário 'user'
            pyautogui.click(603,279, duration=1)
            sleep(1)
            #aperta o botão 'finish'
            pyautogui.click(833,569, duration=1)
            #Aguarda 2 segundos para a tela carregar
            sleep(2)

    #Imprime a lista de usuários já cadastrados ao final do script
    for user in usuarios_cadastrados:
        print("usuário já cadastrado:", user)
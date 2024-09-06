import pyautogui
import pandas as pd
import time
#Interromper a execução do programa ao arrastar o mouse para o lado superior esquerdo da tela.
pyautogui.FailSafeException

def dude():

    #Lê a planilha Excel
    df = pd.read_excel('assets/dude.xlsx')

    #Cria uma lista para armazenar os usuários já cadastrados
    usuarios_cadastrados = []

    #Loop para cada linha da planilha
    for index, row in df.iterrows():
        username = row['LOGIN']
        password = row['SENHA']

        #Clica no +
        pyautogui.click(505,274)
        #Inserir o username
        pyautogui.click(687,317)
        #Exclui o 'admin' que já vem preenchido
        start_time = time.time()  # remember when we started
        while (time.time() - start_time) < 1:  # for the next 5 seconds
            pyautogui.press('backspace')  # press the backspace key
        #Preence o username
        pyautogui.write(username)
        #inserir o password
        pyautogui.click(680,342)
        pyautogui.write(password)
        #clica no group
        pyautogui.click(682,370)
        #clica no read
        pyautogui.click(653,419)
        #clica no apply (perigo)
        pyautogui.click(778,368)
        #clica no ok (perigo)
        pyautogui.click(780,317)
        #se der erro, clica no x
        try:
            #localiza o erro na tela
            local = pyautogui.locateOnScreen('assets/error_AMS.png', confidence=0.9)
            #printa o erro e o usuário
            print("usuário já cadastrado:", username, "error:", local)
            #adiciona o usuário na lista de usuários já cadastrados
            usuarios_cadastrados.append(username)
            #clica no X e repete o loop
            pyautogui.click(778,368)
            #Aguarda 3 segundos
            time.sleep(3)
        except:
            print("usuário cadastrado com sucesso:", username)
            time.sleep(5)
        
    #Imprime a lista de usuários já cadastrados ao final do script
    for user in usuarios_cadastrados:
        print("usuário já cadastrado:", user)

dude()
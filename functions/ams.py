import pyautogui
import pandas as pd
from time import sleep

#Interromper a execução do programa ao arrastar o mouse para o lado superior esquerdo da tela.
pyautogui.FailSafeException

def ams():

    #Lê a planilha Excel
    df = pd.read_excel('assets/AMS.xlsx')

    #Cria uma lista para armazenar os usuários já cadastrados
    usuarios_cadastrados = []

    #Loop para cada linha da planilha
    for index, row in df.iterrows():
        username = row['LOGIN']
        fullname = row['NOME']
        email = row['EMAIL']
        description = row['LOCAL']
        password = row['SENHA']
        confirmPassword = row['SENHA']

        #click em Users
        pyautogui.click(679, 172)
        #botão direito
        pyautogui.click(button='right')
        #move para create
        pyautogui.moveTo(784, 195)
        #espera 3 segundos
        sleep(2)
        #aperta em user
        pyautogui.click(973, 186)
        sleep(3)
        #inserir username
        pyautogui.click(553,254)
        pyautogui.write(username)

        try:
            #se aparecer o erro de user já existente:
            local = pyautogui.locateOnScreen('assets/error_AMS.png', confidence=0.9)
            #printa o erro e o usuário
            print("usuário já cadastrado:", username, "error:", local)
            #adiciona o usuário na lista de usuários já cadastrados
            usuarios_cadastrados.append(username)
            #clica em cancel e repete o loop
            pyautogui.click(878,454)
            #Aguarda 3 segundos
            sleep(3)
        except:
            pyautogui.moveTo(681,457)
            sleep(1)
            #next
            pyautogui.click(681,457)
            #espera 5 segundos
            sleep(5)
            #inserir fullname
            pyautogui.click(589,213)
            pyautogui.write(fullname)
            #inserir email
            pyautogui.click(591,247)
            pyautogui.write(email)
            #inserir description
            pyautogui.click(595,276)
            pyautogui.write(description)
            #inserir password
            pyautogui.click(704,327)
            pyautogui.write(password)
            #inserir confirm password
            pyautogui.click(705,355)
            pyautogui.write(confirmPassword)

            #scroll
            pyautogui.scroll(-1000)
            #add
            pyautogui.click(920,238)
            sleep(2)
            #operator
            pyautogui.click(641,341)
            #ok
            pyautogui.click(834,461)
            
            #add
            pyautogui.click(923,487)
            sleep(2)
            #allPAPs
            pyautogui.click(641,294)
            #ok
            pyautogui.click(833,457)
            #finish
            pyautogui.click(847,683)
            #Aguarda 3 segundos
            print(username, "cadastrado com sucesso!")
            sleep(3)

    #Imprime a lista de usuários já cadastrados ao final do script
    for user in usuarios_cadastrados:
        print("usuário já cadastrado:", user)

ams()
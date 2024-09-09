import pyautogui
import pandas as pd
from time import sleep

df = pd.read_excel('assets/netnumen.xlsx')
usuarios_cadastrados = []

for index, row in df.iterrows():
    username = row['LOGIN']
    fullname = row['NOME']
    password = row['SENHA']
    confirmPassword = row['SENHA']

    #clique com botão direito no 'Root Department'
    pyautogui.moveTo(95,151)
    pyautogui.click(95,151)
    pyautogui.click(button='right')
    pyautogui.click(button='right')
    #Clique em 'New User'
    pyautogui.click(171, 169)
    sleep(2)
    #Clique em User Name
    pyautogui.click(476,147)
    pyautogui.click(476,147)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    #Inserir o username
    pyautogui.write(username)
    #Clique em Full name
    pyautogui.click(472,175)
    pyautogui.click(472,175)
    #Inserir o nome completo
    pyautogui.write(fullname)
    #Clique em Password
    pyautogui.click(474,204)
    pyautogui.click(474,204)
    #Inserir a senha
    pyautogui.write(password)
    #Clique em Confirm Password
    pyautogui.click(477,232)
    pyautogui.click(477,232)
    #Inserir a senha novamente
    pyautogui.write(confirmPassword)
    #Clique em 'Right'
    pyautogui.click(463,100)
    pyautogui.click(463,100)
    #Clique em 'Supervisor Role'
    pyautogui.click(411,214)
    #Clique em 'OK'
    pyautogui.click(820,662)
    sleep(2)
    #Se der erro de usuário já cadastrado, clique em 'Cancel'
    try:
        local = pyautogui.locateOnScreen('assets/error_netnumen.png', confidence=0.9)
        print(local)
        pyautogui.click(local)
        #Armazena o nome do usuário já cadastrado
        usuarios_cadastrados.append(username)
        print("Usuário já cadastrado: ", username)
        #Clique em 'Cancel'
        pyautogui.click(902,661)
    except:
        #Se não, continua o loop
        print("Usuário cadastrado: ", username)
        sleep(1)
        pass

for user in usuarios_cadastrados:
    print("Usuário já cadastrado: ", user)
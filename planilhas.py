import pyautogui
import pandas as pd
from time import sleep

# Carregue a planilha Excel
df = pd.read_excel('usuarios1.xlsx')
print(df)

for index, row in df.iterrows():
    username = row['LOGIN']
    fullname = row['NOME']
    password = row['SENHA']
    confirmPassword = row['CONFSENHA']
    print(username, fullname, password, confirmPassword)

    #Botão de adicionar user
    pyautogui.click(316,168, duration=1)
    #aguarda 3 segundos
    sleep(3) 
    #Botão de adicionar login
    pyautogui.click(774,196, duration=1)
    pyautogui.click(774,196, duration=1)
    pyautogui.write(username)
    #Botão de adicionar nome
    pyautogui.click(792,227, duration=1)
    pyautogui.write(fullname)
    #Botão de adicionar senha
    pyautogui.click(794,256, duration=1)
    pyautogui.write(password)
    #Botão de adicionar confirmar senha
    pyautogui.click(796,287, duration=1)
    pyautogui.write(confirmPassword)
    #next
    pyautogui.click(844,569, duration=1)
    sleep(3)
    #next
    pyautogui.click(844,569, duration=1)
    sleep(3)
    #tipo de usuário 'user'
    pyautogui.click(603,279, duration=1)
    sleep(3)
    #finish
    pyautogui.click(833,569, duration=1)
    sleep(3)
import pyautogui
from functions.menu import exibir_menu
from functions.SparkEasy import sparkEasy
from functions.ams import ams
from functions.netnumen import netnumen
from functions.dude import dude

# Interromper a execução do programa ao arrastar o mouse para o lado superior esquerdo da tela.
pyautogui.FailSafeException

# Abre o menu de opções
escolha = exibir_menu()
print(f"Você escolheu a opção: {escolha}")

if escolha == 1:
    sparkEasy()
elif escolha == 2:
    ams()
elif escolha == 3:
    netnumen()
elif escolha == 4:
    dude()
else:
    print("Opção inválida! Escolha entre 1 e 4.")

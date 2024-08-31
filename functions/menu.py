# menu.py
def exibir_menu():
    mensagem = (
        "Esse é um script em Python para automatizar a criação de usuários no SparkEasy e UNM, "
        "entretanto, ele pode conter erros devido a diferença entre cada computador e tamanho de tela.\n"
    )
    print(mensagem)
    print("Escolha uma das opções abaixo:")
    print("1. SparkEasy")
    print("2. UNM")
    
    opcao = int(input("Digite o número da opção desejada: "))
    return opcao
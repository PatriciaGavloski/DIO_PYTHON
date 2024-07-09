def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem2(nome):
    print(f"Seja Bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja Bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem2(nome="Guilherme")
exibir_mensagem3()
exibir_mensagem3(nome="Chappie")
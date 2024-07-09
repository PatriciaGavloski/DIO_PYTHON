#Estruturas Condicionais 

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print ("Realizando saque!")
else:
    print("Saldo insuficiente")

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
elif opcao == 2 : 
    print(" Exbindo o extrato... ")
else: 
    print("Opção inválida")


MAIOR_IDADE = 18

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Aida não pode tirar a CNH. ")

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
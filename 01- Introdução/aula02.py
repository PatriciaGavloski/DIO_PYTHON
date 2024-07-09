print(True and True) #True
print(True and False) #False
print(False and False) #False
print(True or True) #True
print(True or False) #True
print(False or False) #False

print("--------------------")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite)or (conta_especial and saldo >= saque)


print(exp_2)

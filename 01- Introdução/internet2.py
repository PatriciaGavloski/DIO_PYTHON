def recomendar_plano():
    consumo = float(input())

    if consumo <= 0:
        print("O consumo mensal deve ser maior que zero.")
        return
    
    if consumo == 10:
        print(f"Plano Essencial Fibra - 50Mbps")
    elif consumo == 19:
        print(f"Plano Prata Fibra - 100Mbps")
    elif consumo == 21:
        print(f"Plano Premium Fibra - 300Mbps")
    else:
        print("Não possuímos pacotes para o valor solicitado.")

recomendar_plano()


# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
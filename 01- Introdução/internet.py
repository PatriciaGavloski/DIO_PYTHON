def internet():
    print("Insira o seu consumo mensal de internet (em GB): ")
    consumo = float(input())
   

    if consumo <= 50:
        print("Seu Plano ideial é: Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.")
    elif consumo > 50 and consumo <= 100:
        print("Seu Plano ideial é: Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.")
    elif consumo > 100 and consumo <= 300:
        print("Seu Plano ideial é: Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.")
    else:
        print("Não possuimos pacotes para o valor solicitado")

internet()
  
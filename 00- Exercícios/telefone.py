import re

def validar_numero_telefone(numero):

    regex = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    if re.match(regex, numero):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."


numero_telefone = input()


resultado = validar_numero_telefone(numero_telefone)
print(resultado)

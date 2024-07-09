frutas = ["Laranja", "Maça", "uva"]
print (frutas)

frutas = []
print(frutas)

letras = list("python")
print (letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2090, "São Paulo", True ]
print(carro)

frutas[0]

matriz = [
    [1, "a, 2"],
    ["b", 3, 4],
    [6, 5, "c"]
]

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]

carros = ["gol", "celta", "palio" ]

for carro in carros:
    print(carro)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

lista.clear()
lista.copy()

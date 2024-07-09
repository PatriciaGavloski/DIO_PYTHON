# Herança Simples

class Veiculo:
    def __init__(self, cor, placa,rodas):
        self.cor = cor
        self.palca = placa
        self.rodas = rodas

        def ligar_motor(self):
            print("Ligando o motor")
        
        def __str__(self):
            return "{self. __class__.name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, rodas, carregado):
        super().__init__(cor, placa, rodas)
        self.carregado = carregado
        self.carregado = False

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xcv-2589", 4)

print(moto)
print(carro)
print(Caminhao)

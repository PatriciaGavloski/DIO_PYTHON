# Método construtor e destrutores 
# Contrutor __init__ 
# Destrutores __del__

class Cachorro:
    def __init__ (self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado

    def __del__ (self):
        print("Removendo a instância da classe...")
    
    def falar(self):
        print("Auau")

    def criar_cachorro():
        c = Cachorro("Zeus", "Branco e Preto", False)
        print(c.nome)

c = Cachorro ("Chappie", "Amarelo")
c.falar()

print("OIEEEEE")
print("OIEEEEE")
del c
print("OIEEEEE")
print("OIEEEEE")


#criar_cachorro()
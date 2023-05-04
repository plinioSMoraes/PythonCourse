# Exercício de fixação 1
# Além do liquidificador, podemos modelar inúmeros eletrodomésticos, 
# tais como: ventilador, batedeira, secador, máquina de lavar e etc.
# 
# Para fixar crie uma objeto da classe Ventilador, semelhante ao exemplo
#  do liquidificador.
# 
# Em seguida faça com que a pessoa tenha um ventilador como atributo 
# através da composição.
# 
# Crie também um método comprar_ventilador.
# 
# Faça com que o print (__str__) de Pessoa informe se sua instância possui
#  ou não um ventilador.

class Ventilador:
    def __init__(self, cor, potencia, tensao, preco):
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao
        self.preco = preco
        self.__ligado = False

    def cor(self, cor):
        self.__cor = cor


class Pessoa:
    def __init__(self, nome, carteira):
        self.nome = nome
        self.carteira = carteira
        self.ventilador = None
    
    def set_carteira(self, valor):
        if (self.carteira < valor):
            raise ValueError
        else: 
            self.carteira -= valor
            self.ventilador = True

    def comprar_ventilador(self, ventilador):
        self.set_carteira(ventilador.preco)

    def __str__(self):
        return f"{self.nome} - {self.carteira} - {self.ventilador}"


# euPessoa = Pessoa('Plinio', 1500)
# meuVentilador = Ventilador('Preto', 1200, 127, 350)
# euPessoa.comprar_ventilador(meuVentilador)
# print(euPessoa)


# Exercício de Fixação 2
# Implemente as classes Secador, Batedeira e MaquinaDeLavar, sempre
# herdando da classe Eletrodomestico. Para testar, instancie as novas
# classes e realize alguns prints, como por exemplo, divulgando o preço do Eletrodoméstico.

class Eletrodomestico:
    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidade deve estar entre 0 e {self.__velocidade_maxima}"
            )

        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_ligado(self):
        return self.__ligado

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


class Secador(Eletrodomestico):
    def __init__(self, cor, potencia, tensao, preco):
        super().__init__( cor, potencia, tensao, preco)

    def imprimir_info(self):
        return f"Secador - Cor: {self.cor}, Preco: {self.preco}"

class Batedeira(Eletrodomestico):
    def __init__(self, cor, potencia, tensao, preco):
        super().__init__(cor, potencia, tensao, preco)

    def imprimir_info(self):
        return f"Batedeira - Cor: {self.cor} Preco: {self.preco}"

class MaquinaDeLavar(Eletrodomestico):
    def __init__(self, cor, potencia, tensao, preco, kilos): #Polimorfismo innit esta sendo sobrescrita
        super().__init__(cor, potencia, tensao, preco) # herança, estamos herdando atributos da classe pai
        self.kilos = kilos

    def imprimir_info(self):
        return f"Maquina de lavar - Cor: {self.cor} Preco: {self.preco} Kilos: {self.kilos}"


newSecador = Secador('preto', 400, 220, 100)
newBatedeira = Batedeira('Branca', 500, 127, 300)
newMaquinaLavar = MaquinaDeLavar('Cinza', 1000, 220, 2000, 10)

print(newSecador.imprimir_info())
print(newBatedeira.imprimir_info())
print(newMaquinaLavar.imprimir_info())
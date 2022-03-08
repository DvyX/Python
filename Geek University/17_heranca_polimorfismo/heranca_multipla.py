"""
Herança Múltipla é a possibilidade de uma classe herdar multiplás classes.

Pode ser feita de duas maneiras:
    - Por Mutiderivação Direta;
    - Por Multderivação Indireta.

- Ambos os métodos herdam todos os atributos e métodos de todas as super classes.
"""
"""
# Mutiderivação Direta
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):  # Está herdando DIRETAMENTE a Base1, Base2 e Base3
    pass


# Multderivação Indireta
class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):
    pass


class Multiderivada2(Base6):  # Base6 herda Base5 que herda Base4, logo Multiderivada2 INDIRETAMENTE herda
    pass                      # todas as outras.

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimenta(self):
        return f'Eu sou {self.__nome}!'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando!'

    def cumprimenta(self):
        return f'Eu sou {self.nome} do mar!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando!'

    def cumprimenta(self):
        return f'Eu sou {self.nome} da terra!'


class Penguim(Terrestre, Aquatico):  # Method Resolution Order - MRO = Sempre prioriza o primeiro.

    def __init__(self, nome):
        super().__init__(nome)


peixe = Aquatico('Kokomi')
print(peixe.nadar())
print(peixe.cumprimenta())

tatu = Terrestre('Roger')
print(tatu.andar())
print(tatu.cumprimenta())

penguim = Penguim('Penpen')
print(penguim.andar())
print(penguim.nadar())
print(penguim.cumprimenta())  # Method Resolution Order - MRO


# Verificar Instância - isinstance()
print('\n# Verificar Instância - isinstance()')
print(f'{penguim.nome} é instância de Aquatico? {isinstance(penguim, Penguim)}')
print(f'{peixe.nome} é instância de Terrestre? {isinstance(peixe, Terrestre)}')
print(f'{tatu.nome} é instância de Animal? {isinstance(tatu, Animal)}')
print(f'{penguim.nome} é instância de object? {isinstance(penguim, object)}')  # Toda classe herda de object

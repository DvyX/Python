"""
Herança Múltipla é a possibilidade de uma classe herdar multiplás classes.

Pode ser feita de duas maneiras:
    - Por Mutiderivação Direta;
    - Por Multderivação Indireta.

- Ambos os métodos herdam todos os atributos e métodos de todas as super classes.

    MRO - Method Resolution Order - Ordem de Resolução de Método
- É a ordem de execução dos métodos, quem será executado primeiro

    - É possivel conferir a ordem de execução de 3 formas:
        + Via propriedade de classe __mro__
        + Via método mro()
        + Via help
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


class Pinguim(Terrestre, Aquatico):  # Method Resolution Order - MRO = Sempre prioriza o primeiro.

    def __init__(self, nome):
        super().__init__(nome)


peixe = Aquatico('Kokomi')
print(peixe.nadar())
print(peixe.cumprimenta())

tatu = Terrestre('Roger')
print(tatu.andar())
print(tatu.cumprimenta())

pinguim = Pinguim('Penpen')
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimenta())  # Method Resolution Order - MRO


# Verificar Instância - isinstance()
print('\n# Verificar Instância - isinstance()')
print(f'{pinguim.nome} é instância de Aquatico? {isinstance(pinguim, Pinguim)}')
print(f'{peixe.nome} é instância de Terrestre? {isinstance(peixe, Terrestre)}')
print(f'{tatu.nome} é instância de Animal? {isinstance(tatu, Animal)}')
print(f'{pinguim.nome} é instância de object? {isinstance(pinguim, object)}')  # Toda classe herda de object


# MRO - Method Resolution Order

print(Pinguim.__mro__)  # Mostra a ordem de resolução (Pinguim - Terrestre - Aquatico - Animal - object)
print(Pinguim.mro())

print(help(Pinguim))
"""
|  Method resolution order:
|      Pinguim
|      Terrestre
|      Aquatico
|      Animal
|      builtins.object
"""
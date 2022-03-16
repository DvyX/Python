"""
Poliformismo

poli - formas
morfismo - formas
Objetos que podem se comportar de formas diferentes

Ao reimpletementar um método presente na super classe em classes filhas, está se realizando uma sobrescrita de
método (Overriding). O Overriding é a melhor definição do polimorfismo
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha deve implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo...')

    @property
    def nome(self):
        return self.__nome


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala au au')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala miau')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} não fala')


taroumaru = Cachorro('Taroumaru')
taroumaru.comer()
taroumaru.falar()

garfield = Gato('Garield')
garfield.comer()
garfield.falar()


mickey = Rato('Mickey')
mickey.comer()
mickey.falar()


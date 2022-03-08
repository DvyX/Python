"""
Método super()

Se refere a super classe

"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'{self.__nome} fala {som}')


class Cachorro(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        # super().faz_som('Som')  # É possível acessar qualquer coisa da super classe com super()
        self.__raca = raca


sofia = Cachorro('Sofia', 'Canino', 'Vira-Lata')
sofia.faz_som('Au')

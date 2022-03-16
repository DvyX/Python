"""
Pickle

Binarização -> Objeto Python
Objeto Python <- Binarização
- Esse processo é chamado de serialização/deserialização

# Puckle não é seguro contra dados maliciosos, não é recomendado trabalhar com arquivos pickle vindos de
fontes deconhecidas.
"""
import pickle


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


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala miau')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self.nome} fala au au')


cachorro = Cachorro('Taroumaru')
gato = Gato('Garield')


# Escrita:
# wb = Write Binary
with open('arquivos/animais.pickle', 'wb') as file:
    pickle.dump((cachorro, gato), file)


# Leitura:
# rb = Read Binary
with open('arquivos/animais.pickle', 'rb') as file:
    cachorro, gato = pickle.load(file)
    print(f'O gato chama-se {gato.nome} e o cachorro {cachorro.nome}')
    cachorro.comer()
    gato.falar()
    print(f'O tipo dos dados é {type(gato)} / {type(cachorro)}')

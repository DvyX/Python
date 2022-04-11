"""
Json e Pickle

JSON - JavaScript Object Notation

pip install jsonpickle
"""

import json


ret = json.dumps(['produto', {'Playstation 5': ('2TB', 'nOVO', '220', 2340)}])  # Formata para deixar em padrão json

print(type(ret))
print(ret)


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


gato = Gato('Diona', 'Siamês')

ret2 = json.dumps(gato.__dict__)
print('\nÁspas Simples: ', end='')
print(gato.__dict__)  # Áspas Simples
print('\nÁspas Duplas: ', end='')
print(ret)            # Áspas Duplas


# Integrando JSON com Pickle
print('\n# Integrando JSON com Pickle:')

import jsonpickle


# Gravar o arquivo json
with open('arquivos/diona.json', 'w') as file:
    ret3 = jsonpickle.encode(gato)
    print(ret3)
    file.write(ret3)


# Leitura do json
print('\n# Leitura do json:')
with open('arquivos/diona.json', 'r') as file:
    conteudo = file.read()
    ret4 = jsonpickle.decode(conteudo)
    print(ret4)
    print(type(ret4))
    print(ret4.nome)
    print(ret4.raca)

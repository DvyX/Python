"""
- Baseado em Dicionarios;
- Força o dicionário a ficar ordenado;
- Tem as mesmas funções dos dicts;
"""
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(dicionario)
print(type(dicionario))
print(dir(dicionario))

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')


# Diferença entre dicts e OrderedDicts

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # Dicionários comuns não guardam ordem

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)

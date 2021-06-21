"""
- Baseado em tuplas;
- Funcionam quase como um dicionário, mas nomeado;
- Tem as mesmas funções das tuplas
"""
from collections import namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')  # Forma 1
cachorro = namedtuple('cachorro', 'idade, raca, nome')  # Forma 2
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])  # Forma 3*

ray = cachorro(idade=2, raca='Labrador', nome='Ray')
print(ray)
print(dir(ray))

# Acessar os dados:
print(ray[0])
print(ray[1])
print(ray[2])

print(ray.idade)
print(ray.raca)
print(ray.nome)

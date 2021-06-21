"""
- Cria um iterável (Zip Object) que junta os elementos de cada um dos iteráveis passados como entrada em pares;
- Após converter map pela primeira vez, ele zera;
- Smepre se baseia no tamanho da menor lista;
"""

i1 = [1, 2, 3]
i2 = 4, 5, 6

zip1 = zip(i1, i2, 'abc')

print(list(zip1))

zip1 = zip(i1, i2, 'abc')
print(tuple(zip1))

zip1 = zip(i1, i2, 'abc')
print(set(zip1))

zip1 = zip(i1, i2)  # Só pode ter 2 elementos
print(dict(zip1))


i3 = {7, 8, 9, 10, 11}
zip1 = zip(i1, i2, i3)

print(list(zip1))


# Desempacotar:
dados = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
print(list(zip(*dados)))


# Exemplo:
prova1 = [90, 75, 96]
prova2 = [97, 83, 76]
alunos = ['Cesar', 'Arthur', 'Joui']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Map:
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))

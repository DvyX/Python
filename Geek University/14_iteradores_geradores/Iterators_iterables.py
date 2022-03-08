"""
Iterator:
    -Pode ser iterado;
    -Retorna um dado, um elemento por vez de uma função next();

Iterable:
    -Retorna um iterator com a funcao
"""
nome = 'Davi'  # É um iterable, não um iterator
numeros = [1, 2, 3, 4, 5]  # É um iterable, não um iterator

# print(next(nome))  # Não um iterator

itnome = iter(nome)
itnumero = iter(numeros)

print(next(itnome))
print(next(itnome))
print(next(itnome))
print(next(itnome))
# print(next(itnome))  # StopIteration

print(next(itnumero))
print(next(itnumero))
print(next(itnumero))

# Na verdade esta fazendo isso:
for letra in nome:
    print(f'{letra}')


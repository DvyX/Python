"""
- Tem a mesma diferença de sorted;
- Não modifica o iterável original;
- Sempre retorna uma lista independente de qual iterável foi utilizado;
"""
i = [1, 2, 3, 4, 5]
res = reversed(i)
print(res)
print(type(res))

print(list(reversed(i)))
print(tuple(reversed(i)))
print(set(reversed(i)))  # Naturalmente não guarda a ordem.

for i in reversed(range(0, 10)):
    print(i, end='')
print()

for i in range(9, -1, -1):  # Mais prático
    print(i, end='')
print()


# Strings:
for i in reversed('davi baestero'):
    print(i, end='')
print()

print(''.join(list(reversed('davi baestero'))))

print('davi baestero'[::-1])  # Mais prático

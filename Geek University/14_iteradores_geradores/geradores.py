"""
- São iterators;
- Nem todo iterator é um generator;
- Podem ser criados com funções geradores (usando "yield")"

Diferença entre Funções e Generator Function:
---------------------------------------------------------------------
/ Funções                  / Generator Function                     /
---------------------------------------------------------------------
/ Utilizam return          / Utilizam yield                         /
/ Retorna 1 vez            / Pode se utilizar yield múltiplas vezes /
/ Retorna um valor         / Retorna um generator                   /
---------------------------------------------------------------------
"""

# Generator Function:


def conta(valor_max):
    i = 1
    while i <= valor_max:
        yield i  # A cada next, ele avança até chegar ao yield
        i += 1


gen = conta(3)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # StopIteration


gen2 = conta(7)
for n in gen2:
    print(n)


gen3 = list(conta(5))
print(gen3)


def soma(valor):
    yield valor + 1
    yield valor + 10


gen4 = soma(5)
print(next(gen4))
print(next(gen4))
# print(next(gen4))  # StopIteration


print(sum(num for num in range(1, 10)))

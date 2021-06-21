lista = list(range(6))
print(lista)

lista.extend([1, 0, 5, -2, -5, 7])
print(lista)

soma = lista.index(0) + lista.index(1) + lista.index(5)
print(f'{lista.index(0)} + {lista.index(1)} + {lista.index(5)} = {soma}')

lista.insert(4, 100)
print(lista)

for i in lista:
    print(i)

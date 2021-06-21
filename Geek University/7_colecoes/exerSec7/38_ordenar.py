lista = []
for i in range(10):
    lista.insert(i, int(input(f'Digite o {i + 1}º valor: ')))
    lista.sort()
    print(lista)

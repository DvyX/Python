
matriz = []
z = int(input('Quantidade de linhas: '))
for i in range(z):
    linha = []
    x = input()
    y = x.split()
    for j in y:
        linha.append(int(j))
    matriz.append(linha)

for i in range(z):
    print(f'{sum(matriz[i])} ', end='')

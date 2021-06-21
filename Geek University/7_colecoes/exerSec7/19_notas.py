
matriz = []
z = int(input('Quantidade de alunos:'))
print('Número da matricula | Média das provas | Média dos trabalhos')
for i in range(z):
    linha = []
    x = input()
    y = x.split()
    for j in y:
        linha.append(int(j))
    matriz.append(linha)

for i in range(z):
    matriz[i].append((matriz[i][1] + matriz[i][2])/2)

for i in range(z):
    for j in range(4):
        print(f'{matriz[i][j]}', end=" ")
    print()


maior = 0
numero = 0
for i in range(z):
    if matriz[i][3] > maior:
        maior = matriz[i][3]
        numero = matriz[i][0]

print(f'Número da matricula do aluno que obteve a nota final mais alta: {numero}, com a nota de {maior}')

media = 0
for i in range(z):
    media += matriz[i][3]
media = media/z
print(f'A média das notas finais é de: {media}')

n1 = int(input('Digite o valor de início: '))
n2 = int(input('Digite o valor final: '))
for i in range(n1, n2 + 1):
    contador = 1
    for j in range(1, i + 1):
        if i % j == 0:
            contador += 1
    if contador <= 3:
        print(f'O Valor {j} é primo')



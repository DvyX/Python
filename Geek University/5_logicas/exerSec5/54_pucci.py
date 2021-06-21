contador = 1;
n = int(input('Digite o número: '))
for i in range(1, n):
    if n % i == 0:
        contador += 1

if contador > 2:
    print(f'Não é primo')
else:
    print(f'É primo')

print("Selecione a operação:")
print("1-Adição | 2-Subtração | 3-Multiplicação\n4-Divisão | 5-Divisão inteira | 6-Resto da divisão\n7-Potênciação")
e = int(input())

if 0 < e < 8:
    x = float(input("Digite o 1º valor:"))
    y = float(input("Digite o 2º valor:"))

if e == 1:
    r = (float(x + y))
    print(f'{x} + {y} = {r}')
elif e == 2:
    r = (float(x - y))
    print(f'{x} - {y} = {r}')
elif e == 3:
    r = (float(x * y))
    print(f'{x} X {y} = {r}')
elif e == 4:
    r = (float(x / y))
    print(f'{x} / {y} = {r}')
elif e == 5:
    r = (float(x // y))
    print(f'A divisão interia de {x}/{y} será: {r}')
elif e == 6:
    r = (float(x % y))
    print(f'Resto da divisão de {x}/{y} será: {r}')
elif e == 7:
    r = (float(x ** y))
    print(f'{x}^{y} = {r}')
else:
    print("Erro, valor inválido")

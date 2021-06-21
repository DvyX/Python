"""
Else - É executado caso não ocorra o erro;
Finally - É sempre executado, independente do erro (Normalmente utilizado para otimização);
"""

try:
    # num = int(input('Informe um número: '))
    num = 1
except ValueError:
    print('Valor inválido')
else:
    print(f'Você digitou {num}')
finally:
    print(f'Finally')


# Exemplo:


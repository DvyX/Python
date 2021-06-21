"""
- Executa algum erro expecifico e permite criar um;
- Finaliza o programa;
"""


def cores(texto, cor):
    corx = 'vermelho', 'verde', 'azul'
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')

    if cor not in corx:
        raise ValueError(f'A cor precisa ser uma dessas: {corx}')
    print(f'{texto} será impresso na cor {cor}')


# cores('Davi', 1)
# cores(2, 'verde')
# cores(3, 4)

cores('Davi', 'verde')
cores('Davi', 'amarelo')

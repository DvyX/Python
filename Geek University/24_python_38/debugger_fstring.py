"""
Debugger mais simples com f-strings
"""


def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


resultado: float = multiplicar(4.67453, 8.5723)

print(f'Resultado completo: {resultado}')
print(f'Resultado parcial: {resultado:.2f}')


print(f'{(media := 8 / 2)} é a metade de {media * 2}')


nome: str = 'Davi'

print(f"nome='{nome}'")
print(f'{nome=}')  # Ao colocar '=' no final da variável é possivel imprimir o nome da variável + seu valor
print(f'{nome.upper()[::-1] * 3=}')  # Também mostra a expressão utilizada


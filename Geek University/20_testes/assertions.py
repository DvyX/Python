"""
Assertions

* se um programa for iniciado com o parâmetro -O, nenhum assertion será validado

- Palavra reservada 'assert' utilizada para realizar simples afirmações utilizadas nos testes;
- Pode-se especificar um segundo argumento ou mensagem personalizada de erro;
- 'assert' pode ser utilizada em qualquer parte do código, não necessáriamente somente nos testes;
- 'asert' pode ser utilizado como lista (assert x in []);
"""


def soma_positivo(a, b):
    assert a > 0 and b > 0, 'Ambos os números precisam ser positivos'
    return a + b


print(soma_positivo(2, 4))
# print(soma_positivo(-2, 4))


def restaurante(comida):
    assert comida in [
        'bife',
        'frango',
        'bisteca',
        'linguiça'
    ], f'{comida} não está no cardápio'
    return f'Pedido: {comida}'


print(restaurante('bife'))
print(restaurante('frango'))
print(restaurante('batata'))

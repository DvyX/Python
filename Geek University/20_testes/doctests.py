"""
Doctests são testes que ficam nas docstrings

Executar teste no console: python -m doctest -v nome.py

TDD  - Test Driven Development - Desenvolvimento Orientado por Testes:
Quando o teste é feito antes do desenvolvimento do código
"""


def soma(a, b):
    """
    soma os números a e b

    # >>> soma(1, 2)
    # 3
    """
    return a + b


print(soma(3, 4))


# Exemplo com TDD
def duplicar(value):
    """
    Duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * i for i in value]


def oi():
    """
    Fala oi

    # >>> oi() # "oi"  # Causa erro por conta das àspas triplas
    'oi'
    """
    return "oi"


def verdade():
    """
    Retorna a verdade

    # Causa falha pois 'True' está com espaços no final, porém na IDE pycharm os espaços desnecessários são excluidos
    >>> verdade()
    True
    """
    return True

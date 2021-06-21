import sys


def leitura():
    """
    Realiza a leitura dos números {num1}, {num2} e devolve a {operacao}, e ambos os números.
    :return: Operação, sendo adição, subtração, multiplicação ou divisão.
    """
    conta = input('Digite a conta que deseja fazer: ')
    e1 = conta.find(' ')
    e2 = conta.rfind(' ')

    num1 = conta[:e1]
    calculo1 = conta[e1+1:e2]
    num2 = conta[e2+1:]

    numero1 = float(num1)
    numero2 = float(num2)

    return numero1, calculo1, numero2


def operacao(num1, caculo, num2):
    """
    Define qual operação será realizada entre {num1} e {num2}.
    :param num1: O primeiro número a ser calculado.
    :param caculo: A operação que realizará a conta.
    :param num2: O primeiro número a ser calculado.
    :return: O resultado final.
    """
    if caculo == '+':
        return soma(num1, num2)
    elif caculo == '-':
        return sub(num1, num2)
    elif caculo == '/':
        return div(num1, num2)
    elif caculo == '*' or 'x' or 'X':
        return mult(num1, num2)
    else:
        sys.exit('Operação desconhecida.\nUse as seguintes operações e tente novamente:\nAdição = "+"\nSubtração = '
                 '"-"\nMultiplicação = "x" ou "*"\nDivisão = "/"')


def soma(num1, num2):
    """
    Realiza a soma entre {num1} e {num2}.
    :param num1: O primeiro número a ser calculado.
    :param num2: O primeiro número a ser calculado.
    :return: O resultado da soma.
    """
    return num1 + num2


def sub(num1, num2):
    """
    Realiza a subitração de {num1} por {num2}.
    :param num1: O primeiro número a ser calculado.
    :param num2: O primeiro número a ser calculado.
    :return: O resultado da subtração.
    """
    return num1 - num2


def mult(num1, num2):
    """
    Realiza a multiplicação entre {num1} e {num2}.
    :param num1: O primeiro número a ser calculado.
    :param num2: O primeiro número a ser calculado.
    :return: O resultado da multiplicação.
    """
    return num1 * num2


def div(num1, num2):
    """
    Realiza a divisão de {num1} por {num2}.
    :param num1: O primeiro número a ser calculado.
    :param num2: O primeiro número a ser calculado.
    :return: O resultado da divisão.
    """
    return num1 / num2


calculo = leitura()
resultado = operacao(*calculo)
print(resultado)

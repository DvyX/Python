"""
Funções de Maior Grandeza - Higher Order Functions - HOF

 Quando uma linguagem de programação suporta HOF, indica que se pode ter funções
que retornam outras funções ou passar funções como parâmetros para outras funções
ou variáveis do tipo função.

"Em Python, as funções são Cidadãos de Primeira Classe, ou First Class Citizen."

 Funções dentro de funções são conhecidas como Nested Functions, ou Inner Functions (Funções internas).
    -Elas podem acessar o escopo de funções externas
"""


# Definição:
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):  # Recebe uma função como parâmetro
    return funcao(num1, num2)


# Teste:
print(calcular(4, 3, somar))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Functions - Funções Alinhadas - Inner Functions
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Saia daqui ', 'Que bom te ver '))

    return humor() + pessoa


print(cumprimento("Seu Jorge"))


# Retornando funções de outras funções
def cores(equipamento):
    def rgb():
        cor = choice(('Vermelho', 'Verde', 'Azul'))
        return f'{equipamento} {cor}'

    return rgb()


coisa = cores("Martelo")
print(coisa)

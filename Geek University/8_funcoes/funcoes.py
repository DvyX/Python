"""
- DRY - Don't Repeat Yourself;
"""
from random import random


# Definição:
def hello_world():
    print('Hello World')


hello_world()
variavel = hello_world  # Uma variável pode receber uma função;
variavel()  # E executa-la via variável;


# Retorno:
def quadrado_sete():
    r = 7 ** 2
    return r


print(quadrado_sete())


# Diversos returns:
def varios_returns():
    return 1, 2, 3, 4


n1, n2, n3, n4 = varios_returns()
print(n1, n3, n3, n4)
print(varios_returns())
print(type(varios_returns()))


# Parâmetros:
def soma(num1, num2):
    return num1 + num2


x = soma(1, 2)
print(x)
print(soma(5, 5))


def outra(num1, b, msg):
    return (num1 + b) * msg


print(outra(2, 4, 'Msg '))
print(outra(msg='Msg 2 ', num1=8, b=2))


def moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(moeda())


# Default Parameters:
def exponencial(numero, potencia=2):  # Por padrão será elevado a 2 (DEFAULT DEVEM FICAR AO FINAL);
    return numero ** potencia


print(exponencial(3, 3))
print(exponencial(3))

# Chamar funções em outros arquivos:
# from 8_funcoes.funcoes import hello_world;

total = 0


def incrementa():
    global total  # Identifica que quer trabalhar com a variável global;
    total += 1
    return total


print(incrementa())


# Função em Função
def fora():
    i = 10

    def dentro():
        nonlocal i  # Identifica de trabalhar não com a variável global, mas a global dentro da função;
        i += 1
        return i

    return dentro()


print(fora())


# Docstrings: Documentando funções
def hello_world():
    """Retorna String 'Hello World'"""
    return 'Hello World'


print(hello_world())
help(hello_world)
help(print)


def nome(nome2, sobrenome=''):
    """
    Retorna uma String do 'nome' + 'sobrenome' em uma mensagem de boas vindas.
    :param nome2: Primerio nome da usuário.
    :param sobrenome: Sobrenome opcional do usuário.
    :return: "Seja bem vindo {nome} {sobrenome}."
    """
    return f'Seja bem vindo {nome2} {sobrenome}.'


print(nome('Davi', 'Baestero'))
help(nome)

"""
Argumentos somente posicionais

todos os argumentos antes da / serão somente posicionais
todos os argumentos depois do * nunca serão posicionais
"""


def cumprimenta(nome, /):
    return f'Olá {nome}'


print(cumprimenta('Davi'))
# print(cumprimenta(nome='Davi'))


def cumprimenta2(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


print(cumprimenta2('Jair'))
print(cumprimenta2('Jair', 'Oi'))
print(cumprimenta2('Jair', mensagem='Oi'))
# print(cumprimenta2(nome='Jair', mensagem='Oi'))


def cumprimenta3(nome, *, mensagem):
    return f'{mensagem} {nome}'


# print(cumprimenta3('Osvaldo', 'Oi'))
print(cumprimenta3('Osvaldo', mensagem='Opa'))
print(cumprimenta3(nome='Osvaldo', mensagem='Opa'))

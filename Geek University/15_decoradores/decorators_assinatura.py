"""
Decorators com Diferentes Assinaturas

- Decorator Pattern (args e kwargs)

"""
"""
def gritar(funcao):
    def aumentar(texto):
        return funcao(texto).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'


@gritar  # TypeError pois esperava 1 parâmetro e recebeu 2
def ordenar(principal, acompanhamento):
    return f'Gostaria de {principal}, acompanhado de {acompanhamento}'


print(saudacao('Davi'))
print(ordenar('Picanha', 'Batata Frita'))
"""


# Decorator Pattern
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Gostaria de {principal}, acompanhado de {acompanhamento}'


print(saudacao('Davi'))
print(ordenar('Picanha', 'Batata Frita'))


# Decorator com Argumentos:
print('\n# Decorator com Argumentos:')


def verifica_primeiro(valor):                                                      # Recebe o primeiro valor de entrada
    def interna(funcao):                                                           # Recebe a função a ser decorada
        def outra(*args, **kwargs):                                                # Realiza as verificações
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro('Pizza')
def tier_list_comida(*args):
    print(args)


@verifica_primeiro(10)
def soma10(num1, num2):
    return num1 + num2


# Testes:
print(soma10(10, 12))
print(soma10(11, 11))

print(tier_list_comida('Pizza', 'Hamburger', 'Batata Frita'))
print(tier_list_comida('Batata Frita', 'Hamburger', 'Pizza'))

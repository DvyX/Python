"""
Decoradores - Decorators
    - São funções;
    - Envolvem outras funções e aprimoram seus comportamentos;
    - Exemplo de HOF;
    - Sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

"""
"""

# Sintaxe Incorreta:
def educacao2(funcao):
    def apresentacao2():
        print('Seja bem vindo(a).')
        funcao()
        print('Tenha um excelente dia!')
    return apresentacao2


def display2():
    print('Esta é a loja do seu Jorge.')


apresentar = educacao2(display2)

apresentar()
"""


# Syntact Sugar:
def educacao(funcao):
    def apresentacao():
        print('Seja bem vindo(a).')
        funcao()
        print('Tenha um excelente dia!')
    return apresentacao


@educacao
def jorge():
    print('Esta é a loja do seu Jorge.')


@educacao
def juan():
    print('Esta é a loja do seu Jorge.')


jorge()
juan()

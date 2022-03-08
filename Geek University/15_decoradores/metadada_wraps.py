"""
Preservando Metadata com wraps

- Metadata = São dados intrísticos em arquivos;
- Wraps = São funções que envolvem elementros com diversas finalidades;
"""
'''
def ver_log(func):
    def logar(*args, **kwargs):
        """Função (logar) dentro de outra função"""
        print(f'Chamando função ({func.__name__})')
        print(f'Documentação: {func.__doc__}')
        return func(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


print(soma(2, 3))

print(soma.__name__)  # Dados incorretos, apresentando os valores da função logar ao invez da soma
print(soma.__doc__)
'''

# Resolução do Problema:
from functools import wraps


def ver_log(func):
    @wraps(func)  # Preserva a metadata da função
    def logar(*args, **kwargs):
        """Função (logar) dentro de outra função"""
        print(f'Chamando função ({func.__name__})')
        print(f'Documentação: {func.__doc__}')
        return func(*args, **kwargs)

    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


print(soma(2, 3))

print(soma.__name__)
print(soma.__doc__)

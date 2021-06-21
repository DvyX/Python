"""
Expressões lambdas são funções sem nome, anônimas

- Mais utilizada no local de execução do que instanciar uma variavel;
- 'variável' = lambda 'parâmetro': retorno
"""


# Função base:
def funcao(x):
    return 3 * x


print(funcao(3))

# Lambda
calc = lambda x: 3 * x
# 'variável' = lambda 'parâmetro': retorno
print(calc(3))

nome_idade = lambda nome, sobrenome, idade: f'{nome.strip().title()} {sobrenome.strip().title()}: {idade}'
print(nome_idade('   davi ', 'BaesTERO  ', 17))

sem_parametro = lambda: 'Lambdas Python'
print(sem_parametro())

# Como realmente devem ser utilizadas:
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Hebert', 'Orson Scott Cart',
           'Douglas Adams', 'H. g. Wells', 'Leigh Brackett']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())  # Ordenando pelo sobrenome
print(autores)


# Função Quadratica: f(x) = a * x ** 2 + b * x + c
def quadratica(a, b, c):
    """
    Armazena a função quadratica de a, b, c, nessecitando 'X' para terminar o calculo
    :param a: Int
    :param b: Int
    :param c: Int
    :return: a * x ** 2 + b * x + c, sendo X um valor a ser inserido
    """
    return lambda x: a * x ** 2 + b * x + c


funcao_lambda = quadratica(2, 3, -5)  # Recebe a função lambda com valor 'x' para inserir

print(funcao_lambda(0))
print(funcao_lambda(1))
print(funcao_lambda(2))

print(quadratica(3, 0, 1)(2))

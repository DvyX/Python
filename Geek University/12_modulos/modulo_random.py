"""
- Módulos são outros arquivos Python;
- Não é recomendado importar todo o módulo, somente a função desejada para fins de otimização;

- Random: Por padrão gera um número aleatório entre 0 e 1;
"""
# import random
from random import random  # Forma recomendada de se importar qualquer coisa
print('\nrandom():')
# print(random.random())  # Import Geral
print(random())  # Import Expecífico
print(dir(random))


# uniform() - random entre os valores estabelecidos:
print('\nuniform():')
from random import uniform
for i in range(5):
    print(uniform(3, 7))  # Ultimo numero (7) não incluso

# randint() - random int entre os valores estabelecidos:
print('\nrandint():')
from random import randint
# Gerador de apostas da megasena
for i in range(6):
    print(randint(1, 61), end=', ')
print()


# choice() - valor aleatório entre um iterável:
print('\nchoice():')
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

print(choice('Davi'))


# shuffle() - Enbaralha um iterável:
print('\nshuffle():')
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)


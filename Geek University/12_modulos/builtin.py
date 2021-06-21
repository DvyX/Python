"""
- Módulos integrados;
- Não é recomendado importar todo o módulo, somente a função desejada para fins de otimização;
- Alias: "Nomear" um método
"""
import random as rdm  # alias

print(rdm.random())


from random import randint as rdi, choice as escolha

print(rdi(0, 10))
print(escolha([1, 10, 100]))


# Utilizando Tuple:
from random import (
    random,
    randint,
    randrange,
    shuffle
)

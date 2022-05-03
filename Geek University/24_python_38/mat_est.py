"""
Funções matemáticas  e estatísticas
"""
import math


# math.prod - Retorna o produto de um container numérico:
print('# math.prod')

nuns1 = [1, 3, 4, 6]
nuns2 = (1, 3, 4, 6)
nuns3 = {1, 3, 4, 6}

print(math.prod(nuns1))
print(math.prod(nuns2))
print(math.prod(nuns3))


# math.isqrt - Retorna a raiz quadrada inteira de um número
print('\n# math.isqrt')

print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(17))
print(math.sqrt(17))


# math.dist - Retorna a distância euclidiana entre dois pontos, 3D ou 2D
print('\n# math.dist')

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))


# math.hypot - Retorna a hipotenusa, ou norma Euclidiana
print('\n# math.hypot')

print(math.hypot(*p3d1))
print(math.hypot(*p2d1))


# Estatísticas:
import statistics

# statictics.fmean - Calcula a média de números reais
print('\n# statictics.fmean')

real = [11.45, 3.5634, 4.63, 89.4353]
inteiro = [2, 5, 8, 1]

print(statistics.fmean(real))
print(statistics.fmean(inteiro))


# statictics.geometric_mean - Calcula a média geométrica de números reais
print('\n# statictics.geometric_mean')

print(statistics.geometric_mean(real))
print(statistics.geometric_mean(inteiro))


# statictics.multimode - retorna o valor mais frequente em uma sequência
print('\n# statictics.multimode')

sequencia1 = [1, 3, 6, 7, 1, 3, 4, 6, 0, 1, 2, 4, 5, 1]
sequencia2 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
nome = 'Davi Baestero Silva'

print(statistics.multimode(sequencia1))
print(statistics.multimode(sequencia2))
print(statistics.multimode(nome))


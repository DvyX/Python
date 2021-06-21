"""
Mesmo principio de list_comprehension
"""

# Sintaxe:
# {chave:valor for valor in iteravel}

# sintaxe = {'chave': 'valor' for 'valor' in 'iteralvel'}

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(numeros)
print(quadrado)


listaN = [1, 2, 3, 4, 1, 2]  # Não repete valores
cubo = {valor: valor ** 3 for valor in listaN}

print(listaN)
print(cubo)


chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(len(chaves))}
print(chaves)
print(valores)
print(mistura)


res = {num: ('par' if num % 2 == 0 else 'impar') for num in listaN}
print(res)

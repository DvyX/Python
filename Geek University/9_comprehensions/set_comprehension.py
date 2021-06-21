"""
Mesmo principio de list e dict comprehension
- Não aceita numeros repetidos;
- Não guarda ordem;
"""

numeros = {num for num in range(1, 7)}
print(numeros)

x2 = {x ** 2 for x in range(10)}
print(x2)

# Transformando em dict
dict1 = {x: x ** 2 for x in range(10)}
print(dict1)

letras = {letra for letra in 'Davi Baestero'}
print(letras)

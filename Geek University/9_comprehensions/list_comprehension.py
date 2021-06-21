"""
- Lists 2.0
"""
# Sintaxe:
# [dado for dado in iterável]

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)


def dobro(*args):
    r = [n * 2 for n in args]
    return r


print(dobro(*numeros))

# Exemplo:
palavra = 'Davi Baestero Silva'
print([letra.upper() for letra in palavra])

pessoas = ['maria', 'josé', 'pedro', 'guilherme', 'vanessa']
print([pessoas.title() for pessoas in pessoas])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([int(numero) for numero in ['1', '2', '3', '4', '5']])


# Parte 2:

numeros = [1, 4, 7, 9, 0, 5, 76, 845, 4, 6, 8, 345, 6, 45, 76, 87, 45678, 2]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Qualquer par numero % de 2 é 0, e 0 em python é False.
print(f'Pares: {[numero for numero in numeros if not numero % 2]}')
# Qualquer impar numero % de 2 é 1, e 1 em python é True.
print(f'Impares: {[numero for numero in numeros if numero % 2]}')

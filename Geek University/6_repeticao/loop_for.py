nome = 'Davy X'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)

"""
# exemplo de for-
for letra in nome:
    print(letra)
for letra in nome:
    print(letra, end='')
                'end serve para o que vai estar no final do print'
for letra in nome:
    print(letra)
for numero in lista:
    print(numero)
for numero in range(1, 10):
    print(numero)

# enumerate-
   'i(primeiro valor) v(segundo valor)'
for i, v in enumerate(nome):
    print(nome[i])

# _ descarta um valor desnecessário-
for _, v in enumerate(nome):
    print(v)

# funcionamento do enumerate-
for v in enumerate(nome):
    print(v)
    
# for com input 1-
i = int(input('Digite a quantidade de vezes que o loop deve rodar:'))
for n in range(0, i):
    print(f'Loop {n}')
    
# for com input 2-
i = int(input('Digite a quantidade de vezes que o loop deve rodar:'))
soma = 0
for n in range(1, (1 + i)):
    num = int(input(f'Digite o {n}º/{i} numero'))
    soma += num
print(f'A Soma dos números é {soma}')
"""


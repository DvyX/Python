"""
Permite fazer atribuição e retorno de valor em uma única expressão

variável := expressão
"""
nome = 'Davi'
print(nome)

print(nome := 'Davi')

"""
cesta = []
while True:
    fruta = input('Informe a fruta')
    if fruta == 'stop':
        break
    cesta.append(fruta)
print(cesta)
"""

cesta1 = []
while (fruta1 := input('Informe a fruta')) != 'stop':
    cesta1.append(fruta1)
print(cesta1)

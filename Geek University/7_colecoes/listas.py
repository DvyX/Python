"""
Funcionam como vetores/matrizes em Java;

- Não possuem tamanho fixo;
- Aceita qualquer tipo de dado;
- Representadas por colchetes [] ;
- É possível criar listas dentro de listas;
- São mutaveis (é possível alterar);
- Listas vazias são consideradas False em boolean, e vise versa.
"""
# Exemplos Listas:
print("# Verificação")
print(type([]))
print(dir([]))

listaInt = [1, 2, 10, 44, 1, 21, 4, 1, 777, 8, 6546]
listaStr1 = ['L', 'i', 's', 't', 'a', 's', ' ', 'P', 'y', 't', 'h', 'o', 'n']
listaStr2 = list('Listas Python')
listaStr3 = ['Listas', 'Python']
listaRange = list(range(22))
listaIntStr = ['Lista', 1, 5, 8, 40, 55, 734, 40]
listaTrue = [1, 'a', 3.45, True, [6, 1, 8], 12597846, 'Python']
listaChar = [4]

# Checar valores:
print('# Checar valores:')
num = 8
if num in listaInt:
    print(f'Achei o número {num}')
else:
    print(f'Não achei o número {num}')

# Exemplo 2:
letra = 'v'
if letra in listaStr2:
    print(f'Achei a letra {letra}')
else:
    print(f'Não achei a letra {letra}')

# Iterar listas:
print('\n# Iterar listas:')
for elemento in listaStr1:
    print(elemento)
'''
# Exemplo 2
carrinho = []
produto = ''
i = 1
print('Adicione um produto na lista ou digite "sair" para sair:')
while produto != 'sair':
    produto = input(f"Adcione o {i}º produto:")
    if produto != 'sair':
        carrinho.append(produto)
print('\nProdutos selecionados:')
for produto in carrinho:
    print(produto)
'''
# Acessar elementos de forma indexada
print("\n# Acessar elementos:")
cores = ['Vermelho', 'Verde', 'Azul']
print(cores[0])  # Vemelho
print(cores[1])  # Verde
print(cores[2])  # Azul

print(cores[-1])  # Azul
print(cores[-2])  # Verde
print(cores[-3])  # Vemelho

for i, cor in enumerate(cores):
    print(i, cor)


# Slice [::] - [inicio:final:contagem]:
print("# Slice")
print(listaRange)
print(listaRange[::-1])
print(listaRange[0:20:3])

# .sort() - ordenar de forma crescente:
print("\n# .sort")
print(listaInt)
listaInt.sort()
print(listaInt)

# .count() - contar as ocorrências de um valor:
print("\n# .count")
print(listaInt.count(1))
print(listaStr2.count('t'))

# .append() - adicionar um valor (1 elemento por vez):
print("\n# .append")
print(listaInt)
listaInt.append(666)
print(listaInt)

listaTrue.append([1, 83, 7])
print(listaTrue)

# .extend() - adcionar valores (vários por vez [sintaxe como lista]):
print("\n# .extend")
print(listaInt)
listaInt.extend([2, 84, 8])
print(listaInt)

listaIntStr.extend('Java')
print(listaIntStr)
listaIntStr.extend(['kk', 7])
print(listaIntStr)

# .insert() - adcionar um valor em uma posição determinada:
print("\n# .insert")
print(listaRange)
listaRange.insert(2, 'casa 2')
print(listaRange)
listaRange.insert(8, 99999)
print(listaRange)

# .reverse() = inverter a lista:
print("\n# .reverse")
print(listaStr2)
listaStr2.reverse()
print(listaStr2)

# .copy() - copiar uma lista:
print("\n# .copy")
listaNew = listaRange.copy()
print(listaNew)

# .pop() - remover um elemento da lista (caso defaut, remove o último elemento) ,(também retorna o elemento removido):
print("\n# .pop")
print(listaStr2)
listaStr2.pop()
print(listaStr2)

listaStr2.pop(5)
print(listaStr2)

print(listaStr2.pop())
print(listaStr2)

# .clear() - resetar a lista:
print("\n# .clear")
print(listaNew)
listaNew.clear()
print(listaNew)

# .split() - transformar string em lista (separando por espaço por defaut):
print("\n# .split")
string1 = 'Uma String Qualquer'
print(string1)
string1 = string1.split()
print(string1)

string2 = 'Uma frase,separada por,virgula'
print(string2)
string2 = string2.split(',')
print(string2)

# .join() - converter lista em string:
print("\n# .join")
listaStr3 = ['Listas', 'em', 'Python']
print(listaStr3)
string3 = '_'.join(listaStr3)
print(string3+"\n")

print(listaStr1)
string4 = ''.join(listaStr1)
print(string4)

# .index() - mostrar o indice de X elemento:
print("\n# .index")
print(listaIntStr)
print(listaIntStr.index(40))
print(listaIntStr.index(40, 5))     # A partir d X indice
print(listaIntStr.index(40, 6, 8))  # A partir d X até Y indice

# len, sum, min/max - tamanho, soma, menor/maior valor:
print("\n# len / sum / max / min")
print(listaInt)
print(len(listaInt))
print(sum(listaInt))
print(max(listaInt))
print(min(listaInt))

# tuple() - Lista para tupla:
print("\n# Tuple")
print(listaIntStr)
tupla = tuple(listaIntStr)
print(tupla)
print(type(tupla))

# Desempacotamento de listas (erro caso não tenha o número exato de valores para receber):
print("\n# Desempacotamento")
listaNew = [1, 2, 3.14, 'Davy']
print(listaNew)
num1, num2, float1, str1 = listaNew
print(num1, num2, float1, str1)

# Shallow Copy / Deep Copy:

# Deep Copy = Copiar os dados da lista X para a lista Y sem alrerar os dados da lista X
print("\n# Deep Copy / Shallow Copy")
print("-Deep Copy:")
print(listaInt)
listaNew = listaInt.copy()  # .copy : Caracteristica principal do Deep Copy
print(listaNew)
listaNew.append(616)
print(listaInt)
print(listaNew)

listaNew.clear()
# Shallow Copy = Copiar os dados da lista X para a Y alterando o valor das 2

print("\n-Shallow Copy:")
print(listaInt)
listaNew = listaInt  # Atribuição '=' : Caracteristica principal do Shallow Copy
print(listaNew)
listaNew.append(616)
print(listaInt)
print(listaNew)

# Matrizes:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)
print(matriz[1][2])
print(matriz[2][-1])
[[print(valor) for valor in matrizx] for matrizx in matriz]

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

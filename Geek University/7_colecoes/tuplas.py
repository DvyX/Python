"""
Tuplas:

- São parecidas com listas;
- Representadas por parênteses ();
- São declaradas pela ',' a pesar do parênteses ();
- São imutaveis (não é possível alterar);
- Ao alterar uma tupla, se cria uma nova;
- Declaração de tuplas com 1 elemento devem ser feitas com ',' no final;
- Metodos de adição e remoção de valores não existem, dado o fato de serem imutaveis;
- Muitos métodos das Listas também funcionam nas Tuplas;
- SEMPRE utilizar tuplas em casos que não irão ser alterados.

# Tipos de declaração:
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))
# Diferentes formas de declaração.
tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

tupla3 = (4)  # Não é tupla (int)
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Ou = 4,
print(tupla4)
print(type(tupla4))
"""
# Exemplos de tuplas
print("# Declaração")
print(type(()))
print(dir(()))

tuplaInt = (1, 2, 10, 44, 1, 21, 4, 1, 777, 8, 6546)
tuplaStr1 = ('T', 'u', 'p', 'l', 'a', 's', ' ', 'P', 'y', 't', 'h', 'o', 'n')
tuplaStr2 = (tuple('Tuplas Python'))
tuplaStr3 = ('Tuplas', 'Python')
tuplaRange = (tuple(range(11)))
tuplaIntStr = ('Lista', 1, 5, 8, 40, 55, 734, 40)
tuplaTrue = (1, 'a', 3.45, True, [6, 1, 8], 12597846, 'Python')
tuplaChar = (4,)

# Verficação:
print("\n# Verificação")
print(3 in tuplaInt)
print(2 in tuplaInt)

"""
# Iterar:
print("\n# Iterar")
for n in tuplaInt:
    print(n)

for i, v in enumerate(tuplaInt):
    print(i, v)
"""

# Desempacotamento de tuplas (erro caso não tenha o número exato de valores para receber):
print("\n# Desempacotamento")
tema, linguagem = tuplaStr3
print(tema)
print(linguagem)

# len, sum, min/max - tamanho, soma, menor/maior valor:
print("\n# len / sum / max / min")
print(tuplaInt)
print(len(tuplaInt))
print(sum(tuplaInt))
print(max(tuplaInt))
print(min(tuplaInt))


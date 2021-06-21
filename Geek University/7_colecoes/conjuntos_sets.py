"""
- Conjuntos são referência a teoria dos conjuntos da matemática;
- Em Python são conhecidos como Sets;
- Sets (conjuntos) não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Não são acessados por indices;
- Úteis para armazenar valores onde não se importa a ordem;
- Representados por {};

- Diferença entre Sets e Dicionários:
    - Um Dicionário tem chave/valor
    - Um Set tem somente 1 valor
"""

# Declaração
print("# Declaração")
s = {1, 3, 2, 4, 5, 2, 3}
print(s)
print(type(s))
print(dir(s))

s = set({1, 3, 2, 4, 5, 2, 3})
print(s)
print(type(s))

lista = (1, 2, 3, 4, 5, 6, 2, 4, 6, 8)
print(lista)
print(set(lista))

tupla = [1, 2, 3, 4, 5, 6, 2, 4, 6, 8]
print(tupla)
print(set(tupla))


# Adcionar elementos:
print("\n# Adcionar elementos:")
s1 = {1, 2, 3}
print(s1)
s1.add(4)
print(s1)

# Remover elementos (não retorna valores):
print("\n# Remover elementos:")
s1.remove(3)  # Valor a ser removido, não é o indice
# s1.remove(3)  # Caso o valor não exista, gera erro KeyError
print(s1)

s1.discard(2)
s1.discard(22)  # Não gera erro
print(s1)


# Copiar elementos (Deep/Shallow Copy):
print("\n# Copiar elementos (Deep/Shallow Copy):")
s2 = set(range(1, 10))
# Deep Copy:
print("\n# Deep Copy:")
deep = s2.copy()
print(deep)
print(s2)
deep.add(10)
print(deep)
print(s2)
print("\n# Shallow Copy:")
s3 = s2
print(s3)
print(s2)
s3.add(10)
print(s3)
print(s2)

# .clear: Limpar
print("\n# .clear:")
print(s1)
s1.clear()
s2.clear()
s3.clear()
print(s1)

# Sun, Len, Min, Max:
print('\n # Sun, Len, Min, Max: ')
print(s)
print(f'Sun: {sum(s)}')
print(f'Len: {len(s)}')
print(f'Min: {min(s)}')
print(f'Max: {max(s)}\n')


# Exemplo:
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'São Paulo', 'Cuiaba', 'Cuiaba']

print(cidades)
print(len(cidades))  # Quantidade de visitas
print(len(set(cidades)))  # Quantidade de cidades


# Métodos Mátemáticos:
print("\n# Métodos Mátemáticos:")
# Cenário 1: Imagine que temos dois conjuntos: Um com estudantes de um cuso de Python e um com estudantes de Java:

estudantes_python = {'Marcos', 'Patricia', 'Elen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

print(f'Estudantes do curso de Python:{estudantes_python}')
print(f'Estudantes do curso de Java{estudantes_java}')

# Alguns alunos estudam ambos os cursos, gere um conjunto com o nome dos estudantes que estudam em apenas um curso
print("\n# conjunto com o nome dos estudantes que estudam em apenas um curso: União")

# Forma 1 - .union:
print("\n# .union:")
union1 = estudantes_python.union(estudantes_java)
union2 = estudantes_java.union(estudantes_python)
print(union1)
print(union2)

# Forma 2 - pipe | :
print("\n# pipe '|' :")
pipe1 = estudantes_python | estudantes_java
pipe2 = estudantes_java | estudantes_python
print(pipe1)
print(pipe2)

# adição = estudantes_python + estudantes_java  # Não funciona

# Gere um conjunto com o nome dos estudantes que estudam em ambos os cursos
print("\n# Conjunto com o nome dos estudantes que estudam em ambos os cursos: Interceção")

# Forma 1 - .intersection:
print("\n# .intersection:")
inter1 = estudantes_python.intersection(estudantes_java)
inter2 = estudantes_java.intersection(estudantes_python)
print(inter1)
print(inter2)

# Forma 2 - E comercial & :
print("\n# E comercial '&' :")
e1 = estudantes_python & estudantes_java
e2 = estudantes_java & estudantes_python
print(e1)
print(e2)

# Gere um conjunto com o nome dos estudantes que estudam em um, mas não no outro
print("\n# Conjunto com o nome dos estudantes que estudam em um, mas não no outro: Diferença")

print("\n# .difference:")
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

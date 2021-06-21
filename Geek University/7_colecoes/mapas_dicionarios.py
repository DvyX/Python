"""
- Em Python são conhecidos em python como Dicionários;
- São coleções tipo {chave:valor};
- Representados por {};
- Aceitam qualquer tipo de dado;
- Atualização e Adição de dados é a mesma;
- Não se pode ter chaves repetidas;
"""

# Declaração
print("# Declaração")
print(type({}))
print(dir({}))

cidades = {'sp': 'São Paulo', 'rj': 'Rio de Janeiro', 'ba': 'Bahia'}
print(cidades)
print(type(cidades))

cidades2 = dict(sp='São Paulo', rj='Rio de Janeiro', ba='Bahia')
print(cidades)
print(type(cidades))

# Acesso:
print("\n# Acesso")

# 1 Forma:
print(cidades['sp'])
# print(cidades['mg']) erro

# 2 Forma (.get):
print("\n# .get")
print(cidades.get('sp'))
print(cidades.get('mg'))

print(cidades.get('mg', 'Não encontrado'))
print(cidades.get('rj', 'Não encontrado'))

# Desempacotar:
print("\n# Desempacotar")

print(cidades.keys())
print(cidades.values())
print(cidades.items())

for key in cidades:
    print(key)

for key in cidades:
    print(cidades[key])

for key in cidades.keys():
    print(f'{key}: {cidades[key]}')

for key, value in cidades.items():
    print(f'chave={key} valor={value}')

# Todos os tipos de dados (Tuplas):
print("\n# Teste todos os tipos de dados\nTuplas:")
localidades = {
    (35.5684, 45.5487): 'Escritório em São Paulo',
    (85.1345, 75.4521): 'Escritório em Nova York',
    (125.6598, 15.6428): 'Escritório em Tokyo',
}

print(localidades)
print(type(localidades))

# Adicionar Elementos:
print("\n# Adicionar")
receita = {'jan': 200, 'fev': 500, 'mar': 300}
print(receita)

receita['abr'] = 350
print(receita)

# Verificação:
print("\n# Verificação")
print('sp' in cidades)
print('mg' in cidades)
print('São Paulo' in cidades)

print(f'Sum {sum(receita.values())}')
print(f'Max {max(receita.values())}')
print(f'Min {min(receita.values())}')
print(f'Len {len(receita.values())}')


# Atualizar/Adicionar:
print("\n# Atualizar")
novoDado = {'mai': 400}
receita.update(novoDado)
# receita.update({'mai': 400})
print(receita)

receita.update({'mai': 450})
print(receita)

receita['abr'] = 900
print(receita)

# Remover dados:
print("\n# Deletar")

# Forma 1 (pop - mais comum) :
receita.pop('mai')  # Informar a chave
print(receita)

ret = receita.pop('abr')  # Retorna valor
print(receita)
print(ret)

# Forma 2 (del) :
del receita['fev']  # Não retorna valor
print(receita)


# Exemplo:
print("\n# Exemplo:")
produto1 = {'nome': 'Playstation 5','quantidade': 1,'valor': 9000.00}
produto2 = {'nome': 'Spiderman Miles Morales','quantidade': 1,'valor': 450.00}
produto3 = {'nome': 'Controle Dualsense','quantidade': 2,'valor': 500.00}

carrinho = (produto1, produto2, produto3)
print(carrinho)

valorTotal = produto1['valor'] + produto2['valor'] + produto3['valor']
print(valorTotal)

# .clear:  Limpar
print("\n# .clear:")
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

# .copy: Copiar
print("\n# .copy:")
print("Deep Copy")
d = {'a': 1, 'b': 2, 'c': 3}
novo = d.copy()
print(d)
print(novo)

novo['d'] = 4
print(novo)

print("Shallow Copy")
novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)


# .fromkey: Forma diferenciada de criação de dicionarios
print("\n# .fromkey:")
outro = {}.fromkeys('b', 'a')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['id', 'nome', 'pontos', 'email'], 'desconhecido')
print(usuario)

outro2 = {}.fromkeys('teste', 'valor')
print(outro2)

keyRange = {}.fromkeys(range(1, 11), 'int')
print(keyRange)


# .items:
print("\n# .items:")

# .popitem:
print("\n# .popitem:")

# .setdefaut:
print("\n# .setdefaut:")

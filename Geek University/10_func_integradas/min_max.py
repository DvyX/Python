"""
- Min = Minimo
- Max = Maximo
- Não tem muito segredo
"""
i = [1, 2, 3, 4, 5, 6, 7]
print(max(i))
print(min(i))

print(max(1, 10))
print(min(5, 50))

print(max('a', 'b', 'c', 'd'))
print(max('a', 'ab', 'abc'))
print(max('a', 'ab', 'abc', 'd'))
print(max('Davi Baestero'))

print(min('a', 'b', 'c', 'd'))
print(min('a', 'ab', 'abc'))
print(min('a', 'ab', 'abc', 'd'))
print(min('Davi Baestero'))

# Ordem alfabetica
nomes = ['Tim', 'Arya', 'Dora', 'Olivander', 'Samson']
print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))


musicas = [
    {'titulo': 'Sono Chi No Sadame', 'plays': 156463},
    {'titulo': 'Bloody Stream', 'plays': 100356},
    {'titulo': 'Stand Proud', 'plays': 54368},
    {'titulo': 'End Of The World', 'plays': 124395},
    {'titulo': 'Crazy Noise Bizarre Town', 'plays': 92364},
    {'titulo': 'Chase', 'plays': 26498},
    {'titulo': 'Great Days', 'plays': 84842},
    {'titulo': 'Fighting Gold', 'plays': 45274},
    {'titulo': 'Traitors Requiem', 'plays': 112084},
]

print(min(musicas, key=lambda musica: musica['plays'])['titulo'])
print(max(musicas, key=lambda musica: musica['plays'])['titulo'])

# Modo primitivo (Java):
mais = 0
musica = ''
for i in musicas:
    if i['plays'] > mais:
        mais = i['plays']
        musica = i['titulo']

print(musica)

menos = mais
for i in musicas:
    if i['plays'] < mais:
        mais = i['plays']
        musica = i['titulo']

print(musica)

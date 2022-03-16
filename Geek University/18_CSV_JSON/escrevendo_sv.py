"""
Escrevendo em arquivos CSV

writerow() - escreve uma linha
"""
"""
# writer:
from csv import writer

with open('filmes.csv', 'w') as file:
    csvreader = writer(file)
    filme = None
    csvreader.writerow(['Titulo', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme')
        if filme != 'sair':
            genero = input('Informe o gênero do filme')
            duracao = input('Informe a duração do filme (em minutos)')
            csvreader.writerow([filme, genero, duracao])
"""
# DictWriter:
from csv import DictWriter

with open('arquivos/filmes2.csv', 'w') as file:
    header = ['Titulo', 'Gênero', 'Duração']
    csvreader = DictWriter(file, fieldnames=header)
    csvreader.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme')
        if filme != 'sair':
            genero = input('Informe o gênero do filme')
            duracao = input('Informe a duração do filme (em minutos)')
            csvreader.writerow({"Titulo": filme, "Gênero": genero, "Duração": duracao})  # Mesmas chaves do cabeçalho.

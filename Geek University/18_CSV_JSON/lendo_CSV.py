"""
Lendo arquivos CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

Python possui 2 formas diferentes de ler dados em arquivos CSV:
    - reader -> Permite iterar sobre linhas do arquivo CSV como listas;
    - DictReader -> Permite iterar sobre linhas do arquivo CSV como OrderedDicts.
"""
"""
# Forma Incorreta, porém possível

with open('lutadores.csv', encoding='UTF-8') as file:
    dados = file.read()
    dados = dados.split(',')[2:]
    print(dados)
"""

# Reader:
print('\n# Reader:')

from csv import reader

with open('arquivos/lutadores.csv', encoding='UTF-8') as file:
    scanner = reader(file)
    next(scanner)
    for linha in scanner:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros')

# DictReader:
print('\n# DictReader:')

from csv import DictReader

with open('arquivos/lutadores.csv', encoding='UTF-8') as file:
    scanner = DictReader(file, delimiter=',')  # Parâmetro delimiter indica o caractere que separa os valores,
    # por padrão será vírgula
    for linha in scanner:
        # Cada linha é um OrderedDict, utilia o cabeçalho como chave
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")

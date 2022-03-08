"""
Serve para se trabalhar com um arquivo em bloco.
- Recomendado sempre se trabalhar com with ao trabalhar com arquivos.
"""
with open('arquivos_teste/arquivo1.txt', encoding='UTF-8') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)

print(arquivo.closed)

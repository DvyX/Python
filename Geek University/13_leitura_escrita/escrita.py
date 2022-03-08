"""
write() - recebe uma string para adicionar no arquivo.
- mode w = writing, escrita (O ARQUIVO SERÁ SOBRESCRITO);

OBS: O ARQUIVO SERÁ SOBRESCRITO
"""

with open('arquivos_teste/escrita.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Write 1:\n')
    arquivo.write('Mais texto ã.\n')
    arquivo.write('A' * 5000)

with open('arquivos_teste/arquivo1.txt', encoding='UTF-8') as arquivo:
    print(arquivo.read())

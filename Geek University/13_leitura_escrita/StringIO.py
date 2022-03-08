"""
Criação de arquivos em memória
"""
from io import StringIO

mensagem = 'Mensagem em memória'
arquivo = StringIO(mensagem)
print(arquivo.read())

arquivo.write('\nMais mensagem')
arquivo.seek(0)
print(arquivo.read())


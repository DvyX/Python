"""
Leitura de arquivos funciona com a função open()
https://docs.python.org/3/library/functions.html#open

- Passando somente 1 parâmetro, sendo o caminho do arquivo a ser lido, retornando um _io.TxtIOWrapper, e é com ele que
se trabalha.
- Caso o arquivo não exista, será gerado um erro 'FileNotFoundError'

mode r = reading, leitura (padrão)
"""
arquivo = open('arquivos_teste/hello_world.txt')

print(arquivo)
print(type(arquivo))
print(dir(arquivo))

print(arquivo.read())

print(arquivo.read())
# Python usa um recurso chamado "cursor", quando o .read() lê o arquivo, ele fica com o cursor no final,
# o que significa que caso peça para ler de novo, irá imprimir a partir do final do arquivo, ou seja, nada.
print(type(arquivo.read()))

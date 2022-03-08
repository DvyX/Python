"""
seek() - Usado para manipular o cursor
"""
arquivo = open('arquivos_teste/arquivo1.txt', encoding='UTF-8')
print(arquivo.read())

# Movimentar:
print("# Movimentar:")
arquivo.seek(0)  # Retornando a posição 0, inicio
print(arquivo.read())

arquivo.seek(375)
print(arquivo.read())
arquivo.seek(0)

# readline() - ler por linhas
print("# readline():")
print(arquivo.readline())  # ler a 1º linha
print(arquivo.readline())  # ler a 2º linha
print(arquivo.readline())  # ler a 3º linha
arquivo.seek(0)

ret = arquivo.readline()
print(ret)
print(type(ret))
print(ret.split(' '))

print(arquivo.readline(20))  # Quantidade de caracteres daquela linha
print(arquivo.readline())
arquivo.seek(0)

# readlines() - Tranforma cada linha em listas
print("# readlines():")
print(arquivo.readlines())
arquivo.seek(0)

linha = arquivo.readlines()
print(len(linha))

"""
Ao usar a função open() é criado uma conexão entre o programa e o disco do computador streaming. Ao finalizar os 
trabalhos, deve-se finalizar essa conexão com close(). 
"""
print("\n# close():")
print(arquivo.closed)  # Verifica se o arquivo esta fechado
arquivo.close()

# print(arquivo.read())  # Arquivo já foi finalizado, gerando ValueError.
print(arquivo.closed)

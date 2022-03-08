"""

"""
import os
import tempfile

print(os.path.exists('arquivo.txt'))
print(os.path.exists('sistemas-navegacao.py'))
print(os.path.exists('arquivos_teste\\arquivo1.txt'))

# Criando arquivos:
open('arquivos_teste\\arquivo2.txt', 'w').close()
open('arquivos_teste\\arquivo2.txt', 'a').close()

with open('arquivos_teste\\arquivo3.txt', 'w') as arquivo:
    pass

# Criar diretórios:
try:
    os.mkdir('diretorio teste')
except FileExistsError:
    print('Diretório já existe')

# Diversos diretórios:
os.makedirs('diretorio1\\diretorio2\\diretorio3', exist_ok=True)

# Renomear
try:
    os.rename('arquivos_teste\\arquivo3.txt', 'arquivos_teste\\arquivo renomeado.txt')
except FileExistsError:
    print('Arquivo já renomeado')

# Mover
try:
    os.rename('arquivos_teste\\arquivo renomeado.txt', 'diretorio teste\\arquivo renomeado.txt')
except FileExistsError:
    print('Arquivo já Movido')


# Excluir Arquivos (Não vão para a lixeira):
try:
    # os.remove('diretorio teste\\arquivo renomeado.txt')
    pass
except FileExistsError:
    print('Arquivo já Deletado')

# Excluir diretorios (É necessário estar com o diretório vazio):
try:
    os.mkdir('diretorio excluido')
except FileExistsError:
    print('Diretório já existe')

try:
    os.rmdir('diretorio excluido')
except FileExistsError:
    print('Diretório já excluido')

# Exluir diretorios completamente (com arquivos dentro)
if os.path.exists('diretorio com arquivos'):
    pass
else:
    os.mkdir('diretorio com arquivos')
    open('diretorio com arquivos\\1.txt', 'a').close()
    open('diretorio com arquivos\\2.txt', 'a').close()
    open('diretorio com arquivos\\3.txt', 'a').close()
    open('diretorio com arquivos\\4.txt', 'a').close()
    open('diretorio com arquivos\\5.txt', 'a').close()

for arquivo in os.scandir('diretorio com arquivos'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    else:
        os.rmdir('diretorio com arquivos')

# Arquivos/Diretórios temporários:
with tempfile.TemporaryDirectory() as tmp:
    print(f'Ciação do diretório temporário {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Escrita no arquivo temporário')
    # input()

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Se usa o b no comeco para escrever em binario\n')
    tmp.seek(0)
    print(tmp.read())
    print(tmp.name)
    # input()


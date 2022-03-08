"""
Sistemas de Arquivos - Manipulação

Necessário importar os
"""
import os

print("# .getcwd()")
print(os.getcwd())  # Get Current Directory

print("\n# .chdir()")
os.chdir('..')  # Navegar pelos diretorios
print(os.getcwd())
os.chdir('/')  # Raiz
print(os.getcwd())
os.chdir('C:\\Users\\davib\\PycharmProjects\\guppe')

print("\n# .path.isabs()")
print(os.path.isabs('C:\\Users\\davib\\PycharmProjects\\guppe\\'))  # Checar se o diretorio é obsoluto ou relativo
print(os.path.isabs('..\\PycharmProjects\\guppe\\'))

print("\n# .name()")
print(os.name)  # Verificar sistema operacional | posix = Mac, Linux | nt = Windows

# Navegar absolutamente
print("\n# .path.join()")
print(os.getcwd())
res = os.path.join(os.getcwd(), '13_leitura_escrita')
os.chdir(res)
print(os.getcwd())

print("\n# .listdir()")
print(os.listdir())  # Listar as coisas no diretorio
print(len(os.listdir()))  # Quantidade
print(os.listdir('C:\\Users\\davib\\PycharmProjects\\guppe\\'))

print("\n# .scandir()")
scanner = os.scandir('../13_leitura_escrita')
arquivo = list(scanner)
print(arquivo)
print(dir(arquivo[0]))

print('\nQual o inode (index node)')
print(arquivo[0].inode())
print('É diretorio?')
print(arquivo[0].is_dir())
print('É arquivo?')
print(arquivo[0].is_file())
print('É um link simbolico?')
print(arquivo[0].is_symlink())
print('Nome:')
print(arquivo[0].name)
print('Caminho do arquivo:')
print(arquivo[0].path)
print('Estatisticas do arquivo:')
print(arquivo[0].stat())

scanner.close()

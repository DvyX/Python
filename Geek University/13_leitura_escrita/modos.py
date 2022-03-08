"""
https://docs.python.org/3/library/functions.html#open
r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre exclusivamente para criação, caso exista, será gerado FileExistsError
a -> Abre para escrita - adicionando ao FINAL do arquivo caso exista
+ -> Abre para atualização (leitura e escrita) - é possivel ter o controle do cursor (em 'r' e 'w')
"""

# x:
try:
    with open('arquivos_teste/x.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo\n')
except FileExistsError:
    print('Arquivo já existe')

# a:
with open('arquivos_teste/pessoas.txt', 'a', encoding='UTF-8') as arquivo:
    while True:
        pessoa = input('Informa um nome ou sair:')
        if pessoa != 'sair':
            arquivo.write(f'-{pessoa}\n')
        else:
            break


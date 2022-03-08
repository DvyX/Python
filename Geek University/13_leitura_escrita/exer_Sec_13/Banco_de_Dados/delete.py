import os


def exclusao():
    excluir = input('Qual arquivos deseja excluir? (utilize o número com "-" para separa-los)\n[Caso deseja resetar o '
                    'banco, digite "all"]\n')
    if excluir.lower() == 'all':
        i = 0
        with open('banco/index.txt', 'w+') as index:
            index.write('0')
        with os.scandir('banco') as diretorio:
            for excluir in diretorio:
                if not excluir.name.startswith('index'):
                    os.remove(f'banco/{excluir.name}')
        print('Arquivos excluidos com sucesso')
    else:
        excluir = excluir.replace(' ', '')
        excluir = excluir.split('-')
        for n in excluir:
            try:
                with open(f'banco/arquivo_{n}.txt', 'r+') as a:
                    print(f'{a.readline(9)} excluido')
                    with open('banco/index.txt', 'r+') as index:
                        index.seek(0)
                        indexr = index.read()
                        indexr = indexr.replace(n, '')
                    with open('banco/index.txt', 'w+') as index:
                        index.write(indexr)
                os.remove(f'banco/arquivo_{n}.txt')

            except FileNotFoundError:
                print(f'Arquivo {n} não encontrado')

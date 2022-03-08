import os


def consulta():
    visualizar = input('Qual arquivos deseja visualizar? (utilize o número com "-" para separa-los)\n[Para visualizar '
                       'todos os arquivos digite "all"]\n')
    if visualizar.lower() == 'all':
        with os.scandir('banco') as diretorio:
            for arquivo in diretorio:
                if not arquivo.name.startswith('index'):
                    with open(f'banco/{arquivo.name}', 'r+') as arquivo2:
                        print(arquivo2.read())
    else:
        visualizar = visualizar.replace(' ', '')
        visualizar = visualizar.split('-')
        for n in visualizar:
            try:
                with open(f'banco/arquivo_{n}.txt', 'r+') as a:
                    print(f'{a.read()}')
            except FileNotFoundError:
                print(f'Arquivo {n} não encontrado')

"""
Criar um loop manualmente
"""


def loop_manual(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


nome = 'Davi'
loop_manual(nome)

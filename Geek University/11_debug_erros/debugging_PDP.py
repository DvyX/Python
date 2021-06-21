"""
PDP - Python Debugger;

- Selecionar os breakpoints clickando no começo da linha;
- Selecionar os Watchers quando em execução do debug, selecionando o que deseja e crickando com o botão direito;
"""


# Pycharm:

def div(a, b):
    # print(f'a={a}, b={b}')  # Não se deve usar print para debugar.
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as error:
        return f'Ocorreu um erro: {error}'


print(div(4, 0))

# PDB, manual:
'''
Comandos básicos do PDB:
- l = listar onde estamos no codigo
- n = próxima linha
- p = imprime variável
- c = continua/finaliza a execução

- Cuidado ao nomear variáveis com essas letras, assim utilizar o 'p' para mostrar as variáveis em vez dos comandos;
'''
nome = 'Davi'
sobrenome = 'Baestero'
breakpoint()  # Adciona um breakpoint na linha de baixo
nome_completo = f'{nome} {sobrenome}'
idade = 17
final = f'{nome_completo} tem {idade} anos'

print(final)


'''
# Exemplo antigo:

nome = 'Davi'
sobrenome = 'Baestero'
import pdb; pdb.set_trace()  # Adciona um breakpoint na linha de baixo
nome_completo = f'{nome} {sobrenome}'
idade = 17
final = f'{nome_completo} tem {idade} anos'

print(final)
'''
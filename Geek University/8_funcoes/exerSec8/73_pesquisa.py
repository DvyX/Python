
quantidade = 0


def leitura():
    """
    Realiza a leitura da quantidade de habitantes a serem catalogados e suas informações.
    :return: Dict dos habitantes: [caracteristicas,].
    """
    global quantidade
    quantidade = int(input('Quantos habitantes deseja catalogar?'))
    habitantes = {}
    for i in range(quantidade):
        print(f'\nHabitante {i + 1}:')
        sexo = input('Digite o sexo:').upper()
        cor_olhos = input('Digite a cor dos olhos (A-Azul/C-Castanho):').upper()
        cor_cabelo = input('Digite a cor do cabelo (L-Louros/P-Pretos/C-Castanhos):').upper()
        idade = int(input('Digite a idade:'))

        habitantes[f'Habitante {i + 1}'] = [sexo, cor_olhos, cor_cabelo, idade]

    return habitantes


def media_c_p(habitante):
    """
    Calcula a média de idade dos habitantes que possuem olhos castanhos 'C' e cabelos pretos 'P'.
    :param habitante: O dict contendo todos os habitantes.
    :return: A média de idade float ou caso não existam habitantes com essas caracteristicas, uma mensagem de erro.
    """
    contador = 0
    idade = 0
    for i in range(quantidade):
        if habitante[f'Habitante {i + 1}'][1] == 'C' and habitante[f'Habitante {i + 1}'][2] == 'P':
            contador += 1
            idade += habitante[f'Habitante {i + 1}'][3]

    if contador == 0:
        return 'Não há nenhum habitante com essas caracteristicas'

    media = idade / contador
    return media


def maior_idade(habitante):
    """
    Retorna o habitante mais velhoe a sua idade.
    :param habitante: O dict contendo todos os habitantes.
    :return: Habitante mais velho e sua idade.
    """
    maximo = 0
    mais_velho = ''
    for i in range(quantidade):
        if int(habitante[f'Habitante {i + 1}'][3]) > maximo:
            maximo = habitante[f'Habitante {i + 1}'][3]
            mais_velho = f'Habitante {i + 1}'

    return f'{mais_velho}, {maximo} anos'


def estranhamente_especifico(habitante):
    """
    Calcula a quantidade de habitantes do sexo feminino que tenham olhos azuis e cabelos louros, entre 18 e 35 anos de
    idade.
    :param habitante: O dict contendo todos os habitantes.
    :return: A quantidade de habitantes, ou caso não existam habitantes com essas caracteristicas, uma mensagem de erro.
    """
    quantos = 0
    for i in range(quantidade):
        if habitante[f'Habitante {i + 1}'][0] == 'F' and habitante[f'Habitante {i + 1}'][1] == 'A':
            if habitante[f'Habitante {i + 1}'][2] == 'L' and 17 < habitante[f'Habitante {i + 1}'][3] < 36:
                quantos += 1

    if quantos == 0:
        return 'Não há nenhum habitante com essas caracteristicas'
    return quantos


pessoas = leitura()
print(f'\nMédia da idade dos habitantes que tem olhos castanhos e cabelos pretos: {media_c_p(pessoas)}.')
print(f'Habitante mais velho: {maior_idade(pessoas)}.')
print(f'Quantidade de habitantes do sexo feminino que tem entre 18 e 35 anos e que tem olhos'
      f' azuis e cabelos louros: {estranhamente_especifico(pessoas)}.')

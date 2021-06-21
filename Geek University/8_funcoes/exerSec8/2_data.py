def leitura():
    """
    Realiza a leitura dos valores dia, mês e ano.
    :return: Uma lista com os valores de dia, mês e ano em int
    """
    txt = input('Insira a data (dd/mm/aaaa)')
    e1 = txt.find('/')
    e2 = txt.rfind('/')

    dia = txt[:e1]
    mes = txt[e1 + 1:e2]
    ano = txt[e2 + 1:]

    idia = int(dia)
    imes = int(mes)
    iano = int(ano)

    return idia, imes, iano


def verificacao_mes(int_mes):
    """
    Transforma o valor int do mês em extenço.
    :param int_mes: Valor do mês em int.
    :return: mês por extenço em string
    """
    if int_mes == 1:
        return 'Janeiro'
    elif int_mes == 2:
        return 'Fevereiro'
    elif int_mes == 3:
        return 'Março'
    elif int_mes == 4:
        return 'Abril'
    elif int_mes == 5:
        return 'Maio'
    elif int_mes == 6:
        return 'Junho'
    elif int_mes == 7:
        return 'Julho'
    elif int_mes == 8:
        return 'Agosto'
    elif int_mes == 9:
        return 'Setembro'
    elif int_mes == 10:
        return 'Outubro'
    elif int_mes == 11:
        return 'Novembro'
    elif int_mes == 12:
        return 'Dezembro'
    else:
        import sys
        sys.exit('Mês desconhecido, tente novamente')


def apresentacao(dia, emes, ano):
    """
    Apresenta o resultado.
    :param dia: Dia do mês em int.
    :param emes: Mês do ano por extenço.
    :param ano: Ano em int.
    """
    print(f'{dia} de {emes} de {ano}')


data = leitura()
txtmes = verificacao_mes(data[1])
apresentacao(data[0], txtmes, data[2])

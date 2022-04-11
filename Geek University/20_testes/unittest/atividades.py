def comer(comida, saudavel):
    if saudavel:
        return f'Comer {comida} é saudável'
    return f'Comer {comida} não é saudável'


def dormir(horas):
    if horas < 7:
        return f'{horas} horas de sono não é suficiente, recomendado são 7-9'
    elif horas > 9:
        return f'{horas} horas de sono é mais que o necessário, recomendado são 7-9'
    return f'{horas} horas de sono é o ideal'


def playstation(jogo):
    jogos = ['Crash', 'Gran Turismo', 'God of War']
    if jogo in jogos:
        return True
    return False

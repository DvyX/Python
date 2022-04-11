"""
Manipulando Data e Hora

Python tem um módulo built-in para se trabalhar com data e hora "datetime"
"""

import datetime
print(dir(datetime))

# Ano máximo e minimo para se trabalhar (MAXYYEAR - MINYEAR)
print('\n# Ano máximo e minimo para se trabalhar (MAXYYEAR - MINYEAR):')
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now())  # YYYY-MM-DD HH:MM:SS.MLLLLLL

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print('\n# datetime.datetime(year, month, day, hour, minute, second, microsecond)')
print(repr(datetime.datetime.now()))


# Alterar Horário:
print('\n# Alterar Horário replace():')
hora = datetime.datetime.now()
print(hora)
hora = hora.replace(hour=16, minute=0, second=0, microsecond=0)
print(hora)


# Criar Dada Hora:
print('\n# Criar Dada Hora:')
evento = datetime.datetime(2023, 1, 1, 0)
print(evento)


# Leitura de data:
print('\n# Leitura de data:')
data = input('Informe a data (DD/MM/AAAA):\n')
hora2 = input('Informe a hora(HH:MM:SS)')

data = data.split('/')
hora2 = hora2.split(':')

print(data)
datahora = datetime.datetime(int(data[2]), int(data[1]), int(data[0]), int(hora2[0]), int(hora2[1]), int(hora2[2]))
print(datahora)
print(type(datahora))

print(datahora.year)
print(datahora.month)
print(datahora.day)
print(datahora.hour)
print(datahora.minute)
print(datahora.second)
print(datahora.microsecond)

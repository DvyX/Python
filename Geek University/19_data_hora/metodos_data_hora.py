"""
Métodos de data e hora:

- .now() - Retorna as informações de tempo atuais (pode ser especificado fuso horário);
- .today() - Retorna as informações de tempo atuais;
- .combine() - Combina dois horários (informações de dia/mês + horário, por exemplo);
- .time() - Caso não tenha parâmetro, retorna horas, minutos e segundos como zero;
- .weekday() - Retorna o dia da semana de determinada data em int, começando com 0, sendo segunda feira;
- .strftime() - String Format Time, formata a data para um espeficicado;
- .strptime() - Formata uma string para formato de data;
- .time() - Utiliza somente o tempo;
- .timeit() - Utilizado para medir a velocidade de execução do código;
"""
import functools

"""
strftime tabela:

%a  | Abreviação do dia da semana. (Sun, Mon, ...)
%A  | Nome do dia da semana completo. (Sunday, Monday, ...)
%w  | Dia da semana como decimal. (0, 1, ..., 6)
%d  | Dia do mês com decimal preenchido com zero. (01, 02, ..., 31)
%-d	| Dia do mês como decimal. (1, 2, ..., 30)
%b  | Abreviação do nome do mês. (Jan, Feb, ..., Dec)
%B  | Nome do mês completo.	(January, February, ...)
%m  | Mês como decimal preenchido com zero.	(01, 02, ..., 12)
%-m	| Mês como número decimal. (1, 2, ..., 12)
%y  | Ano sem século como um número decimal preenchido com zeros. (00, 01, ..., 99)
%-y	| Ano sem século como número decimal. (0, 1, ..., 99)
%Y  | Ano com século como número decimal. (2013, 2019 etc.)
%H  | Hora (relógio de 24 horas) como um número decimal preenchido com zeros. (00, 01, ..., 23)
%-H | Hora (relógio de 24 horas) como um número decimal. (0, 1, ..., 23)
%I  | Hora (relógio de 12 horas) como um número decimal preenchido com zeros. (01, 02, ..., 12)
%-I | Hora (relógio de 12 horas) como um número decimal. (1, 2, ... 12)
%p  | Localidade AM ou PM. AM, PM)
%M  | Minuto como um número decimal preenchido com zeros. (00, 01, ..., 59)
%-M | Minuto como um número decimal. (0, 1, ..., 59)
%S  | Segundo como um número decimal preenchido com zeros. (00, 01, ..., 59)
%-S | Segundo como um número decimal. (0, 1, ..., 59)
%f  | Microssegundo como um número decimal, preenchido com zeros à esquerda. (000000 - 999999)
%z  | deslocamento UTC no formato +HHMM ou -HHMM.
%Z  | Nome do fuso horário.
%j  | Dia do ano como um número decimal preenchido com zeros. (001, 002, ..., 366)
%-j | Dia do ano como número decimal. (1, 2, ..., 366)
%U  | Número da semana do ano (domingo como o primeiro dia da semana). 
    | Todos os dias em um novo ano anterior ao primeiro domingo são considerados na semana (0. 00, 01, ..., 53)
%W  | Número da semana do ano (segunda-feira como o primeiro dia da semana).
    | Todos os dias em um novo ano anterior à primeira segunda-feira são considerados na semana (0. 00, 01, ..., 53)
%c  | representação de data e hora apropriada do local. (Mon Sep 30 07:06:05 2013)
%x  | Localiza a representação de data apropriada.  (09/30/13)
%X  | Localiza a representação de tempo apropriada. (07:06:05)
%%  | Literalmente um '%' caractere. (%)
"""

import datetime

# Com now() podemos especificar um fuso horário (timezone)
print('# .now():')
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

print('\n# .today():')
hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

print('\n# .combine() - .time():')
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

print('\n# .weekday()')
print(agora.weekday())

print('\n# .strftime()')
print(hoje)
hoje_format = hoje.strftime('%d/%m/%Y')
print(hoje_format)

from textblob import TextBlob  # TextBlob tem um método de tradução, já que strfformat retorna em inglês (internet)

# https://textblob.readthedocs.io/en/dev/

hoje_format2 = hoje.strftime(f"%d de {TextBlob(hoje.strftime('%B')).translate(to='pt-br')} de %Y")
print(hoje_format2)

print('\n# .strptime()')
data = '30/12/2003'
print(data)
print(type(data))

data_datetime = datetime.datetime.strptime(data, '%d/%m/%Y')
print(data_datetime)
print(type(data_datetime))

print('\n# .time()')
hora = datetime.time(9, 15, 0)
print(hora)
print(type(hora))
print(repr(hora))

print('\n# .timeit()')

import timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num * num + 4
    return soma


# functools - Utilizado para verificar funções
print(timeit.timeit(functools.partial(teste, 5), number=10000))

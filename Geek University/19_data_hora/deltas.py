"""
Trabalhando com Deltas de data e hora

delta = diferença entre uma data e outra
"""
import datetime

agora = datetime.datetime.now()

aniversario = datetime.datetime(agora.year, 2, 15)

tempo_evento = aniversario - agora

if tempo_evento.days < 0:
    aniversario = datetime.datetime(agora.year + 1, 1, 30)
    tempo_evento = aniversario - agora


print(type(tempo_evento))
print(repr(tempo_evento))
print(tempo_evento)

print(f'Faltam {tempo_evento.days} dias e {tempo_evento.seconds // 60 // 60} minutos')


print()
data_compra = datetime.datetime.now()
print(data_compra)

regra_boleto = datetime.timedelta(days=3)  # Adicionar 3 dias
print(regra_boleto)

vencimento = data_compra - regra_boleto
print(vencimento)

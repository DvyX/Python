"""
- Um parâmetro especial de funções;
- É caracterizado por *;
- Coloca os valores extras de entrada como uma tupla;
- Podem ser nomeados de qualquer forma, mas convencionalmente são nomeados com *args
- Não é obrigatório;

# Os parâmetros devem ser inseridos nessa ordem:
.Parâmetros obrigatórios;
.*args;
.Parâmetros default;
.**kwargs
"""


# Definição:
def arg(*args):
    return args


print(arg(1))
print(arg(2, 3))
print(arg(4, 'Sim', True))


def somar_todos(*args):
    return sum(args)


print(somar_todos(2, 3, 4))
print(somar_todos(1, 2, 3, 4, 5, 6, 7, 8, 9))
lista = [1, 2, 3, 4]
tupla = (1, 2, 3, 4)

# print(somar_todos(lista))  # TypeError
# print(somar_todos(tupla))  # TypeError
print(somar_todos(*lista))  # Correto
print(somar_todos(*tupla))  # Correto
# Serve para indicar uma lista de dados, o informando de deve desempacota-la;

print("\n# Exemplo:")


def string_media(nome, sobrenome='', *args):
    return nome, sobrenome, sum(args)/len(args)


print(string_media('Davi', 'Baestero', 4, 6, 8))
print(string_media('Ronaldo', '', 12, 30))

# Desempacotamento simples:


def soma3(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)  # Os nomes no dicionário devem ser os mesmos da função

soma3(*lista)
soma3(*tupla)
soma3(*conjunto)
soma3(**dicionario)

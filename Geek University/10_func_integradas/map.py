"""
- Mapeia valores para uma função, para cada iterável que é usado na função é gerado um outro iterável com os resultados;
- Como se fosse umm loop para função;
- Utilizada em IA, ciancia de dados, bio;
- Após converter map pela primeira vez, ele zera;
"""
import math


# Exemplo sem map:
def area(r):
    """
    Calucula a área de um circulo com raio 'r'
    :param r: Raio
    :return: Área do circulo
    """
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)


# Utilizando Map:
areas = map(area, raios)  # Recebe 2 valores: função, iterável
print(areas)
print(type(areas))  # Retorna um Map Object
print(list(areas))
print(list(areas))  # Após converter map pela primeira vez, ele zera

# Lambda:
print(list(map(lambda r: math.pi * (r ** 2), raios)))


cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]
print(cidades)

# Transformar em fº:
c_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_f, cidades)))


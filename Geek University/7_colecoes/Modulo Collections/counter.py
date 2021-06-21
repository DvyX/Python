"""
- Collections = High-performance Container Datetypes
- Recebe um iterável (lista, mapa) e retorna a quantidades de ocorrências de um elemento;
"""
from collections import Counter

lista = [1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 6, 6, 6, 6]

res = Counter(lista)

print(type(res))
print(res)

print(Counter('Counter de uma string'))

texto = """Meu nome é Yoshikage Kira. Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as 
moradias são, e eu não sou casado. Eu trabalho como funcionário das lojas de departamento Kame Yu, e chego em casa 
todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23h e me certifico 
de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte 
minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como 
um bebê, eu acordo sem qualquer fadiga ou estresse pela manhã. Foi-me dito que não houve problemas no meu último 
check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me 
incomodar com quaisquer inimigos, como ganhar e perder, que me faria perder o sono à noite. É assim que eu lido com a 
sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém."""

palavras = texto.split()
print(palavras)

res2 = Counter(palavras)
print(res2)

print(res2.most_common(5))  # 5 palavras com mais ocorrência
print(dir(Counter))

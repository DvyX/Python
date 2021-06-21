"""
- sort() só funciona com listas, sorted() funciona com qualquer iterável;
- Não modifica o iterável original;
- Sempre retorna uma lista independente de qual iterável foi utilizado;
"""
numeros = (4, 6, 2, 1, 8, 0)

print(numeros)
print(sorted(numeros))
print(numeros)
print(set(sorted(numeros)))  # Pode ser convertido na hora da execução.


# Parâmetros:
print(dir(sorted))
print(sorted(numeros, reverse=True))  # Decrescente.


# Exemplos:
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu amo pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'bob123', 'tweets': []},
    {'username': 'jeff', 'tweets': [], 'cor': 'verde'},
    {'username': 'doge', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje', 'Voltei']},
    {'username': "gal '-'", 'tweets': [], 'cor': 'preto', 'musica': 'rock'},
]
print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario['username']))
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']), reverse=True))


musicas = [
    {'titulo': 'Sono Chi No Sadame', 'plays': 156463},
    {'titulo': 'Bloody Stream', 'plays': 100356},
    {'titulo': 'Stand Proud', 'plays': 54368},
    {'titulo': 'End Of The World', 'plays': 124395},
    {'titulo': 'Crazy Noise Bizarre Town', 'plays': 92364},
    {'titulo': 'Chase', 'plays': 26498},
    {'titulo': 'Great Days', 'plays': 84842},
    {'titulo': 'Fighting Gold', 'plays': 45274},
    {'titulo': 'Traitors Requiem', 'plays': 112084},
]

print(sorted(musicas, key=lambda musica: musica['plays'], reverse=True))

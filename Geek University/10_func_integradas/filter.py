"""
- É um filtro, não tem muito segredo;
- Trabalha como boolean, se o valor estiver no filtro indicado, retorna True e adciona a um filter_obdject;
- Após converter map pela primeira vez, ele zera;
"""
import statistics

dados = [1.3, 2.4, 0.4, 6.3, 6.4, -4.6]

# .mean() - Média:
media = statistics.mean(dados)
print(media)

res = filter(lambda x: x > media, dados)  # Valores acima da média
print(list(res))
# print(list(res))  # Após converter map pela primeira vez, ele zera;


# Dados faltantes:
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', '', 'Equador', 'Venezuela']
print(paises)

res1 = filter(None, paises)
print(list(res1))

# Exemplo:
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu amo pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'bob123', 'tweets': []},
    {'username': 'jeff', 'tweets': []},
    {'username': 'doge', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje', 'Voltei']},
    {'username': "gal '-'", 'tweets': []},
]
print(usuarios)
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Exemplo 2: Retornar uma string f'Sua instrutora é {nome}', para cada instrutora com nome com menos de 5 caracteres
nomes = ['Vanessa', 'Ana', 'Maria']
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

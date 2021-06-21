"""
- A partir do Python3+, reduce() não é mais uma função integrada, é necessário importa-la da biblioteca 'functools';
- É mais recomendável simplismente utilizar loop for;
- É necessário receber 2 parâmetros;
- Aplica o 1 resultado da função novamente na função [funcao(funcao(a1, a2), a3), a4), ...), aN];
"""
from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 11, 15, 30]
res = reduce(lambda x, y: x * y, dados)

print(res)

# loop:
res2 = 1
for n in dados:
    res2 = n * res2

print(res2)

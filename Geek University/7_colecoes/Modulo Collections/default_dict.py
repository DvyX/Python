"""
- Baseado em Dicionarios;
- Um dicionário onde a inserção de dados é dinânica, quando se consulta um index inexistente, ele o cria com o valor
defaut;
- Serve para evitar KeyError e tratamento de erros;
- Tem as mesmas funções dos dicts;
- Lambdas são funções sem nome que podem ou não receber/retornar valores;
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 'inexisteste')

print(dicionario)
print(dir(dicionario))

dicionario['sp'] = 'São Paulo'
print(dicionario)
print(dicionario['rj'])
print(dicionario)

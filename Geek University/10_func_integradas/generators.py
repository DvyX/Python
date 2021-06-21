"""
- Basicamente Tuple Comprehension;
- Após converter map pela primeira vez, ele zera;
- Generator tem melhor performance, mais otimizado;
- É mutavel, adicionar elementos.
"""
from sys import getsizeof

nomes = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke', 'Giorno']
# List Comprehension:
res = [nome[:2] == 'Jo' for nome in nomes]
print(res)
print(type(res))

# Generator:
res2 = (nome[:2] == 'Jo' for nome in nomes)
print(res2)
print(type(res2))

# Otimização:

print(getsizeof(res))
print(getsizeof(res2))

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
gen_comp = getsizeof(x * 10 for x in range(1000))

print(f'List Comprehension: {list_comp}\nSet Comprehension: {set_comp}\nDictionary Comprehension: {dict_comp}\n'
      f'Generator Expression: {gen_comp}')

"""
- Generators são mais otimizados
"""

# Testes de velocidade:
import time

# Generator Expression:
gen_inicio = time.time()
print(sum(num for num in range(70000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension:
list_inicio = time.time()
print(sum([num for num in range(70000000)]))
list_tempo = time.time() - list_inicio


print(f'Generator Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')


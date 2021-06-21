m = 0
mp = 0
q = int(input('Digite quantos números deseja inserir: '))
for i in range(1, q + 1):
    n = int(input(f'Digite o {i}° número: '))
    if i == 1:
        min = i
        max = i
    if n < min:
        min = n
    if n > max:
        max = n
    if n % 2 == 0:
        mp += n
    m += n
s = m
m = m/q
mp = mp/q
print(f'\nForam digitados {q} números.')
print(f'Soma dos números: {s}')
print(f'Média dos números: {m}')
print(f'Média dos números pares: {mp}')
print(f'Menor número: {min}')
print(f'Maior número: {max}')

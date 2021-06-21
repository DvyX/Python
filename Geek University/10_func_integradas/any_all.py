"""
All - retorna True se todos os elementos do iterável são verdadeiros ou ainda se o tierável estiver vazio;
Any - retorna True se algum dos elementos do iterável são verdadeiro, se o iterável estiver vazio retorna False;
"""
# All:
print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, 4]))
print(all([]))


nomes = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke']
print(nomes)
print(all([nome[:2] == 'Jo' for nome in nomes]))

nomes = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke', 'Giorno']
print(nomes)
print(all([nome[:2] == 'Jo' for nome in nomes]))


print(all([letra for letra in 'aio' if letra in 'aeiou']))


# Any:
print(any([0, 1, 2, 3, 4]))
print(any([0, False, {}, (), []]))


nomes = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke']
print(nomes)
print(any([nome[:3] == 'Gio' for nome in nomes]))

nomes = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke', 'Giorno']
print(nomes)
print(any(nome[:3] == 'Gio' for nome in nomes))


print(any([num for num in [2, 4, 6, 8, 10, 11] if num % 2 == 1]))
print(any([num for num in [2, 4, 6, 8, 10] if num % 2 == 1]))

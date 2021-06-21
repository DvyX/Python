"""
- len() = Tamanho, quantidade de itens de um iterável;
- abs() = Absoluto, valor absoluto de um numero real ou inteiro, ou seja, o numero positivo;
- sum() = Soma, soma os itens de um iterável incluindo o valor inicial (default = 0);
- round() = Arredondar, numero para n digitos de precisão após a casa decimal (default = inteiro mais proximo)
"""

# len():
print('# len():')

print(len('Davi Baestero'))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd':  4, 'e': 5}))
print(len(range(0, 10)))

# Dunder len:
print('Davi Baestero'.__len__())


# abs():
print('\n# abs():')

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))


# sum():
print('\n# sum():')

print(sum([1, 2, 3, 4, 5]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))

print(sum([1, 2, 3, 4, 5], 5))
print(sum([1, 2, 3, 4, 5], -5))


# round():
print('\n# round():')

print(round(10.1))
print(round(10.5))
print(round(10.9))
print(round(3.3333333333333))
print(round(9.69696969696))
print(round(1))

print(round(79.3254732, 2))
print(round(3.14159265358979323846, 10))
print(round(1.1, 10))

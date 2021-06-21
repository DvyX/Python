#print 1.0 (ver 2.x)
""""
print("Digite seu nome:")
nome = input()

print("Seja bem vindo(a) %s " % nome)

print("Digite sua idade:")
idade = input()

print('%s tem %s anos ' % (nome, idade))

#print 2.0 (ver 3.x)

print("Digite seu nome:")
nome = input()

print("Seja bem vindo(a) {0} ".format(nome))

print("Digite sua idade:")
idade = input()

print('{0} tem {1} anos '.format(nome, idade))

"""""
#print 3.0 (ver 3.7)

print("Digite seu nome:")
nome = input()

print(f'Seja bem vindo(a) {nome}')

print("Digite sua idade:")
idade = input()

print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {2019 - int(idade)}')

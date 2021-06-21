"""
- SystaxError - Erro de Sintaxe, caso algo esteja escrito errado;
- NameError - Erro de Nome, quando algo não está definido;
- TypeError - Erro de Tipo, quando uma função/operação/ação é aplicada a um tipo errado;
- IndexError - Erro de Indice, ao tentar acessar um elemento em um indice que não existe;
- ValueError - Erro de Valor, quando uma função/operação built-in recebe um argumento com valor inapropriado;
- KeyError - Erro de Chave, ao acessar um dicionário com chave que não existe;
- AttributeError - Erro de Atributo, quando uma variável não tem atributo/função;
- IdentationError - Erro de Identação, respeite a identação!
"""

# SystaxError:
'''
def funcao:  # Parenteses.
    print('Davi')
    
def = 1

return  # Não tem o que retornar.
'''

# NameError:
'''
print(i)
funcao()  # Não estão definidos.
'''

# TypeError:
'''
print(len(5))  # len() não aceita int
print('Davi ' + 1)
'''

# IndexError:
'''
lista = ['Davi']
print(lista[1])

print('Davi'[4])
'''

# ValueError:
'''
print(int('1'))  # Correto.
print(int('Davi'))
'''

# KeyError:
'''
dic = {'Davi': 'Baestero'}
print(dic['Silva'])
'''

# AttributeError:
'''
tupla = 4, 1, 3, 2
tupla.sort()  # Tuplas não tem .sort()
print(tupla)  

lista = [4, 1, 3, 2]
lista.sort()
print(lista)  # Correto.
'''

# IdentationError:
'''
for i in range(10):
print(i)

def funcao():
 print('Davi')  # Não causa erro caso não haja 4 espaços/tab, mas é necessário ter pelo menos 1 espaço.
'''





"""
Duck Typing - Digitação Pato
"Se parece como pato, anda como pato, nada como pato é um pato"

O tipo/classe de um objeto é menos importante que os metodos que o define e ao invés de checar a classe ou o tipo de
dado é checada a presença ou não de métodos ou atributos específicos.
"""


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()
print(len(livro))

nome = 'Davi'
lista = [11, 22, 33, 44]
dicio = {'Carlos': 1, 'Marcio': 4, 'Adriana': 23}

print(len(nome))
print(len(lista))
print(len(dicio))

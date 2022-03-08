"""
Dunder Name - __name__
Dunder Main - __main__

Dunder = Double Under

Usados para criar funções, atributos, propriedades, etc para não gerar conflitos com nomes desses elementos
Em background, o Python atribuirá à variável __name__ o valor __main__ para indicar que esse é o modulo principal
"""
print(__name__)
from pacotespkg import dunder_exemplo

print(dunder_exemplo.soma_impares([1, 2, 3, 4, 5, 6]))

"""
Módulo - Arquivo simples
Pacote - Package

Em verções Python 2.x, um pacote Python deveria conter um arquivo __init__.py
Nas 3.x não é mais obrigatório, mas é uma boa norma
"""
from pacotespkg import pacote1, pacote2

print(pacote1.soma(5, 7))
print(pacote1.c)

print(pacote2.nome())

from pacotespkg.subpkg import pacote3
print(pacote3.quadrado(4))

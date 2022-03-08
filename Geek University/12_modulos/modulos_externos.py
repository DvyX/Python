"""
Gerenciador de pacotes PIP - Python Installer Package
https://pypi.org/

pip install colorama

colorama (https://pypi.org/project/colorama/) -> Usado para mudar a cor do texto no terminal
"""
from colorama import init
init()

from colorama import Fore, Back
print(Fore.RED + 'Red')
print(Fore.GREEN + 'Green')

print(Back.YELLOW, Fore.BLACK + 'Back Yellow')

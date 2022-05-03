"""
Type Hinding - Utilizado para especificar um tipo de dado predefinido.
"""


def oi(nome: str) -> str:  # Indica o valor de entrara e saida como string
    return f'Oi {nome}'


print(oi('Davi'))


# print(oi(1))  # Permite utilizar outros tipos de dados, porém avisa que não é esperado esse tipo.


def cabecalho(text: str, align: bool = True) -> str:
    if align:
        return f'{text.title()}\n{"-" * len(text)}'
    else:
        return f' {text.title()} '.center(30, '#')


print(cabecalho('Python'))
print(cabecalho('Python', False))

# Annotations:

print(cabecalho.__annotations__)

nome: str = 'Davi'
peso: float = 68.3
sim: bool = True


# print(__annotations__)


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


pessoa = Pessoa('Davi', 18, 68.3)

print(pessoa.__dict__)
# print(pessoa.__annotations__)  # Não possui annotations, somente métodos específicos
print(pessoa.andar.__annotations__)
print(pessoa.__init__.__annotations__)


# tipos em comentários (não recomendado):

def cabecalho2(text, align=True):
    # type: (str, bool) -> str
    if align:
        return f'{text.title()}\n{"-" * len(text)}'
    else:
        return f' {text.title()} '.center(30, '#')


def cabecalho3(
        text,  # type: str
        align=True  # type: bool
):  # type: (...) -> str
    if align:
        return f'{text.title()}\n{"-" * len(text)}'
    else:
        return f' {text.title()} '.center(30, '#')


from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Davi', 'Silva']
versoes: Tuple[int, int, int] = (3, 6, 9)
opcoes: Dict[str, bool] = {'ligado': True, 'desligado': False}
valores: Set[int] = {2, 4, 6, 8}

print(__annotations__)

"""
Tipos de dados mais precisos

- Literal type: Indica um valor específico de dado a ser recebido
- Union: Indica um tipo de dado específico de dado a ser recebido
- Final: Utilizado para criar constantes
- Typed dictionaries: Cria uma classe como um dicionário
- Protocols: Todos os objetos que seguirem o procoloco serão considerados partes daquele protocolo
"""

# Literal type
from typing import Literal


def pegar_status(usuario: str) -> Literal['Conectado', 'desconectado']:
    pass


def calcula(num1: int, operacao: Literal['+', '-'], num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # !r faz com que a variável fique em áspas simples


calcula(1, '+', 2)
# calcula(1, '*', 2)


# Union:
from typing import Union


def mult(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 * num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado


# Final:
from typing import Final

NOME: Final = 'Davi'
print(NOME)

from typing import final


@final  # Indica que nenhuma classe deveria extender essa
class Pessoa:
    pass


class Aluno(Pessoa):  # Errado
    pass

    @final
    def estudar(self):
        print('Estudando')


# Typed dictionaries
from typing import TypedDict


class Jogo(TypedDict):
    versao: str
    atualizacao: int


eldenring = Jogo(versao='1.0.4', atualizacao=2022)
print(eldenring)

# Protocols
from typing import Protocol


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'titulo'


v1 = Venda()

estudar(v1)

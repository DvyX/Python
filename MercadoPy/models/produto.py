from utils.helper import format_float_str_moeda


class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__cod: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def cod(self: object) -> int:
        return self.__cod

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco

    def __str__(self) -> str:
        return f'{self.cod=}\n{self.nome=}\n{format_float_str_moeda(self.preco)=}'


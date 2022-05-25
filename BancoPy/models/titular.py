from datetime import date

from utils.helper import date_str, str_date


class Titular:
    i: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nasc: str) -> None:
        self.__codigo: int = Titular.i
        self.__nome: str = nome.title()
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nasc: date = str_date(data_nasc)
        self.__data_cadastro: date = date.today()
        Titular.i += 1
    
    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nasc(self: object) -> str:
        return date_str(self.__data_nasc)

    @property
    def data_cadastro(self: object) -> str:
        return date_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f'{self.codigo=}\n{self.nome=}\n{self.email=}\n{self.cpf=}\n{self.data_nasc=}\n{self.data_cadastro=}'


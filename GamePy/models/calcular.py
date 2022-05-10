from random import randint


class Calcular:

    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @valor1.setter
    def valor1(self, value):
        self.valor1 = value

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @valor2.setter
    def valor2(self, value):
        self.valor2 = value

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Subtrair'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            raise ValueError('Operação Desconhecida')
        return f'{self.valor1=}\n{self.valor2=}\n{self.dificuldade=}\n{op=}\n{self.resultado=}'
    
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(1, 100)
        elif self.dificuldade == 3:
            return randint(1, 1000)
        raise ValueError('Dificuldade inválida, tente novamente')

    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        return self.valor1 * self.valor2

    def checar_resultado(self: object, resposta: int) -> bool:
        if resposta == self.resultado:
            return True
        return False

    def mostrar_operacao(self: object) -> None:
        if self.operacao == 1:
            print(f'{self.valor1} + {self.valor2} = ?')
        elif self.operacao == 2:
            print(f'{self.valor1} - {self.valor2} = ?')
        else:
            print(f'{self.valor1} x {self.valor2} = ?')

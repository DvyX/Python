from models.titular import Titular
from utils.helper import format_float_str_moeda


class Conta:
    codigo: int = 1001

    def __init__(self: object, titular: Titular,) -> None:
        self.__numero: int = Conta.codigo
        self.__titular: Titular = titular
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self.calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def titular(self: object) -> Titular:
        return self.__titular

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, value: float) -> None:
        self.__saldo = value

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, value: float) -> None:
        self.__limite = value

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, value: float) -> None:
        self.__saldo_total = value

    def __str__(self: object) -> str:
        return f'{self.numero=}\n{self.titular.nome=}\n{self.saldo=}\n{self.limite=}\n{self.saldo_total=}'

    @property
    def calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def sacar(self: object, valor: float) -> None:
        """
        Saca um valor monetário de conta
        :param valor: Valor em dinheiro que vai ser sacado
        """
        if 0 < valor <= self.calcula_saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saldo_total = self.calcula_saldo_total
            else:
                resto: float = self.saldo - valor
                self.limite += resto
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
            print(f'Saque de {format_float_str_moeda(valor)} realizado com sucesso\n')
        else:
            print('Saque não realizado, tente novamente\n')

    def depositar(self: object, valor: float) -> None:
        """
        Deposita um valor monetário em uma conta
        :param valor: Valor em dinheiro que vai ser depositado
        """
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self.calcula_saldo_total
            print(f'Depósito de {format_float_str_moeda(valor)} realizado com sucesso\n')
        else:
            print('Valor de depósito precisa ser maior que 0\n')

    def transferir(self: object, destino: object, valor: float) -> None:
        """
        Transfere um valor monetário de uma conta para outra
        :param destino: Conta da qual vai receber a transferência
        :param valor: Valor em dinheiro que vai ser transferido
        """
        if 0 < valor <= self.calcula_saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saldo_total = self.calcula_saldo_total
                destino.saldo += valor
                destino.saldo_total = destino.calcula_saldo_total
            else:
                resto: float = self.saldo - valor
                self.limite += resto
                self.saldo = 0
                self.saldo_total = self.calcula_saldo_total
                destino.saldo += valor
                destino.saldo_total = destino.calcula_saldo_total
            print(f'Transferência de {format_float_str_moeda(valor)} para {destino.titular.nome} realizada com sucesso\n')
        else:
            print('Saque não realizado, tente novamente\n')

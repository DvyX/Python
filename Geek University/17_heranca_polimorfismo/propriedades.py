"""
Properties - Propriedades

Getters/Setters:

    @property
    def "atributo"(self):
        return self.__"atributo"

    @"atributo".setter
    def "atributo"(self, value):
        self.__"atributo" = value

    - Usando o template "prop" ou "props"
"""


class Conta:

    i = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.i + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.i += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, value):
        self.__titular = value

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, value):
        self.__limite = value

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.saldo += valor

    @property  # Pode ser utilizado em métodos que não sejam getter/setter
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta('Marco', 3000, 5000)
conta2 = Conta('Mercules', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

print(conta1.titular)

print(conta2.__dict__)
conta2.limite = 7000
print(conta2.__dict__)

print(conta1.valor_total)  # Não faz o uso de () por ser uma propriedade

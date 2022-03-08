"""
Herança - Inheritance

A ideia de herança é de reaproveitar código e extender classes

Quando uma classe herda outra, a classe que herda (Pessoa) é conhecida como:
 - Super Classe;
 - Classe Mãe;
 - Classe Pai;
 - Classe Base;
 - Classe Genérica.

Quando uma classe herda outra, a classe herdada (Cliente, Funcionario) é conhecida como:
 - Sub Classe;
 - Classe Filha;
 - Classe Específica.

Quando uma classe herda outra, ela herda TODOS os atributos e métodos da classe herdada.


Sobrescrita de Método - Override
    Reescrever um método presenta na superclasse em classes filhas.
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def cpf(self):
        return self.__cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)  # Acessar os dados da super classe
        # Pessoa.__init__(self, nome, sobrenome, cpf)  # Não comum, porém possível
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Jail', 'Son', '123.456.789-99', 3000)
funcionario1 = Funcionario('Paulo', 'Vina', '987.654.321-00', 6547)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)


# Sobreescrita de Métodos (Overriding)

class ClienteCPF(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    def nome_completo(self):
        return f'Cliente: {self.nome} CPF: {self.cpf}'


cliente2 = ClienteCPF('Tadeo', 'Silva', '123.456.789-99', 3000)
print(cliente2.nome_completo())

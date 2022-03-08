"""
Abstração e Encapsulamento

Abstração - Expor apenas dados relevantes de uma classe.

getter e setter:
    - Getter usa a palavra reservada @property;
    - Setter usa a palavra reservada @"atributo".setter;
    - Python aplica automaticamente os metodos getters setters quando chamados em execução.
"""


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @sobrenome.setter
    def sobrenome(self, value):
        self.__sobrenome = value

    @email.setter
    def email(self, value):
        self.__email = value

    @senha.setter
    def senha(self, value):
        self.__senha = value


user = Usuario('Davi', 'Silva', 'davi.davi@gmail.com', 'senha')
print(user.__dict__)

print(user.nome)  # Automaticamente chama o getter
user.nome = 'Jailson'  # Automaticamente chama o setter
print(user.nome)

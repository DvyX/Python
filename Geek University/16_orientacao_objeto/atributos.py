"""
- Atributos -> Representam as características do objeto;

Em Python atributos são divididos em 3 grupos:
    - Atributos de Instância - Atributos declarados dentro do método construtor;

    - Atributos de Classe - Atributos declarados na diretamente na classe,
    geralmente inicializado com um valor; (conhecidos como atributos estáticos em java);

    - Atributos de Dinâmicos - Atributos de instância criado em tempo de execução,
    sendo exclusivo da instância que o criou (não é comum, mas é possível).

Públicos e Privados:
    - Em Python, por convenção, todos os atributos de uma classe são publicos;
    - Para ser declarado como privado utiliza-se __ (duplo underline).

- self é o próprio objeto, não é obrigatorio ser exatamente esse nome, mas é uma convenção;
"""


# Atributos de Instância:

# Atributos Públicos:
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


# Atributos Privados:
class ContaCorrente:
    def __init__(self, nome, desc, valor):
        self.__nome = nome
        self.__desc = desc
        self.__valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha


user = Usuario('Davi', 'davi.davi@gmail.com', 'senha')

print(user.nome)  # Atributo público permite a vizualização comum
# print(user.senha)  # Atributo privados não, AttributeError
print(user.__dict__)  # Retorna todos os valores como um dicionário

print(dir(user))

print(user._Usuario__senha)  # Garante o acesso, mas não é recomendado (Name Mangling)


# Atributos de Classe:

class Produto:
    imposto = 1.05  # 0.05% de imposto
    codigo = 0

    def __init__(self, nome, desc, valor):
        self.id = Produto.codigo + 1
        self.nome = nome
        self.desc = desc
        self.valor = (valor * Produto.imposto)
        Produto.codigo = self.id


geladeira = Produto('Geladeira', 'Eletrolux', 4500)
microondas = Produto('Microondas', 'Britânia ', 500)
lavadoura = Produto('Lava-louças', 'Electrolux ', 2500)

print(geladeira.imposto)
print(geladeira.valor)

print(Produto.imposto)  # Acesso diretamente pela classe

print(geladeira.id)
print(microondas.id)
print(lavadoura.id)


# Atributos de Dinâmicos:

geladeira.peso = 65  # Geladeira não possuia esse atributo até esse momento
lavadoura.energia = '3 kWh'

print(geladeira.peso)
print(lavadoura.energia)

# print(lavadoura.peso)  # AttributeError, não possui esse atributo

# Deletar atributos dinâmicamente
print(geladeira.__dict__)
del geladeira.peso
print(geladeira.__dict__)
del geladeira.desc
print(geladeira.__dict__)


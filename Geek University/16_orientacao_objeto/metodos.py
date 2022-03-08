"""
- Método -> São os comportamentos do objeto (funções);

Em Python atributos são divididos em 3 grupos: Instância, Classe e Estático

    - Instância: Recebe como parâmetro a instância do objeto;
    - Classe: Recebe como parâmetro a classe do objeto;
    - Estático: Não recebe parâmetro.

- dunder init (__init__) é o método construtor que serve para construir o objeto a partir de uma classe;
- Métodos dunder também são chamados de métodos mágicos;
- Não é recomendado criar métodos dunder por conta própria.
"""


# Métodos de Instância:
class Produto:
    codigo = 0

    def __init__(self, nome, desc, valor):
        self.id = Produto.codigo + 1
        self.nome = nome
        self.desc = desc
        self.valor = valor
        Produto.codigo = self.id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.valor * (100 - porcentagem)) / 100


geladeira = Produto('Geladeira', 'Eletrolux', 4500)
microondas = Produto('Microondas', 'Britânia ', 500)

print(geladeira.desconto(20))

from passlib.hash import pbkdf2_sha256 as crypto


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.sobrenome = sobrenome
        self.__email = email
        self.__senha = crypto.hash(senha, rounds=20000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.sobrenome}'

    def checa_senha(self, senha):
        if crypto.verify(senha, self.__senha):
            return True
        return False

    @property
    def get_senha(self):
        return self.__senha


"""
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma = input('Confirme a senha : ')

if senha == confirma:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user.get_senha}')
"""


# Métodos de Classe
class ContaCorrente:
    id = 0

    @classmethod
    def quantidade_contas(cls):  # Recebe cls ao invés de self como parâmetro
        print(f'Temos {cls.id} conta(s) no sistema')

    @classmethod
    def classe(cls):
        print('Métodos de Classe não interagem com os valorem ca classe')

    @classmethod
    def __classe(cls):
        print('Métodos privados também iniciam com __')

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.id + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.id = self.__numero


conta1 = ContaCorrente(6134, 134563)
conta2 = ContaCorrente(13654, 123423456)
conta3 = ContaCorrente(6143, 654671)

ContaCorrente.quantidade_contas()


# Método Estático:

class Lampada:

    @staticmethod
    def definicao():
        return 'Recipiente com líquido combustível (azeite, gasolina, petróleo, querosene etc.) e um pavio por onde é' \
               ' alimentada a chama que serve para iluminar. '

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


print(Lampada.definicao())

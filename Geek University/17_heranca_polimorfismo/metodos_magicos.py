"""
São todos os métodos que utilizam dunder - double underscore - __

dunder init -> __init__()
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    def __repr__(self):  # Representação, sobreescreve o método de representação do objeto, utilizado mais pelos devs.
        return self.__titulo

    def __str__(self):  # Mesma função do __repr__, porém tem preferência sobre __repr__ na execução.
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):  # Originalmente, Livro não tem o método len(), porém fazendo override é possível modifica-lo.
        return self.__paginas
    """
    def __del__(self):  # Quando o programa é finalizado, o Python deleta todas as variáveis, e executa o __del__
        print('Um objeto do tipo livro foi deletado da memoria')
    """
    def __add__(self, other):  # Representação de +
        return f'{self} - {other}'

    def __mul__(self, other):  # Representação de *
        if isinstance(other, int):
            msg = ''
            for i in range(other):
                msg += ' ' + str(self)
            return msg
        raise ValueError(f"'{type(other).__name__}' object cannot be interpreted as an integer")


livro1 = Livro('Python', 'Guido van Rossum', 400)
livro2 = Livro('Java', 'James Gosling', 900)

print(dir(Livro))

print('\n# __repr__ e __str__')
print(livro1)
print(livro2)

print(repr(livro1))  # Obriga a mostrar repr, desconsiderando __str__
print(str(livro2))

print('\n __len__')
print(len(livro1))  # Normalmente ocorreria TypeError, porém como foi sobreescrito, apresentará o valor configurado.

"""
print('\n __del__')
del livro2
print(livro2)
"""

print('\n __add__')
print(livro1 + livro2)

print('\n __mul__')
print(livro2 * 4)
# print(livro1 * 'a')  # ValueError

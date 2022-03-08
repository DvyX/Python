"""
Forçando tipos de dados com decoradores
"""


def forca_tipo(*tipos):
    def decorador(func):
        def converter(*args, **kwargs):
            args2 = []
            for (valor, tipo) in zip(args, tipos):
                args2.append(tipo(valor))  # Transforma o dado requisitados no tipo requisitado
            return func(*args2, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vezes in range(vezes):
        print(msg)


repete_msg('Mensagem', '3')  # Transforma o str "3" em int

"""
Checagem de tipos com Mypy - http://mypy-lang.org
"""


def cabecalho(text: str, align: bool = True) -> str:
    if align:
        return f'{text.title()}\n{"-" * len(text)}'
    else:
        return f' {text.title()} '.center(30, '#')


print(cabecalho('Mypy'))
print(cabecalho('Mypy', False))
print(cabecalho('Mypy', align='verdadeiro'))

"""
- Try/Catch em outras linguagens;
- Tratamento de erros;
- Sempre tente tratar de forma expecífica, informando o tipo do erro;

> Onde tratar um erro?
    - Toda entrada de dados deve ser tratada (a função do usuário é destruir o seu sistema);
"""
# Erro generico:
try:
    len(5)
except:
    print('Erro')

# Erro expecífico:
try:
    funcao()
except NameError:
    print('Função não definida')

try:
    len(5)
except TypeError as error:
    print(f'Erro encontrado: {error}')

num = 'nada'
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou : {num}')

# Diversos tratamentos:
try:
    len(5)
except TypeError as erroA:
    print(f'TypeError detectado: {erroA}')
except ValueError as erroB:
    print(f'ValueError detectado: {erroB}')
except:
    print(f'Erro desconhecido detectado')

try:
    len(5)
except (TypeError, ValueError) as erroC:
    print(f'Erro ({erroC}) detectado')


# Exemplo

def valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as erroK:
        return f'KeyError detectado: {erroK}'
    except TypeError as errorT:
        return f'TypeError detectado: {errorT}'


dic = {'nome': 'Davi'}

print(valor(dic, 'nome'))
print(valor(dic, 'sobrenome'))
print(valor(7, 7))


def div(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return f'Valor inválido'
    except ZeroDivisionError:
        return f'Não é possível realizar uma divisão por 0 (zero)'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(div(num1, num2))

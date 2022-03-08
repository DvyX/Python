"""
- Um parâmetro especial de funções;
- É caracterizado por **;
- Podem ser nomeados de qualquer forma, mas convencionalmente são nomeados com **kwargs;
- Diferente dos *args, o **kwargs exige que utilizemos parâmetros nomeados, e os transfoma em um dicionário;
- Não é obrigatório;

# Os parâmetros devem ser inseridos nessa ordem:
.Parâmetros obrigatórios;
.*args;
.Parâmetros default;
.**kwargs
"""
# Definição:
print("# Definição:")


def nomes_idades(**kwargs):
    return kwargs


print(nomes_idades(marco=15,  junior=6, marcio=24, antonio=69))


def nomes_idades2(**kwargs):
    for nome, idade in kwargs.items():
        print(f'{nome.title()} tem {idade} anos')


nomes_idades2(marco=15,  junior=6, marcio=24, antonio=69)


def verificacao(**kwargs):
    if 'Davi' in kwargs and kwargs['Davi'] == 'Python':
        return 'Linguagem boa'
    elif 'Davi' in kwargs and kwargs['Davi'] == 'Java':
        return 'Linguagem ruim'
    return 'Linguagem diferente'


print(verificacao())
print(verificacao(Davi='Python'))
print(verificacao(Davi='Java'))
print(verificacao(Davi='php'))

print("\n# Exemplo:")


def ordem(idade, nome, *args, vivo=True, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if vivo:
        print('Vivo')
    else:
        print('Morto')
        print(kwargs)


ordem(20, 'Roberto')
ordem(15, 'Maicon', 4, 6, 7, vivo=False, python=True)
ordem(15, 'Maicon', 'Args', vivo=True, kwargs1='Kwargs1', kwargs2='Kwargs2', numero=567)


# Desempacotar:
pessoas = {'Davi': 17, 'Roger': 22}
# print(nomes_idades2(pessoas))  #Type Error
print(nomes_idades2(**pessoas))

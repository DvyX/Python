from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import format_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    """Função Principal"""
    """
    # Produtos teste
    
    produto1: Produto = Produto('Arroz', 5.99)
    produto2: Produto = Produto('Feijão', 4.99)
    produto3: Produto = Produto('Macarrão', 7.99)
    lista: List = [produto1, produto2, produto3]
    produtos.extend(lista)
    """

    inicio()
    menu()


def inicio() -> None:
    """
    Apresenta o painel inicial
    """
    print(''.center(40, "="))
    print(' Bem-vindo(a) '.center(40, "="))
    print(' Python  Shop '.center(40, "="))
    print(''.center(40, "="))


def menu() -> None:
    """
    Apresenta o menu de opções e executa a opção selecionada
    """
    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    try:
        opcao: int = int(input())
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            comprar_produtos()
        elif opcao == 4:
            visualizar_carrinho()
        elif opcao == 5:
            fechar_pedido()
        elif opcao == 6:
            print('Volte sempre')
            sleep(2)
            exit(0)
        else:
            print('Opção desconhecida, tente novamente')
            sleep(2)
            menu()

    except ValueError:
        print(f'Valor informado não é um número, tente novamente')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    """
    Realiza o cadastro de um novo produto
    """
    print(''.center(40, '='))
    print('Cadastrar Produto:'.center(40, '='))
    print(''.center(40, '='))

    nome: str = input('Informe o nome do produto...\n')
    preco: float = float(input('Informe o preço do produto...\n'))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'Produto {produto.nome} foi cadastrado com sucesso!')

    sleep(1)
    menu()


def listar_produtos() -> None:
    """
    Lista todos os produtos registrados
    """
    print('Lista de produtos disponíveis:'.center(40, '='))
    if len(produtos) > 0:
        for produto in produtos:
            print(f'{produto.cod}-{produto.nome.title()} {format_float_str_moeda(produto.preco)}')
            sleep(1)
        print()
    else:
        print('Sem produtos registrados\n')
        sleep(1)

    sleep(1)
    menu()


def comprar_produtos() -> None:
    """
    Verifica se o produto existe, adiciona ao carrinho, caso o produto já esteja no carrinho, somente incrementea a
    quantidade
    """
    if len(produtos) > 0:
        verifica: bool = True
        nome_cod = input('Informe o nome ou código do produto...\n')
        quant: int = int(input('Informe a quantidade...\n'))

        try:
            nome_cod = int(nome_cod)
            tipo: type = type(nome_cod)
        except ValueError:
            tipo: type = type(nome_cod)

        if tipo is str:
            nome_cod = nome_cod.lower()
            for i in range(len(produtos)):
                if nome_cod == produtos[i].nome.lower():
                    verifica = False
                    if len(carrinho) > 0:
                        tem_carrinho: bool = False
                        for item in carrinho:
                            quant_varifica: int = item.get(produtos[i])
                            if quant_varifica:
                                item[produtos[i]] += quant
                                print(f'Produto {nome_cod} já está no carrinho, adicionando mais {quant} unidade(s) '
                                      f'(total: {item.get(produtos[i])})\n')
                                tem_carrinho = True
                        if not tem_carrinho:
                            item = {produtos[i]: quant}
                            carrinho.append(item)
                            print(f'Produto {nome_cod} adicionado ao carrinho!\n')
                    else:
                        item = {produtos[i]: quant}
                        carrinho.append(item)
                        print(f'Produto {nome_cod} adicionado ao carrinho!\n')
            if verifica:
                print('Produto não encontrado, tente novamente\n')

        elif tipo is int:
            produto = pegar_codigo(nome_cod)
            if produto:
                if len(carrinho) > 0:
                    tem_carrinho: bool = False
                    for item in carrinho:
                        for dados in item:
                            if dados.nome.lower() == produto.nome.lower():
                                item[produto] += quant
                                tem_carrinho = True
                                print(f'Produto {produto.nome} já está no carrinho, adicionando mais {quant} unidade(s) '
                                      f'(total: {item.get(produto)})\n')
                    if not tem_carrinho:
                        carrinho.append({produto: quant})
                        print(f'Produto {produto.nome} foi adicionado ao carrinho!')
                else:
                    carrinho.append({produto: quant})
                    print(f'Produto {produto.nome} foi adicionado ao carrinho!')
            else:
                print('Produto não encontrado, tente novamente\n')
        else:
            print('Um erro ocorreu, tente novamente\n')

    else:
        print(f'Ainda não existem produtos registrados\n')
    sleep(1)
    menu()


def visualizar_carrinho() -> None:
    """
    Lista todos os itens no carrinho
    """
    print(' Carrinho: '.center(40, '='))
    if len(carrinho) > 0:
        for produto in carrinho:
            for dados in produto.items():
                print(f'-X{dados[1]} {dados[0].nome} {format_float_str_moeda(dados[0].preco)}')
        print()
    else:
        print('Sem produtos no carrinho')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    """
    Finaliza o pedido, apresentando o valor total e encerrando o programa
    """
    if len(carrinho) > 0:
        print(' Conta: '.center(40, '='))
        total: float = 0
        for produto in carrinho:
            for dados in produto.items():
                print(f'-X{dados[1]} {dados[0].nome} {format_float_str_moeda(dados[0].preco)}')
                total += dados[0].preco * dados[1]

        print(''.center(40, '='))
        print(f'Valor total: {format_float_str_moeda(total)}')
        sleep(1)
        print(f'Volte sempre!')
        carrinho.clear()
        exit(1)
    else:
        print('Sem produtos no carrinho.\n')
        sleep(2)
        menu()


def pegar_codigo(codigo: int) -> Produto:
    """
    Seleciona um produto pelo seu código
    :param codigo: Código do produto
    :return: Produto do qual o código foi informado
    """
    p = None

    for produto in produtos:
        if produto.cod == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()

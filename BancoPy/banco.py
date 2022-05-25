from datetime import date
from time import sleep
from typing import List

from models.conta import Conta
from models.titular import Titular
from utils.helper import format_float_str_moeda

contas: List[Conta] = []


def main() -> None:
    """Função Principal"""
    """
    # Titulares teste
    
    conta1: Conta = Conta(Titular('Dante', 'dante@gmail.com', '105.078.890-70', '12/12/1992'))
    conta2: Conta = Conta(Titular('Vergil', 'vergil@gmail.com', '936.926.725-17', '06/06/1992'))
    conta3: Conta = Conta(Titular('Nero', 'nero@gmail.com', '543.123.654-12', '03/03/2003'))

    conta_lista: List[Conta] = [conta1, conta2, conta3]
    contas.extend(conta_lista)
    """

    inicio()
    menu()


def inicio() -> None:
    """
    Apresenta o painel inicial
    """
    print(''.center(40, "="))
    print(f' ATM {date.today()} '.center(40, "-"))
    print(' Python Bank '.center(40, "-"))
    print(''.center(40, "="))


def menu() -> None:
    """
    Apresenta o menu de opções e executa a opção selecionada
    """
    print('Selecione uma opção abaixo:')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Deposito')
    print('4 - Efetuar Transferêcia')
    print('5 - Listar Contas')
    print('6 - Sair do sistema')

    try:
        opcao: int = int(input())
        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            efetuar_saque()
        elif opcao == 3:
            efetuar_deposito()
        elif opcao == 4:
            efetuar_transferencia()
        elif opcao == 5:
            listar_contas()
        elif opcao == 6:
            print('Obrigado pela Preferência.')
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


def criar_conta() -> None:
    """
    Realiza o cdastro de uma nova conta
    """
    print('Informe os dados do titular:'.center(40, '.'))
    nome: str = input('Nome do titular:\n')
    email: str = input('Email do titular:\n')
    cpf: str = input('CPF do titular:\n')
    nasc: str = input('Informe a data de nascimento do titular (dd/mm/AAAA):\n')

    titular: Titular = Titular(nome, email, cpf, nasc)
    conta: Conta = Conta(titular)

    contas.append(conta)
    print('Cadastro realizado com sucesso!')
    sleep(2)
    menu()


def efetuar_saque() -> None:
    """Verifica e executa a função conta.sacar()"""
    if len(contas) > 0:
        try:
            numero: int = int(input('Informe o número da conta...\n'))
            conta: Conta = buscar_conta_numero(numero)
            if conta:
                print(f'{conta.numero} - {conta.titular.nome} ({conta.titular.email}): Saldo Total = '
                      f'{format_float_str_moeda(conta.calcula_saldo_total)}')
                sleep(1)
                valor: float = float(input('Informe o valor que deseja sacar...\n'))
                conta.sacar(valor)
            else:
                print(f'Conta {numero} não encontrada, tente novamente\n')
        except ValueError:
            print('Valor informado não é um número, tente novamente\n')
    else:
        sleep(1)
        print('Sem contas registradas\n')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    """Verifica e executa a função conta.depositar()"""
    if len(contas) > 0:
        try:
            numero: int = int(input('Informe o número da conta...\n'))
            conta: Conta = buscar_conta_numero(numero)
            if conta:
                print(f'{conta.numero} - {conta.titular.nome} ({conta.titular.email}): Saldo Total = '
                      f'{format_float_str_moeda(conta.calcula_saldo_total)}')
                sleep(1)
                valor: float = float(input('Informe o valor que deseja depositar...\n'))
                conta.depositar(valor)
            else:
                print(f'Conta {numero} não encontrada, tente novamente\n')
        except ValueError:
            print('Valor informado não é um número, tente novamente\n')
    else:
        sleep(1)
        print('Sem contas registradas\n')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    """Verifica e executa a função conta.transferir()"""
    if len(contas) > 0:
        try:
            numero_o: int = int(input('Informe o número da conta de origem...\n'))
            origem: Conta = buscar_conta_numero(numero_o)
            if origem:
                print(f'{origem.numero} - {origem.titular.nome} ({origem.titular.email}): Saldo Total = '
                      f'{origem.calcula_saldo_total}')
                sleep(1)
                numero_d: int = int(input('Informe o número da conta de destino...\n'))
                destino: Conta = buscar_conta_numero(numero_d)
                if destino:
                    print(f'{destino.numero} - {destino.titular.nome} ({origem.titular.email}): Saldo Total = '
                          f'{destino.calcula_saldo_total}')
                    sleep(1)
                    valor: float = float(input('Informe o valor a ser transferido...\n'))
                    origem.transferir(destino, valor)
                else:
                    print(f'Conta {numero_d} não encontrada, tente novamente\n')
            else:
                print(f'Conta {numero_o} não encontrada, tente novamente\n')
        except ValueError:
            print('Valor informado não é um número, tente novamente\n')
    else:
        sleep(1)
        print('Sem contas registradas\n')
    sleep(2)
    menu()


def listar_contas() -> None:
    """
    Lista todas as contas registradas
    """
    print('Contas Registradas:'.center(40, '-'))
    if len(contas) > 0:
        for conta in contas:
            print(f'{conta.numero} - {conta.titular.nome} ({conta.titular.email}): Saldo Total = '
                  f'{format_float_str_moeda(conta.calcula_saldo_total)}')
            sleep(1)
    else:
        sleep(1)
        print('Sem contas registradas')
        sleep(2)
    print()
    menu()


def buscar_conta_numero(numero: int) -> Conta:
    """
    Seleciona uma conta pelo seu número
    :param numero: Número da conta
    :return: Conta do qual o número foi informado
    """
    c = None

    for conta in contas:
        if conta.numero == numero:
            c = conta
    return c


if __name__ == '__main__':
    main()

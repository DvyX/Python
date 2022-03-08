from insert import insercao
from consulta import consulta
from delete import exclusao

menu = input('1-Cadastro\n2-Consulta\n3-Excluir\n')

while True:
    if menu == '1':
        insercao()
        break
    elif menu == '2':
        consulta()
        break
    elif menu == '3':
        exclusao()
        break
    else:
        print('Opção Inválida, tente novamente')

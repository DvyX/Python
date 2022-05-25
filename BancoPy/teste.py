from models.titular import Titular
from models.conta import Conta

dante: Titular = Titular('Dante', 'dante@gmail.com', '105.078.890-70', '12/12/1992')
vergil: Titular = Titular('Vergil', 'vergil@gmail.com', '936.926.725-17', '06/06/1992')

print('# Clientes')
print(dante)
print(vergil)


conta_d: Conta = Conta(dante)
conta_v: Conta = Conta(vergil)

print('\n# Contas')
print(conta_d)
print(conta_v)

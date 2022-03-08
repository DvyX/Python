

def soma_impares(n):
    total = 0
    for num in n:
        if num % 2 != 0:
            total += num
    return total


# Sem essa verificação a importação irá executar esse comando toda vez que for importada;
# Só sendo executado quando esse arquivo for o principal
if __name__ == '__main__':
    print("Erro com dunder")

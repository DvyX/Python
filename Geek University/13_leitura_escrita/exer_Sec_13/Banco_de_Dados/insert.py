def insercao():
    with open('banco/index.txt', 'a+') as index:
        index.seek(0)
        i = len(index.read())
        if i / 2 != 0:
            i = i - 1
            i = i / 2
            i = int(i)
        else:
            i = i / 2
            i = int(i)

        while True:
            i += 1
            copiar = index.read()
            index.write(f'{copiar}\n{i}')

            nome = input('Digite seu nome completo:')
            idade = input('Digite sua idade:')
            email = input('Digite seu email:')
            cpf = input('Digite seu cpf:')

            with open(f'banco/arquivo_{i}.txt', 'w', encoding='UTF-8') as arquivo:
                arquivo.write(f'Arquivo {i}\nNome: {nome}\nIdade: {idade}\nEmail: {email}\nCPF: {cpf}\n')

            r = input('Deseja continuar? (sim / não)')
            r.lower()
            if r == 'não':
                break

"""
Desenvolva uma classe Televisão e uma classe ControleRemoto que podem controlar o volume e trocar os canais da televisão

- O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez, no intervalo
 de 0 a 50.
- O controle de canal permite aumentar ou diminuir o número do canal em uma unidade, porém, também possibilita trocar
para um canal específico, no intervalo de 1 a 500.
- Os canais disponíveis são apenas os canais cujos números sejam divisíveis por 3 ou por 5. Caso o usuário selecione um
canal inválido, a Televisão deverá selecionar o próximo canal válido.
"""


class Televisao:

    def __init__(self, canal=1, volume=0):
        self.__canal = canal
        self.__volume = volume

    @property
    def canal(self):
        return self.__canal

    @property
    def volume(self):
        return self.__volume

    @canal.setter
    def canal(self, value):
        self.__canal = value

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def informacao(self):
        """Apresenta as informações de canal e volume da televisão"""
        print(f'Televisão está no canal {self.__canal} com {self.__volume} de volume')


class ControleRemoto:

    def __init__(self, televisao):
        self.__televisao = televisao

    @property
    def televisao(self):
        return self.__televisao

    @televisao.setter
    def televisao(self, value):
        self.__televisao = value

    def aumentar_volume(self):
        """Aumenta o volume da televisão de 1 em 1."""
        if self.__televisao.volume > 49:
            print('Volume mínimo (0)')
        else:
            self.__televisao.volume += 1

    def diminuir_volume(self):
        """Diminui o volume da televisão de 1 em 1."""
        if self.__televisao.volume < 1:
            print('Volume mínimo (0)')
        else:
            self.__televisao.volume -= 1

    def proximo_canal(self):
        """Aumenta o canal da televisão para o próximo multiplo de 3 ou 5."""
        if self.__televisao.canal > 499:
            self.__televisao.canal = 1
        else:
            if self.__televisao.canal == 1:
                self.__televisao.canal = 3
            else:
                i = 1
                while i in range(6):
                    if (self.__televisao.canal + i) % 3 == 0 or (self.__televisao.canal + i) % 5 == 0:
                        self.__televisao.canal += i
                        break
                    i += 1

    def anterior_canal(self):
        """Diminui o canal da televisão para o multiplo de 3 ou 5 anterior."""
        if self.__televisao.canal == 3:
            self.__televisao.canal = 1
        else:
            i = 1
            while i in range(6):
                if (self.__televisao.canal - i) % 3 == 0 or (self.__televisao.canal - i) % 5 == 0:
                    self.__televisao.canal -= i
                    break
                i += 1
            if self.__televisao.canal < 1:
                self.__televisao.canal = 500

    def selecionar_canal(self, canal):
        """Seleciona um canal específico na televisão, no caso de um canal inválido, selecionará o próximo canal válido.
        :param canal: Número do canal desejado
        :return: Retorna True se o canal selecionado não existir"""
        if 500 > canal > 0:
            if canal % 3 == 0 or canal % 5 == 0:
                self.__televisao.canal = canal
                return False
            else:
                i = 1
                while i in range(6):
                    if (canal + i) % 3 == 0 or (canal + i) % 5 == 0:
                        self.__televisao.canal = canal + i
                        break
                    i += 1
                return True
        else:
            print('Canal inválido...')

    @staticmethod
    def desligar():
        """Encerra o processo"""
        exit(1)

    @staticmethod
    def ajuda():
        """Apresenta todos os comandos disponíveis"""
        print('"Info" - Mostra as informações de canal e volume atuais\n'
              '"Aumentar" - Aumenta o volume da televisão em 1\n'
              '"Diminuir" - Diminui o volume da televisão em 1\n'
              '"Próximo" - Seleciona o próximo canal disponível\n'
              '"Anterior" - Seleciona o canal anterior disponível\n'
              '"Selecionar" - Seleciona um canal específico\n'
              '"Desligar" - Encerra o processo\n'
              '"Help" - Mostra os comandos disponíveis')


tv = Televisao()
controle = ControleRemoto(tv)

controle.selecionar_canal(678)
controle.selecionar_canal(378)
controle.selecionar_canal(-678)
tv.informacao()
controle.ajuda()

while True:
    x = input('...')
    x.lower()
    if x == 'info':
        print(tv.informacao())
    elif x == 'aumentar':
        controle.aumentar_volume()
        print(f'Volume: {tv.volume}')
    elif x == 'diminuir':
        controle.diminuir_volume()
        print(f'Volume: {tv.volume}')
    elif x == 'proximo' or x == 'próximo':
        controle.proximo_canal()
        print(f'Canal: {tv.canal}')
    elif x == 'anterior':
        controle.anterior_canal()
        print(f'Canal: {tv.canal}')
    elif x == 'selecionar':
        y = input('Selecione o canal:')
        try:
            y = int(y)
            if controle.selecionar_canal(y):
                print(f'Canal selecionado não existe, selecionando o próximo ({tv.canal})')

        except ValueError:
            print('Valor informado precisa ser um número...')
    elif x == 'help' or x == 'ajuda' or x == 'ajudar':
        controle.ajuda()
    elif x == 'desligar':
        controle.desligar()
    else:
        print('Comando desconhecido, tente novamente')


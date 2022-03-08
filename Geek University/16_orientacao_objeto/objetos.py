"""
- Objeto -> Instância da classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade, ligada=False):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = ligada

    @property
    def get_cor(self):
        return self.__cor

    def checar(self):
        return self.__ligada

    def on_off(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


vermelha = Lampada('Vermelho', 110, 70)  # Este é o objeto/instância

print(f'Lâmpada {vermelha.get_cor} está ligada? {vermelha.checar()}')
vermelha.on_off()
print(f'Lâmpada {vermelha.get_cor} está ligada? {vermelha.checar()}')


azul = Lampada('Azul', 220, 110, True)
print(f'Lâmpada {azul.get_cor} está ligada? {azul.checar()}')


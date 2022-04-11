import unittest

from atividades import comer, dormir, playstation


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('tomate', True),
            'Comer tomate é saudável'
        )

    def test_comer_nsaudavel(self):
        """Testando o retorno com comida não saudável"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Comer pizza não é saudável'
        )

    def test_dormir_pouco(self):
        """Testando o retorno com poucas horas de sono"""
        self.assertEqual(
            dormir(5),
            '5 horas de sono não é suficiente, recomendado são 7-9'
        )

    def test_dormir_muito(self):
        """Testando o retorno com muitas horas de sono"""
        self.assertEqual(
            dormir(12),
            '12 horas de sono é mais que o necessário, recomendado são 7-9'
        )

    def test_dormir_ideal(self):
        """Testando o retorno com horas ideais de sono"""
        self.assertEqual(
            dormir(8),
            '8 horas de sono é o ideal'
        )

    def test_playstation_exclusivo(self):
        """Testando o retorno de um jogo exclusivo playstation"""
        self.assertTrue(playstation('God of War'), True)

    def test_playstation_xbox(self):
        """Testando o retorno de um jogo exclusivo xbox"""
        self.assertFalse(playstation('Forza'), False)


if __name__ == '__main__':
    unittest.main()

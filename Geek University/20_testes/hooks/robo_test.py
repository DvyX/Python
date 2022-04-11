import unittest

from robo import Robo


class RoboTests(unittest.TestCase):

    def setUp(self):
        self.yorha = Robo('2B', bateria=50)
        # print('setUp() executado')

    def test_carregar(self):
        self.yorha.carregar()
        self.assertEqual(self.yorha.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.yorha.dizer_nome(), 'Unidade 2B se apresentando.')
        self.assertEqual(self.yorha.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self):
        # print('tearDown() executado')
        pass


if __name__ == '__main__':
    unittest.main()

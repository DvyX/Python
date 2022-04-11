"""
Unittests - Antes e Após Hooks

Hooks são os testes em si, a execução dos testes.

setup() - Executado antes de cada método de teste. Utilizado para criar instâncias de objetos ou outros tipos de dados;
teardown() - Executado depois de cada método de teste. Utilizado apara excluir dados ou fechar conexões com DB;
"""
import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setup()
        pass

    def test_primeiro(self):
        # setup() sempre é rodado antes de um teste
        # teardown sempre é rodado após um teste
        pass

    def tearDown(self):
        # Configuração do teardown()
        pass

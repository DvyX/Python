"""
Unittest - Testes Unitários

Habilidade de testar unidades individuais de código fonte.
Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

Para criar os testes, cria-se classes que herdam de unittest.TestCase, e então se ganha todos os assertions presentes no
módulo.

Por convenção, todos os testes em um test case devem ser iniciados com 'test_'.

Para executar o teste com mais informações, no modo verbose se usa -v no console.

Recomendado utilizar docstrings nos testes.
"""
"""
|         Método            |      Verifica se       |
----------------------------|------------------------|
assertEqual(a, b)           | a == b                 |
assertNotEqual(a, b)        | a != b                 |
assertTrue(x)               | x é Verdadeiro         |
assertFalse(x)              | x é Falso              |
assertIs(a, b)              | a é b                  |
assertIsNot(a, b)           | a não é  b             |
assertIsNone(x)             | x é None               |
assertIsNotNone(x)          | x não é None           |
assertIn(a, b)              | a está b               |
assertNotIn(a, b)           | a não está b           |
assertIsInstance(a, b)      | a é instância de b     |
assertNotIsInstance(a, b)   | a não é instância de b |

https://docs.python.org/3/library/unittest.html
"""
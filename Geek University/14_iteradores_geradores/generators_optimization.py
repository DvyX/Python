"""
- Generators são mais otimizados
"""


# Teste com listas (464MB):
def fib_list(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


"""
for n in fib_list(100000):
    print(n)
"""


# Teste com generators (2,9MB):
def fib_gen(maximo):
    a, b, i = 0, 1, 0
    while i < maximo:
        a, b = b, a + b
        yield a
        i += 1


"""
for n in fib_gen(100000):
    print(n)
"""
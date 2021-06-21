"""
- Uma lista de alta performance
"""
from collections import deque

deq = deque('deque')
print(deq)
print(dir(deq))

deq.append('x')  # Adciona no final
print(deq)

deq.appendleft('y')  # Adiciona no começo
print(deq)

print(deq.pop())  # Remove e retorna o último elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)

deq.extend(['x', 'y', 'z'])
print(deq)

deq.extendleft(['a', 'b', 'c'])
print(deq)

# Inteiro:
integer = 1000000
print(integer)
#      =
integer = 1_000_000
print(integer)

# Float / Double:
x = 3.45
y = 5j
print(x)
print(int(x))
print(type(x))
print(y)
print(type(y))

# Boolean:
true = True
false = False

print(true)
print(not true)
print(false)
print(not false)

true or false
true and false

# String:
s = 'Davy'
s = "Davy"
s = '''Davy'''
s = """Davy"""
print(s)

s = 'Davy\'s Bar'
print(s)

print(s.upper())
print(s.lower())
print(s.replace('a', 'e'))
print(s.strip())  # Retira os espaços no inicio e final

print(s[0:4])
print(s[7:])
print(s[::2])
print(s[::-1])
# [inicio:fim:passo]

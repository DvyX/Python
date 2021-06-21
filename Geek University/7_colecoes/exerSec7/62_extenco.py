
c = 0
n = list(input('números:'))
for i in n:
    if i == '1':
        c += 2
    elif i == '2':
        c += 4
    elif i == '3':
        c += 4
    elif i == '4':
        c += 6
    elif i == '5':
        c += 5
    elif i in range(6, 10):
        c += 4
    print(c)

print(c)



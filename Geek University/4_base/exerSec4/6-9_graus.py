print("Selecione qual operação deseja fazer:\n1-Celcius = Fahrenheit | 2-Celcius = Kelvin")
print("3-Fahrenheit = Celcius | 4-Fahrenheit = Kelvin\n5-Kelvin = Celcius | 6-Kelvin = Fahrenheit")
e = int(input())

if e == 1:
    t = float(input("Digite a temperatura em Celcius:"))
    r = float(t*(9/5)+32)
    print(f'{r}F°'[:6])
elif e == 2:
    t = float(input("Digite a temperatura em Celcius:"))
    r = float(t+273.15)
    print(f'{r}K°'[:6])
elif e == 3:
    t = float(input("Digite a temperatura em Fahrenheit:"))
    r = float(5*(t-32)/9)
    print(f'{r}C°'[:6])
elif e == 4:
    t = float(input("Digite a temperatura em Fahrenheit:"))
    r = float((t-32)/1.8+273.15)
    print(f'{r}K°'[:6])
elif e == 5:
    t = float(input("Digite a temperatura em Kelvin:"))
    r = float(t-273.15)
    print(f'{r}C°'[:6])
elif e == 6:
    t = float(input("Digite a temperatura em Kelvin:"))
    r = float((t-273.15)*9/5+32)
    print(f'{r}F°'[:6])
else:
    print("Opção inválida")

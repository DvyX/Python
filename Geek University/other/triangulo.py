ab = 8
bc = 8
ca = 8

if ab == bc and ab == ca:
    triangulo = 'Equilatero'
    path = './images/equilatero.png'
elif ab == bc or bc == ca or ca == ab:
    triangulo = 'Isosceles'
    path = './images/isosceles.png'
else:
    triangulo = 'Escaleno'
    path = './images/escaleno.jpg'

print(f'Este é um triangulo {triangulo}')
print(f'{path} é o path da imagem')

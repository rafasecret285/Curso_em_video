x = float(input('Insira a medida do primeiro lado do triângulo:'))
y = float(input('Insira a medida do segundo lado do triângulo:'))
z = float(input('Insira a medida do terceiro lado do triângulo'))

if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print('O triângulo é equilátero.')
    elif x != y != z != x:
        print('O triângulo é escaleno.')
    else:
        print('O triângulo é isóceles.')
else:
    print('O triângulo não pode existir')


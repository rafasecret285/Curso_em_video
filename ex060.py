x = int(input('Digite um número para calcular sua fatorial:'))
cont = x
soma = 1
print('Calculando {}!...'.format(x))
while cont > 0:
    print('{} '.format(cont),end='')
    print('x 'if cont > 1 else '= ',end='')
    soma = soma * cont
    cont -= 1
print(soma)





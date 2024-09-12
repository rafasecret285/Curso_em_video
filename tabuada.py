x = int(input('Insira um número:'))
cont = 1

while cont <= 10:
    resultado = x * cont
    print('{}x{}={}'.format(x,cont,resultado))
    cont = cont + 1

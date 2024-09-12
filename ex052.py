n = int(input('Digite um número:'))
cont = 1
print('\033[31m1 ',end='')
primo = 0
for c in range(2,n):
    cont = cont + 1
    if n % cont == 0:
        print('\033[31m{} \033[m'.format(cont),end='')
        primo = 1
    else:
        print('\033[000m{}\033[m '.format(cont),end='')
print('\033[31m{}\033[m'.format(n))
if primo > 0:
    print('O NÚMERO {} NÃO É PRIMO!'.format(n))
else:
    print('O NÚMERO {} É PRIMO'.format(n))






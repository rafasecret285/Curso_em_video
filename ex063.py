print('''{}
SEQUÊNCIA DE FIBONACCI
{}'''.format('-'*25,'-'*25))

far = int(input('Quantos termos você quer mostrar?'))

cont = 2
t1 = 0
t2 = 1
print('0 --> 1 ',end='')

while cont < far:
    t3 = t1 + t2
    print('--> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' --> FIM')





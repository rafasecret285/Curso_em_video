x = float(input('Qual o seu salário?:R$'))

if x <= 1250:
    print('Agora o seu salário é de {}'.format(x + (x/100*15)))
else:
    print('Agora o seu salário é de {}'.format(x + (x/100*10)))
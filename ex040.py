n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))

media = (n1 + n2) / 2

if media >= 7:
    print('Sua média é {:.2f}, você foi aprovado'.format(media))
elif media < 7 and media >= 5:
    print('Sua média é {:.2f}, você está de recuperação'.format(media))
else:
    print('Sua média é {:.2f}, você foi reprovado!'.format(media))


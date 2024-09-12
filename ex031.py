x = float(input('Qual é a distância de sua viagem em km?:'))

if x <= 200:
    print('O preço de sua viagem é {:.2f}R$'.format(x * 0.5))
else:
    print('O preço de sua viagem é {:.2f}R$'.format(x * 0.45))
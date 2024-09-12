from random import randint

certo = randint(1,10)
tentativas = 0
palpite = 0

print('''Sou seu computador...
Acabei de pensar em um número de 0 a 10
Será que você consegue adivinhar?''')


while palpite != certo:
    palpite = int(input('Qual é seu palpite?:'))
    tentativas += 1
    if palpite != certo and palpite < 11 and palpite > 0:
        if palpite > certo:
            print('Menos...',end='')
        else:
            print('Mais...',end='')
    elif palpite == certo:
        print('Acertou com {} tentativas, parabéns!'.format(tentativas))
    elif palpite > 10 or palpite < 1:
        print('Você não tentou um número entre 1 e 10')


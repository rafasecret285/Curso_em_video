#PEDRA PAPEL TESOURA
from random import choice
from time import sleep
lista = ['pedra','papel','tesoura']

player = input('Escolha pedra, papel ou tesoura:').lower().strip()
pc = choice(lista)

if player in lista:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)

    if player == 'pedra' and pc == 'tesoura' or player == 'papel' and pc == 'pedra' or player == 'tesoura' and pc == 'papel':
        print('=-'*15)
        print('Você venceu!')
        print('O computador escolheu {}'.format(pc))
        print('-=' * 15)
    elif pc == 'pedra' and player == 'tesoura' or pc == 'papel' and player == 'pedra' or pc == 'tesoura' and player == 'papel':
        print('-=' * 15)
        print('Você perdeu!')
        print('O computador escolheu {}'.format(pc))
        print('=-' * 15)
    elif player == pc:
        print('=-' * 15)
        print('Empate')
        print('O computador escolheu {}'.format(pc))
        print('=-' * 15)
else:
    print('Código inválido')


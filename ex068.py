from random import randint
v = 0
win = True

print(' {}\n'.format('=-'*20),'VAMOS JOGAR PAR OU ÍMPAR\n','{}'.format('=-'*20))
while win == True:
    print('{}'.format('-'*37))

    tipo = str(input('Par ou Ímpar? [P/I]:')).upper().strip()[0]
    jogador = int(input('Escolha um número:'))
    computador = randint(1,10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}')
    print('Deu impar!'if total % 2 == 1 else 'Deu par!')

    #sistema de vitórias ou derrotas
    if total % 2 == 0 and tipo == 'P' or total % 2 == 1 and tipo == 'I':
        print('Você VENCEU! Vamos jogar novamente...')
        v = v + 1
    elif total % 2 == 0 and tipo == 'I' or total % 2 == 1 and tipo == 'P':
        print('GAME OVER!')
        win = False
print(f'Você venceu {v} vez(es)')
print('{}'.format('-'*37))

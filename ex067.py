while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? (Digite -1 para parar):'))
    if tabuada < 0:
        break
    print('{}'.format('=' * 30))
    for c in range (1,11):
        print(f'{tabuada} x {c} = {tabuada * c}')
    print('{}'.format('=' * 30))
print('PROGRAMA DE TABUADA ENCERRADO, VOLTE SEMPRE!')


termo1 = int(input('Digite um termo:'))
razao = int(input('Digite a razao:'))

cont =1
mostra = termo1
quantidade = 0

while cont <= 10:
    print('{} --> '.format(mostra),end = '')
    cont = cont + 1
    mostra = mostra + razao
    quantidade = quantidade + 1

print('PAUSA')
cont= 1
far = 1
while far != 0:

    far = int(input('Quantos termos você quer mostrar a mais?:'))
    if far == 0:
        print('Progressão finalizada com {} termos!'.format(quantidade))
    else:
        while cont <= far:
            print('{} --> '.format(mostra),end='')
            mostra = mostra + razao
            cont = cont + 1
            quantidade = quantidade + 1
    print('PAUSA'if far != 0 else 'FIM')

    cont = 1




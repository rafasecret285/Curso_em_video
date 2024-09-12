termo = int(input('Digite um termo:'))
razao =  int(input('Digite a razão de PA:'))
cont = 1
mostra = termo

while cont < 11:
    print('{} --> '.format(mostra),end = '')
    mostra = mostra + razao
    cont = cont + 1
print('FIM')


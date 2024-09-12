soma = 0
menosde20=0
homemmaisvelho = ''
idademaisvelho = 0


for cont in range(1,5):
    print('{}{}a PESSOA{}'.format('='*4,cont,'='*4))
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('Sexo[M/F]:').lower()
    if sexo == 'f':
        if idade < 20:
            menosde20 = menosde20 + 1
    soma += idade
    if sexo == 'm':
        if idade > idademaisvelho:
            homemmaisvelho = nome


print('''São {} mulheres com menos de 20 anos
A média de idade dos integrantes é de {}
O homem mais velho se chama {}'''.format(menosde20,soma/4,homemmaisvelho))

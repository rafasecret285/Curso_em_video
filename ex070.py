print(' {}\n'.format('-'* 18),'LOJA SUPER BARATÃO\n','{}'.format('-'*18))
resposta = 'S'
total = 0
mais1000 = 0
maisbaratonome = ''
maisbaratopreço = 0
cont = 0
while resposta == 'S':
    cont = cont + 1
    nome = input('Digite o nome do produto:')
    preço = float(input('Digite seu preço:R$'))
    resposta = input('Deseja continuar? [S/N]:').upper().strip()[0]
    print('{}'.format('-'*30))
    total = total + preço
    if preço > 1000:
        mais1000 = mais1000 + 1
    if cont == 1 or preço < maisbaratopreço:
        maisbaratopreço = preço
        maisbaratonome = nome
print(f'Você gastou R${total}.')
print(f'Você comprou {mais1000} acima de R$1000,00')
print(f'Seu produto mais barato foi o {maisbaratonome}')





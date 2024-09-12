print(' {}\n'.format('-'*20),'CADASTRE UMA PESSOA\n','{}'.format('-'*20))
resposta = 'S'
maior18 = 0
homem = 0
mulhermenos20 = 0
while resposta == 'S':
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]:').upper().strip()[0]
    resposta = input('Deseja continuar? [S/N]:').strip().upper()[0]
    print('{}'.format('-'*30))
    if idade >= 18:
        maior18 = maior18 + 1
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 = mulhermenos20 + 1
print('Total de pessoas maior de idade: {}'.format(maior18))
print(f'Ao todo foram {homem} home(m)(ns) cadastrados.')
print(f'São {mulhermenos20} mulher(es) com menos de 20 anos')


opcao = 'oi'
cont = 0
soma = 0
menor = 0
maior = 0

while opcao.strip().lower()[0] != 'n':
    n = int(input('Digite um número:'))
    opcao = input('Quer continuar? [S/N]:')
    soma += n
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

print('Você digitou {} número(s) e média entre ele(s) foi {:.2f}.'.format(cont,soma/cont))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))


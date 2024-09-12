valor1 = int(input('Primeiro Valor:'))
valor2 = int(input('Segundo Valor:'))
opcao = 1
while opcao != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual sua opção?:'))
    if opcao == 1:
        print('A soma entre os número é {}'.format(valor1 + valor2))
    elif opcao == 2:
        print('O produto entre os número é {}'.format(valor1 * valor2))
    elif opcao == 3:
        if valor1 > valor2:
            print('O {} é o maior valor'.format(valor1))
        elif valor2 > valor1:
            print('O {} é o maior valor'.format(valor2))
        else:
            print('Os números são iguais')
    elif opcao == 4:
        print('==-' * 20)
        valor1 = int(input('Primeiro Valor:'))
        valor2 = int(input('Segundo Valor:'))
    elif opcao == 5:
        print('Finalizando programa...')
    else:
        print('Opção inválida!')
    print('==-'*20)


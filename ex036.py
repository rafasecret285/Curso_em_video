casa = float(input('Qual o valor da casa:R$'))
salario = float(input('Qual o seu salário?:R$'))
x = int(input('Em quantos anos você vai pagar a casa?:'))

tempo = x * 12
preco = casa / tempo
minimo = salario/100 * 30

if minimo >= preco:
    print('Para pagar a casa de R${}, em {} anos, a prestação mensal será de R${:.2f}\nEMPRÉSTIMO ACEITO!'.format(casa,x,preco))
else:
    print('Para pagar a casa de R${}, em {} anos, a prestação mensal será de R${:.2f}\nEMPRÉSTIMO NEGADO!'.format(casa, x,preco))
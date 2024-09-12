preco = float(input('Insira o preço do produto:'))
desconto = int(input('Insira o desconto:'))

numerador = 100 - desconto

novopreco = numerador/100 * preco
print('O preço do produto com desconto é de R${:.2f}'.format(novopreco))

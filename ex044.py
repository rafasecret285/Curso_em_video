print('{}LOJAS RAFAEL{}'.format('=*'*5,'=*'*5))

preco = float(input('PREÇO DA COMPRA: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista no dinhero ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('FORMA ESCOLHIDA:'))

if opcao == 1:
    print('''PREÇO DO PRODUTO:R${}
TOTAL A SER PAGO:R${:.2f}'''.format(preco,preco - preco/10*1))
elif opcao == 2:
    print('''PREÇO DO PRODUTO:R${}
TOTAL A SER PAGO:R${:.2f}'''.format(preco,preco - preco/100*5))
elif opcao == 3:
    print('''PREÇO DO PRODUTO:R${}
TOTAL A SER PAGO:R${}'''.format(preco,preco))
elif opcao == 4:
    parcela = int(input('EM QUANTAS PARCELAS A COMPRA SERÁ FEITA?:'))
    print('''PREÇO DO PRODUTO:R${}
TOTAL A SER PAGO:R${:.2f}
CADA PARCELA CUSTARÁ R${:.2f}'''.format(preco,preco + preco/100*20,(preco + preco/100*20)/parcela))



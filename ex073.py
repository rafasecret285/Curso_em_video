tabela = ('Pal','Fla','Cor','Int','Flu','Apr','Amg','Ame','San','Bra','Goi','For',
          'Bor','Spa','Cea','Cui','Cor','Ava','Ago','Juv')
print(f'Tabela Brasileirão:{tabela}')
print(f'Os 5 primeiros são:{tabela[0:5]}')
print(f'Os 4 últimos são:{tabela[-4:]}')
print(f'Times em ordem alfabética:{sorted(tabela)}')
print('O Fluminense está em {}o lugar'.format(tabela.index('Flu')+1))

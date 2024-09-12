lista=('Lápis',1.75,
       'Borracha',2,
       'Estojo',10,
       'Transferidor',15,
       'Caderno',15.5,
       'Compasso',12,
       'Mochila',100,
       'Livro',50)
print(f'-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(f'-'*40)
for x in range(0,len(lista)):
    if x%2==0:
        print(f'{lista[x]:.<30}',end='')
    else:
        print(f'R${lista[x]:.2f}')
print(f'-'*40)
from random import randint
tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for n in tupla:
    print(n,end = ' ')

print(f'\nMaior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')
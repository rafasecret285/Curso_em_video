print('='*30)
print('{:^30}'.format('BANCO VASCONCELOS'))
print('='*30)

cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1= 0
resto = int(input('Qual o valor que deseja sacar? R$'))

while resto > 0:
    while resto >= 50:
        resto -=50
        cedula50 += 1
    while resto >= 20:
        resto -= 20
        cedula20 += 1
    while resto >= 10:
        resto -= 10
        cedula10 += 1
    while resto >= 1:
        resto -= 1
        cedula1 += 1
print(f'Total de {cedula50} cédula(s) de R$50'if cedula50 > 0 else'')
print(f'Total de {cedula20} cédula(s) de R$20'if cedula20 > 0 else'')
print(f'Total de {cedula10} cédula(s) de R$10'if cedula10 > 0 else'')
print(f'Total de {cedula1} cédula(s) de R$1'if cedula1 > 0 else '')
print('='*30)


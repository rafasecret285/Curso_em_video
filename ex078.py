lista = []
menor = 0
maior = 0

for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0 or lista[c] < menor:
        menor = lista[c]
    if c == 0 or lista[c] > maior:
        maior = lista[c]
print(f'=-'*17)
print(f'O menor valor digitado foi o {menor} nas posições',end=' ')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print(f'\nO maior valor digitado foi o {maior} nas posições',end=' ')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')

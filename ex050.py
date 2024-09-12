soma = 0
cont = 0


for c in range(1,7):
    x = int(input('Digite um valor:'))
    if x % 2 == 0:
        soma = soma + x
        cont = cont + 1
print('Você informou {} números pares e a soma entre eles é {}'.format(cont,soma))
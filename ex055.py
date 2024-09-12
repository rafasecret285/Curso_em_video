
maior = 0
menor = 0


for cont in range(1,6):
    peso = float(input('Digite o peso da {}a pessoa:'.format(cont)))
    if cont == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('''O maior peso lido foi {}
E o menor: {}'''.format(maior,menor))
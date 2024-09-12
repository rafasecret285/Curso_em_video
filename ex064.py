n = 1
soma = 0
cont = -1
while n != 0:
    n = int(input('Digite um valor [0 para parar]:'))
    soma += n
    cont += 1
print('Você digitou {} números e a soma entre eles foi de {}'.format(cont,soma))
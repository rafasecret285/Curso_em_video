n = int(input('Digite um número de 0 a 9999:'))

u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unidades:{}'.format(u))
print('Dezenas:{}'.format(d))
print('Centenas:{}'.format(c))
print('Milhares:{}'.format(m))
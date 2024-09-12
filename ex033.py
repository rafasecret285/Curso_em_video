a = float(input('Digite um número:'))
b = float(input('Digite outro número:'))
c = float(input('Digite outro número:'))

if a > b and a > c:
    print('{} é o maio número.'.format(a))
elif b > a and b > c:
    print('{} é o maior número'.format(b))
else:
    print('{} é o maior número'.format(c))

if a < b and a < c:
    print('{} é o menor número.'.format(a))
elif b < a and b < c:
    print('{} é o menor número'.format(b))
else:
    print('{} é o menor número'.format(c))
print('{}\nANALISADOR DE TRIÂNGULOS\n{}'.format('='*25,'='*25))

a = float(input('Digite um lado para um triângulo:'))
b = float(input('Digite outro lado para um triângulo:'))
c = float(input('Digite outro lado para um triângulo:'))

if a > b + c and b > a + c and c > a + b:
    print('Os segmentos pode formar um triângulo')
else:
    print('Os segmentos não pode formar um triângulo')

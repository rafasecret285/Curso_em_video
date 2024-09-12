n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))
n4 = int(input('Digite um último número:'))

tupla = (n1,n2,n3,n4)


print(f'O valor 9 apareceu {tupla.count(9)} veze(s)')
if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram:',end='')
for x in tupla:
    if x%2==0:
        print(x,end=' ')


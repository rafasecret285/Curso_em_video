# calcular potencia
n = int(input('Insira um número:'))
exp = int(input('Insira seu expoente:'))

cont = 1
resultado = n

while cont < exp:
     resultado = resultado * n
     cont = cont + 1
print(resultado)
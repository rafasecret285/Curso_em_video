n = int(input('Insira o número para calcular sua fatorial:'))
resultado = 1


while n > 0:
    resultado = n * resultado
    n = n - 1
    print (resultado)
print(resultado)

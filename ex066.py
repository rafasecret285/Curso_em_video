valor = soma = quant = 0
while True:
    valor = int(input('Digite um valor (999 para parar):'))
    if valor == 999:
        break
    quant += 1
    soma += valor
print(f'A soma dos {quant} valores foi {soma}!')



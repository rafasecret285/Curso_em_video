frase = input('Digite uma frase para ver se ela é um palíndromo:').upper()
frase1 = frase.replace(' ','')


reverso = ''
for indice in range(len(frase1)-1,-1,-1):
    reverso += frase1[indice]
    print(reverso)

if reverso == frase1:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo')



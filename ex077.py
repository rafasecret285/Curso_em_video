palavras=('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR')
for x in range(0,len(palavras)):
    print(f'\nNa palavra {palavras[x]} temos as vogais' if x != 0 else f'Na palavra {palavras[x]} temos as vogais' ,end=' ')
    for letra in palavras[x]:
        if letra in 'AEIOU':
            print(letra,end=' ')

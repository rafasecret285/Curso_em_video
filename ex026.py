from unidecode import unidecode

x = unidecode(input('Digite uma frase:').strip().lower())


print('A letra "a" aparece {}x'.format(x.count('a')))
print('A letra "a" aparece primeiramente na posição {}'.format(x.find('a')))
print('A letra "a" aparece pela última vez na posição {}'.format(x.rfind('a')))
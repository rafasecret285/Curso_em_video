from datetime import date

maiores = 0
menores = 0
ano = 0
idade = 0

for cont in range(1,8):
    ano = int(input('Qual o ano de nascimento do {}o inegrante?'.format(cont)))
    idade = date.today().year - ano
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print('''O grupo possui {} integrantes maiores de idade
E {} menores de idade.'''.format(maiores,menores))
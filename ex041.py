from datetime import date

x = int(input('Digite seu ano de nascimento:'))
idade = date.today().year - x

if idade <= 9:
    print("Você está classificado como mirim")
elif idade > 9 and idade <= 14:
    print('Você está clasificado como infantil')
elif idade > 14 and idade <= 19:
    print('Você está classificado como junior')
elif idade > 19 and idade <= 25:
    print('Você está classificado como sênior')
else:
    print('Você está classificado como master')
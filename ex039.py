from datetime import date
ano = int(input('Em que ano você nasceu:'))
idade = date.today().year - ano

if idade < 18:
    print('Faltam {} anos para você completar 18'.format(18-idade))
elif idade == 18:
    print('Você tem 18 anos, aliste-se já!')
else:
    print('Você tem {} anos, já deveria ter se alistado há {} anos'.format(idade,idade - 18))
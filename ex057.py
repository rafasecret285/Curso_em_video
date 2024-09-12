sexo = input('Digite seu sexo [F/M]?:').lower().strip()[0]
while sexo not in 'fm':
    sexo = input('Dados inválidos, digite seu sexo novamente:').lower().strip()[0]
if sexo == 'f':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'
print('Seu sexo é {}'.format(sexo))
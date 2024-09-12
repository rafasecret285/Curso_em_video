nome = input('Digite seu nome completo:').strip().upper()
x = nome.find('SILVA')
if x >=0:
    print('Seu nome {}tem{} Silva'.format('\033[32m','\033[m'))

else:
    print('Seu nome {}não{} tem Silva'.format('\033[31m','\033[m'))




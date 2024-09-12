from random import randint

n = randint(1,5)

usuario = int(input('Digite um número inteiro de 1 a 5:'))

if usuario == n:
    print('{}Parabéns{} você acertou o número!'.format('\033[32m','\033[m'))
else:
    print('Você {}errou{} o número. Número certo {}'.format('\033[31m','\033[m',n))

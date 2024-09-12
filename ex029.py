vel = int(input('EM QUAL VELOCIDADE O SEU CARRO ESTÁ?:'))

if vel > 80:
    print("""VOCÊ ESTÁ \033[31mACIMA\033[m DA VELOCIDADE PERMITIDA, 
SUA MULTA CUSTARÁ {}{}R${}""".format('\033[31m',7*(vel - 80),'\033[m'))
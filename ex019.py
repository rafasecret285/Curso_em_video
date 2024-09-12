import random
n1 = input('Nome do 1o aluno:')
n2 = input('Nome do 2o aluno:')
n3 = input('Nome do 3o aluno:')
n4 = input('Nomde do 4o aluno:')

lista = [n1,n2,n3,n4]

escolhido = random.choice(lista)
print(escolhido)
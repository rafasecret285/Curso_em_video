# Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas
# as informações possíveis sobre ele

x = input('Digite algo:')
print('O tipo primitivo de x é {}:'.format(type(x)))

print('É um espaço?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculo?', x.isupper())
print('Está em minúsculo?', x.islower())
print('Está capitalizada? (maiúscula e minúscula)', x.istitle())

# esses métodos só funcionam em objetos que são string (str)

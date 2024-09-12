tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = 21
while n < 0 or n > 20:
    n = int(input('Digite un número de 0 a 20:'))
print(tupla[n])

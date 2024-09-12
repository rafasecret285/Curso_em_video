peso = float(input('Qual o seu peso (Kg)?:'))
altura = float(input('Qual a sua altura (m)?:'))
imc = peso / altura ** 2

if imc < 18.5:
    print('Abaixo do peso! IMC:{:.1f}'.format(imc))
elif imc < 25:
    print('Peso ideal. IMC:{:.1f}'.format(imc))
elif imc < 30:
    print('Sobrepeso.IMC:{:.1f}'.format(imc))
elif imc < 40:
    print('Obesidade!IMC:{:.1f}'.format(imc))
else:
    print('Obesidade mórbida. IMC:{:.1f}'.format(imc))
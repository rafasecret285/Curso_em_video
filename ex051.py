print("""{}
\033[35m10 TERMOS DE UMA PA\033[m
{}""".format('='*21,'='*21))

pt = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))

if razao > 0 :
    for c in range(pt,pt+9*razao+1,razao):
        print('{}-->'.format(c),end='')
else:
    for c in range(pt,pt+9*razao-1,razao):
        print('{}-->'.format(c),end='')
print('ACABOU!')


from time import sleep
for c in range(10,0,-1):
    print(c)
    sleep(1)
print("""\033[34m{}\033[m
\033[31mEXPLOSÃO DE FOGOS!!!\033[m
\033[34m{}\033[m""".format('=*'*10,'=*'*10))
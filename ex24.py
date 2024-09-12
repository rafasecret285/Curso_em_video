x = input('Em qual cidade você nasceu?')
cidade = x.split()[0].upper().strip()
if cidade == 'SANTO':
    print('True')
else:
    print('False')
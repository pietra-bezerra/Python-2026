print(f'Progama de empréstimo.' f'Responda: (0- Não ou 1- Sim)')
nomeNega = int(input('Possui carteira assinada?'))

if nomeNega == 1: #SIM
    print('Não pode realizar empréstimo')
else:
    cartAssi = int(input('Possui carteira assinada?'))
if cartAssi == 0: #NAO
    print('Não pode realizar empréstimo')
else:
    possuCasa = int(input('Possui casa própria?'))
if possuCasa == 0: #NAO
    print('Não pode realizar empréstimo')
else:
    print('Conceder empréstimo')
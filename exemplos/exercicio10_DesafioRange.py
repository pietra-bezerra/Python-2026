senha = 123456
tenta = 2
while tenta >= 0:
    entrada = int(input('Digite a senha: '))
    if entrada == senha:
        print('Acesso permitido!!')
        break
    else:
        tenta -= 1
      
        if tenta <= 0:
            print('Número de tentativas exedido.')
            break
        print(f'Senha incorreta. Você tem mais {tenta} tentativa(s).')
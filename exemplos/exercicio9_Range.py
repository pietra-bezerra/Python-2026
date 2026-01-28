pares = 0
print('Digite 5 números inteiros:')
for i in range(5):
    num = int(input(f'Número {i+1}: '))
    if num % 2 == 0:
        pares += 1 
print(f'A quantidade dos números pares é: {pares}')
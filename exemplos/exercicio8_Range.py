n1 = print('Digite quantos número que você quer adicionar:')
n = int(input())
soma = 0

for i in range(n):
    nume = int(input(f'Digite os números {i+1}: '))
    soma = soma + nume
    media = soma / n
print(f'A média é: {media}')

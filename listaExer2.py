numeros = []
print("Digite 5 números inteiros:")
for i in range(5):
    num_usu = int(input("Digite o número inteiro: "))
    numeros.append(num_usu)
    
print(f"Números digitados: {numeros}")
soma = sum(numeros)
print(f"A soma dos números digitados é: {soma}")
maior = max(numeros)
print(f"O maior número digitado é: {maior}")
menor = min(numeros)
print(f"O menor número digitado é: {menor}")
media = soma / len(numeros)
print(f"A média dos números digitados é: {media}")

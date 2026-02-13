produtos = []
preco = []
quantidade = []

print("Digite os produtos, preços e quantidades (digite '0' para encerrar):")
total = 0
while True:
    produto = input("Produto: ")
    if produto == '0':
        break
    produtos.append(produto)

    preco_produto = float(input("Preço: "))
    preco.append(preco_produto)

    quantidade_produto = int(input("Quantidade: "))
    quantidade.append(quantidade_produto)

    
print("Lista de Compras:")
for i in range(len(produtos)):
        total += preco[i] * quantidade[i]
        print(f"{produtos[i]} - R$ {preco[i]:.2f} - {quantidade[i]} un -  R$ {preco[i] * quantidade[i]:.2f}")

    
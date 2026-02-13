produtos = {
    1: "Monitor LED 24 polegadas",
    2: "Teclado wireless",
    3: "Mouse wireless",
    4: "Cartucho colorido"
}

preco = {
    1: 599.99,
    2: 49.26,
    3: 19.90,
    4: 54.00
}

quantidade = {
    1 : 1,
    2 : 1,
    3 : 1,
    4 : 2
}

print("Carrinho de Compras:")
for i in produtos:
 print(f"Código: {[i]} || Produto: {produtos[i]} || Preço Unitário {preco[i]:.2f} || Qtde Comprada {quantidade[i]} ")


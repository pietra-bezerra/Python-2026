quant = int(input('Digite a quantidade de camisas: '))
camisa = 12.50 
preco = quant * camisa

if quant <= 5:
    preco = preco * 0.97
elif quant <= 10:
        preco = preco * 0.95
else:
        preco = preco * 0.93
        
print(f'O valor total da compra é: {preco: .2f}')


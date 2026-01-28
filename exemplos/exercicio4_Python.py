valorDele = float(input("Digite quanto você possui em reais: "))
dolar = 5.32
euro = 6.16 

contaDo = valorDele * dolar 
contaEur = valorDele * euro

print(f"Você terá em Dolars {contaDo: .2f}, seu valor em Euro é: {contaEur: .2f}")

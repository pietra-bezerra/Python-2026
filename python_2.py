fonte = float(input(" Digite a tensão da fonte de alimentação em V (ex: 24V) :  "))
opera = float(input(" Digite a tensão de operação do dispositivo/LED em V (ex: 2V): "))
corrente = float(input("Digite a corrente desejada no circuito em Amperes "))

volta = (fonte - opera) / corrente

print(f"A resistência necessária para o circuito é de: {volta} Ohms")
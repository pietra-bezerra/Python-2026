import requests #bibilhoteca para fazer requisições HTTP

cep = input('Digite o CEP (somente números): ')
cep = cep.replace("-","") #vai tirar o tracinho se o usuario digitar 

if len(cep) != 8 or not cep.isdigit:
    print("CEP inválido!! DIgite até 8 números.")
else:
    url = f"https://viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)
    dados = resposta.json()

if 'erro' in dados: 
    print("CEP não encontrado")
else:
    logradouro = dados.get('logradouro', '')
    complemento = dados.get('complemento', '')
    bairro = dados.get('bairro', '')
    cidade = dados.get('localidade', '')
    estado = dados.get('uf', '')

    print('\n --- Endereço encntrado')
    print(f"Logadouro: {logradouro} ")
    print(f"complemento: {complemento} ")
    print(f"Bairro: {bairro} ")
    print(f"Cidade: {cidade} ")
    print(f"Estado: {estado} ")


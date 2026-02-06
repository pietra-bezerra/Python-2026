alunos = ["Michele Oliveira"]
alunos.append("João da Silva")
while True:
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    resposta = input("Deseja adicionar outro aluno ? (S/N)")
    if resposta.upper() == "N":
        break
print(f"Alunos cadastrados: {alunos}")
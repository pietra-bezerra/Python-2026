import random 
alunos = ['João', 'Marta', 'Pedro', 'Ana', 'Lucas', 'Martina' ]
#Embaralha a lista 
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
#Escolhe um aluno aleatoriamente
sorteio = random.choice(alunos)
print(f"Aluno Sorteado: {sorteio}")
print("Olá mundo!!")

# /////////////////////////////////////////////////////////////////////////////////

from datetime import datetime
ano_atual = datetime.now() . year
clube = "SPFC"
campeonato_mundial = 3
ano_fundacao = 1931
print(f"{clube} possui {campeonato_mundial} títulos mundiais.")
print(f"São {ano_atual - ano_fundacao} anos existência.")

# ////////////////////////////////////////////////////////////////////////////////

escola = 'Senai'
curso = 'Técnico em Desenvolvimento de Sistema'
uc = 'Lógica de Programação e Algoritmos'
print(
    f"Escola: {escola}\n"
    f"Curso: {curso}\n"
    f"Unidade Curricular: {uc}"
)

# ////////////////////////////////////////////////////////////////////////////////

print(f"Matrícula do Junior é {25:06d}.")
print(f"Matrícula da Alice é {14785:06d}.")
print(f"Matrícula do José é {100258:06d}.")

# /////////////////////////////////////////////////////////////////////////////////

print(f"Valor de pi é {3.14159265352384626433}.")
print(F"Valor de pi é {3.14159265352384626433: .20f} .")

# //////////////////////////////////////////////////////////////////////////////// 
agentes = {
    "007": "Londres",   
    "Viúva Negra": "Budapeste",
    "Ethan Hunt": "Paris",
}

print("Agentes e suas localizações:")

nome = input("Digite o nome do agente: ")
if agentes.get(nome) is None:
    print("Agente não encontrado.")
else:
 agentes.update({"Agente 007": "Tóquio"}) 
 agentes.update({"Trinity": "Matrix"}) 
 todos_agentes = list(agentes.keys())
 print("Todos os agentes cadastrados:")
 for agente in todos_agentes:
  print(f"Agente: {agente} || Localização: {agentes[agente]}")   

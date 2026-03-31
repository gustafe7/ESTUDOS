# Demonstração de métodos em listas...
INSS = ["Maria", "Manoel", "José", "Isabela"]
print("Eis, a fila do INSS:", INSS)

NOVO = input("Digite o nome do novo cliente do INSS: ")
INSS.append(NOVO)
print("Eis, a nova fila do INSS:", INSS)

print("Vou tirar a ultima pessoa da fila do INSS...")
ESPECIAL = INSS.pop()

print("Agora, vou colocaá-la na frente da fila do INSS...")
INSS.insert(0, ESPECIAL)
print("Eis, a nova fila do INSS:", INSS)

print("Maria não gostou e reclamou...")
INSS.remove("Maria")
print("E agora ela saiu 'Pe da vida'", INSS)

print("Para não ter mais reclamação, vamos atender...")
INSS.sort()
print("... em ordem alfabética!", INSS)

print("Onde está a nova pessoa chamada", ESPECIAL, "?")
print("Ela está na posição:", INSS.index(ESPECIAL)+1, "!")
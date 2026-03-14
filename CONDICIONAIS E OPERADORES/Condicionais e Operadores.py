# Demonstração de condicionais e operadores...

AVALIAÇAO = input("Digite a avaliação (A/B/C/D/E): ") # imputando avaliação...

if AVALIAÇAO:
    if AVALIAÇAO == "A" or AVALIAÇAO == "B" or AVALIAÇAO == "C": # avaliação igual A ou B ou C...
        print("APROVADO!")
    else: # caso não seja A, B ou C... logo, será D ou E 
        print("REPROVADO!")
else:
    print("VOCÊ NAO DIGITOU...")

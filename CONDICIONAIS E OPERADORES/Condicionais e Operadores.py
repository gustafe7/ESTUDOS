# Demonstração de condicionais e operadores...

AVALIAÇAO = input("Digite a avaliação (A/B/C/D/E): ")

if AVALIAÇAO:
    if AVALIAÇAO == "A" or AVALIAÇAO == "B" or AVALIAÇAO == "C":
        print("APROVADO!")
    else:
        print("REPROVADO!")
else:
    print("VOCÊ NAO DIGITOU...")

# 1 - ATIVIDADE: Construa uma simples matriz 2X2 e, como saída desse programa, a média e a soma dos valores digitados deverão ser calculadas e impressas na tela.
MATRIZ = [[0, 0], [0, 0]]
SOMA = 0

for I in range(2):
    for J in range(2):
        MATRIZ[I][J] = int(input(f"Digite o valor para a posição ({I}, {J}): "))
        SOMA = MATRIZ[I][J]

MEDIA = SOMA / 4

print("A soma dos valores é:", SOMA)
print("A média dos valores é:", MEDIA)
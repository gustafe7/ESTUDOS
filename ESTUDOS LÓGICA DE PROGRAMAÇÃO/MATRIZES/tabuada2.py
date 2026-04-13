# Demonstração de matrizes em Python
print("Eis, a tabela numerica original: ")
TABUADA = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

MULTIPLICAR = int(input("Digite o multiplicador: "))

for X in range(3):
    for Y in range(0, 3):
        TABUADA[X][Y] *= TABUADA[X][Y] * MULTIPLICAR

print("Eis, o multiplicador: ", MULTIPLICAR)
print("Confira o resultado das operações: ")
for RESULTADO in TABUADA:
    print(RESULTADO)
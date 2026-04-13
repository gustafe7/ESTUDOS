# 1 - ATIVIDADE: Construa um programa onde o usuário digitará um valor e o programa mostrará, na tela, a tabuada de multiplicação desses números. 
# Se possível, promova uma impressão que possibilite visualizar tais números da melhor maneira possível.

print("\n ==== TABUADA ===\n")

print("Digite um número desejado: ")
NUMERO = int(input()) # imputando um número desejado...

for X in range (0, 10): #DE 0 ATÉ 10...
    print(f"{X} x {NUMERO} =", X * NUMERO) # impressão do resultado das expressões...
   
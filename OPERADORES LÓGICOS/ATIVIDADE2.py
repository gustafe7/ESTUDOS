# 2- ATIVIDADE: Escreva um programa onde o usuário irá digitar 3 números distintos, 
# que por sua vez serão armazenados nas variáveis "X", "Y" e "Z". 
# A partir daí, o programa informe se estes números estão em ordem crescente ou decrescente. 
# Se não, exibir "Eles estão misturados"!​

print("Informe o primeiro número, Por favor!: ")
X = float(input())
print("Informe o segundo número, Por favor!:  ")
Y = float(input())
print("Informe o terceiro numero, Por favor!: ")
Z = float(input())

if X < Y < Z:
    print("Ordem Crescente!")
elif X > Y > Z:
    print("Ordem Decrescente!")
else:
    print("Eles estão misturados!")

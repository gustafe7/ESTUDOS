# 2- ATIVIDADE: Construa um programa onde o usuário digitará as quatro notas trimestrais e com base nelas, o programa irá calcular a média. 
# Caso a média seja menor do que 6, o programa deverá exibir na tela: “Aluno reprovado”; caso ela seja maior ou igual a 6, exibir: “Aluno aprovado”.​

print("Digite as respectivas notas: ")
print("NOTA 1: ")
NOTA1 = float(input()) # imputando nota 11
print("NOTA 2: ")
NOTA2 = float(input()) # imputando nota 2...
print("NOTA 3: ") 
NOTA3 = float(input()) # imputando nota 3...
print("NOTA 4: ")
NOTA4 = float(input()) # imputando nota 4..

# soma as notas inseridas e divide pela quantidade para obter a média...
SOMAR = (NOTA1 + NOTA2 + NOTA3 + NOTA4) / 4 
print("A nota do aluno é: ",SOMAR)

if SOMAR < 6: # média menor que 6...
    print("ALUNO REPROVADO!")

elif SOMAR <=10: # média supeprior a 6 e menor ou igual a 10...
    print("ALUNO APROVADO!")
else:
    print("Nota inválida.")
    
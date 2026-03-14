#3 - ATIVIDADE: Escreva um programa onde o usuário possa digitar o tamanho dos três lados de um triângulo 
# e com base nestas informações, verificar se o objeto geométrico é equilátero (com todos os lados iguais), 
# isósceles (com dois lados iguais) e escaleno (nenhum lado igual).​

print("\n=== ÁREA DO TRIANGULO===\n")

print("Informe o lado 'A' do triangulo, Por favor!: ")
A = input() # imputando o lado A...
print("Informe o lado 'B' DO triangulo, Por favor!: ")
B = input() # imputando o lado B...
print("Informe o lado 'C' do triangulo, Por favor!: ")
C = input() # imputando o lado C...

if A == B == C: # caso todos os lados sejam iguais...
    print("EQUILÁTERO!")
elif A == B or A == C or B == C: # caso apenas se 2 lados forem iguais...
    print("ISÓSCELES!")
else: # caso nenhum lado seja igual...
    print("ESCALENO!")

    
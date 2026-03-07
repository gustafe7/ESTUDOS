#3 - ATIVIDADE: Escreva um programa onde o usuário possa digitar o tamanho dos três lados de um triângulo 
# e com base nestas informações, verificar se o objeto geométrico é equilátero (com todos os lados iguais), 
# isósceles (com dois lados iguais) e escaleno (nenhum lado igual).​

print("\n=== ÁREA DO TRIANGULO===\n")

print("Informe o lado 'A' do triangulo, Por favor!: ")
A = input()
print("Informe o lado 'B' DO triangulo, Por favor!: ")
B = input()
print("Informe o lado 'C' do triangulo, Por favor!: ")
C = input()

if A == B == C:
    print("EQUILÁTERO!")
elif A == B or A == C or B == C:
    print("ISÓSCELES!")
else:
    print("ESCALENO!")

print("Os valores informados não formam um triangulo!")
    
# 3- ATIVIDADE: Construa um programa onde o usuário digitará o seu peso e a sua altura e o programa irá calcular o IMC correspondente. 
# Caso ele seja maior do que 25, ele deverá exibir "Acima do peso ideal". Caso seja menor do que 18, exibir "Abaixo do peso ideal". 
# Por fim, se o resultado do cálculo entregar um valor entre 18 e 25, informar ao usuário que "O seu peso está OK".​

print("Informe sua Altura: ")
ALTURA = float(input())

print("Informe o seu Peso: ")
PESO = float(input())

IMC = PESO / (ALTURA * ALTURA)
print("Seu IMC é: ", IMC)

if IMC > 25:
    print("ACIMA DO PESO IDEAL.")
elif IMC < 18:
    print("ABAIXO DO PESO IDEAL.")
elif 18 <= IMC <= 25:
    print("O seu peso está OK")

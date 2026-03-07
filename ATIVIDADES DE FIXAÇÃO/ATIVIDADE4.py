#4- ATIVIDADE: Construa um programa para que o usuário possa digitar o ano que nasceu 
# e o programa irá escrever, na tela, quantos anos ele completaria se ele estivesse em 2040.​

NASCIMENTO = int(input("Digite o ano do seu nascimento: "))

X = int(input("Digite o ano desejado: "))

CALCULO = X - NASCIMENTO
print("A sua idade será de: ", CALCULO)
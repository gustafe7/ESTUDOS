# 4 - ATIVIDADE: Criar um programa que possibilite o usuário digitar um determinado valor e a partir daí, 
# o sistema irá informar quantas notas ou moedas de quais valores serão entregues pelo caixa eletrônico.

SAQUE = int(input("Digite o valor a ser sacado: ")) # imputando valor a ser sacado...
CONT200 = 0; CONT100 = 0; CONT50 = 0; CONT20 = 0; CONT10 = 0; CONT5 = 0; CONT2 = 0

while True:
    if SAQUE >= 200:
        CONT200 += 1
        SAQUE = SAQUE - 200
    elif SAQUE >= 100:
        CONT100 += 1
        SAQUE = SAQUE - 100
    elif SAQUE >= 50:
        CONT50 += 50
        SAQUE = SAQUE - 50
    elif SAQUE >= 20:
        CONT20 = 20
        SAQUE = SAQUE - 20
    elif SAQUE >= 10:
        CONT10 += 10
        SAQUE = SAQUE - 10
    elif SAQUE >= 5:
        CONT5 += 5
        SAQUE = SAQUE - 5
    elif SAQUE >= 2:
        CONT2 += 2 
        SAQUE = SAQUE - 2
    else:
        break
print(f"O saque será entregue da seguinte forma: \n{CONT200} notas de R$200,00 \n{CONT100} notas de R$100,00 \n{CONT50} notas de R$50,00 \n{CONT20} notas de R$20,00 \n{CONT10} notas de R$10,00 \n{CONT5} notas de R$5,00 \n{CONT2} notas de R$2,00")


    
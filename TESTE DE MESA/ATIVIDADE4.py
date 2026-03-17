# 4 - ATIVIDADE: Criar um programa que possibilite o usuário digitar um determinado valor e a partir daí, 
# o sistema irá informar quantas notas ou moedas de quais valores serão entregues pelo caixa eletrônico.

valor = int(input("Digite o valor a ser sacado: ")) # imputando valor a ser sacado...

while valor >= 200:
    print("Nota de R$200")
    valor -= 200    
while valor >= 100:
    print("Nota de R$100")
    valor -= 100
while valor >= 50:
    print("Nota de R$50")
    valor -= 50
while valor >= 20:
    print("Nota de R$20")
    valor -= 20
while valor >= 10:
    print("Nota de R$10")
    valor -= 10
while valor >= 5:
    print("Nota de R$5")
    valor -= 5
while valor >= 2:
    print("Nota de R$2")
    valor -= 2
while valor >= 1:
    print("Moeda de R$1")
    valor -= 1
    
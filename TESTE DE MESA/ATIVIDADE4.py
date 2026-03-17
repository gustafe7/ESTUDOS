# 4 - ATIVIDADE: Criar um programa que possibilite o usuário digitar um determinado valor e a partir daí, 
# o sistema irá informar quantas notas ou moedas de quais valores serão entregues pelo caixa eletrônico.

valor = int(input("Digite o valor a ser sacado: ")) # imputando valor a ser sacado...

while valor >= 200: # Verificando se a nota é maior que 200...
    print("Nota de R$200")
    valor -= 200    
while valor >= 100: # Verificando se a nota é maior que 100...
    print("Nota de R$100")
    valor -= 100
while valor >= 50: # Verificando se a nota é maior que 50...
    print("Nota de R$50")
    valor -= 50
while valor >= 20: # Verificando se a nota é maior que  20...
    print("Nota de R$20")
    valor -= 20
while valor >= 10: # Verificando se a nota é maior que 10...
    print("Nota de R$10")
    valor -= 10
while valor >= 5: # Verificando se a nota é maior que 5...
    print("Nota de R$5")
    valor -= 5
while valor >= 2: # Verificando se a nota é maior que 2...
    print("Nota de R$2")
    valor -= 2
while valor >= 1: # Verificando se a moeda é maior que 1...
    print("Moeda de R$1")
    valor -= 1
    
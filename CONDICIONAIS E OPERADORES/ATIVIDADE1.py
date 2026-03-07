# 1 - ATIVIDADE: “Construa um programa onde o usuário irá informar o saldo da sua conta bancária e o valor do produto que ele deseja comprar. 
# A partir daí, deverá ser feita a subtração para verificar se há saldo suficiente ou não para a compra, além de notificar o usuário se ele pode ou não fazer a compra

print("Informe o valor da sua conta bancária: ")
VALOR = float(input())

print("Informe o valor do Produto: ")
PRODUTO = float(input())

SUBTRAIR = VALOR - PRODUTO
print("Restou o valor de: ", SUBTRAIR)

if VALOR >= PRODUTO: 
 print("Valor autorizado para a transação!")

else:
 print("Saldo insuficiente.")


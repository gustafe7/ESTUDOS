# 5- ATIVIDADE: Criar um programa que me permita saber exatamente por quanto tempo a minha poupança pode durar, 
# com base no saldo a ser informado, nos rendimentos mensais da caderneta e nos valores mensais que irei sacar 
# (desconsiderando a inflação e os respectivos reajustes). 
# Tenho guardado algo em torno de R$ 450.000,00 na minha poupança, 
# a qual rende 0,5% todos os meses. 
# Pretendo sacar mensalmente 3 salários mínimos (aproximadamente R$ 4.863,00), 
# para atender às minhas necessidades pessoais.

print("\n=== TEMPO DA POUPANÇA ===\n")
# usado para o usuário imputar as informações...
SALDO = float(input("Insira o seu saldo atual: "))
RENDIMENTO = float(input("Insira o seu rendimento mensal: "))
SAQUE = float(input("Informe o valor do saque: "))
MESES = 0

while SALDO > 0:
    SALDO = SALDO + (SALDO * RENDIMENTO) #  soma o saldo informado ao saldo * o rendimento informado
    SALDO = SALDO - SAQUE # subtrai o sanque do saldo atual ja com o rendimento
    MESES += 1 # adiciona mais um mês 
    print(MESES) # imprime os meses
    ANOS = MESES // 12 # transforma os meses em anos
MESES_RESTANTES = MESES % 12 # mostra os meses restantes 

print("A poupança irá durar:", ANOS, "anos e", MESES_RESTANTES, "meses")
#2- ATIVIDADE: Construa um programa para que o usuário digite o valor de um produto 
# e a quantidade de prestações que ele gostaria de pagar e com base nela, o valor de cada prestação.​

VALOR = int(input("Digite aqui o valor do Produto: "))
PARCELAS = int(input("Digite aqui o numero de parcelas: "))

PRESTACAO = VALOR / PARCELAS
print("O valor das parcelas é de: ", PRESTACAO)
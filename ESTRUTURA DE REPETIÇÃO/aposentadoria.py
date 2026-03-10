# Cálculo da aposentadoria...
IDADE = int(input("Qual é a idade: "))
INSS = int(input("Quantos anos de contribuição: "))
INSALUBRE = input("Em condições insalubres (S/N)? ")

if INSALUBRE == "S":
    if INSS >= 25:
        print("Aposentadoria especial!")
    else:
        print(f"Faltam {25 - INSS} para se aposentar...")
else:
    if IDADE >= 65 and INSS >= 35:
        print("Aposentadoria normal!")
    elif IDADE < 65 and INSS < 35:
        print(f"(IDADE): Faltam {65 - IDADE} anos e (CONTRIBUIÇÃO): Faltam {35 - INSS} anos para se aposentar...")
    else:
        print("Falta atender os requisitos...")
# 5 - ATIVIDADE: Escreva um algoritmo para criar um sistema de avaliação de serviços prestados, 
# para 5 notas diferentes e informar os seus respectivos valores: 
# "1) péssimo"; "2) ruim"; "3) razoável"; "4) bom" e "5) ótimo". 
# Porém, as avaliações só poderão ser feitas se o serviço em questão ter sido realmente prestado (“sim” ou “não”), atendendo a todos os requisitos.
#  Caso contrário, o usuário deverá digitar “não" e a nota atribuída será “0”, para que o sistema lhe possibilite descrever as suas reclamações.​

servico_prestado = input("O serviço foi prestado? (sim/não): ")
if servico_prestado == "sim":

    print("\n=== AVALIAÇÃO DE SERVIÇOS ===\n")

    print("1 - Péssimo")
    print("2 - Ruim")
    print("3 - Razoável")
    print("4 - Bom")
    print("5 - Ótimo\n")

    nota = input("Digite a nota do serviço (1-5): ")

    if nota == "1":
        print("Avaliação: péssimo\n")
        reclamacao = input("Por favor, descreva suas reclamações: \n")
        print("Agradecemos seu feedback.")
    elif nota == "2":
        print("Avaliação: ruim")
        reclamacao = input("Por favor, descreva suas reclamações: \n")
        print("Agradecemos seu feedback.")
    elif nota == "3":
        print("Avaliação: razoável")
        reclamacao = input("Por favor, descreva em que podemos melhorar: ")
        print("Agradecemos seu feedback.")
    elif nota == "4":
        print("Avaliação: bom")
        reclamacao = input("Por favor, descreva em que podemos melhorar: ")
        print("Agradecemos seu feedback.")
    elif nota == "5":
        print("Avaliação: ótimo")
        print("Agradecemos seu feedback.")
    else:
        print("Nota inválida. Por favor, digite um número entre 1 e 5.")

elif servico_prestado == "não":
    print("Nota atribuída: 0")

    reclamacao = input("Por favor, descreva suas reclamações: ")
    print("Reclamação registrada. Agradecemos seu feedback.")
else:
    print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")

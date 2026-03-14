# 1- ATIVIDADE: Escreva um programa para cadastrar o time e a sua posição na tabela de classificação do campeonato brasileiro. 
# A partir da sua posição, ele deverá exibir as seguintes classificações: "Campeão!" (1o. Lugar), 
# "Libertadores!" (entre 2o. e 6o.), 
# "Sul-Americana!" (entre 7o. e 12o.) 
# e "Rebaixado" (entre os 4 últimos). 
# Para clubes que estão entre a 13a. e a 16a. posição…

print('\n === CADASTRO DE TIME ===\n')

print("Informe o seu time, Por favor: ")
TIME = input()
print("Informe a posição na tabela de classifiação, Por favor: ")
CLASSIFICACAO = input()

if not TIME or not CLASSIFICACAO: # se não conter valor em TIME e CLASSIFICACAO...
    print("Informe o time e a classificação, Por favor!")

if CLASSIFICACAO:
    if CLASSIFICACAO == "1": # se for igual a 1...
        print("CAMPEÃO!")
    if CLASSIFICACAO >= "2" and CLASSIFICACAO <="6": # maior ou igual a 2 e menor ou igual a 6...
        print("LIBERTADORES!")
    if CLASSIFICACAO >= "7" and CLASSIFICACAO <="12": # maior ou igual a 7 e menor ou igual a 12...
        print("Sul-Americana!")
    if CLASSIFICACAO >="13" and CLASSIFICACAO <="16": # maior ou igual a 13 e menor ou igual a 16...
        print("REBAIXADO!")
else:
    print("As posições aceitas são somente da 1 até 16.")
# 1- ATIVIDADE: “Construa um programa onde o usuário irá digitar o nome de um filme ou série de TV e em seguida, perguntará qual seria a sua nota para avaliar o filme, em uma escala de 1 a 5. 
# De acordo com a nota definida, o usuário receberá as respostas “Péssimo”, “Ruim”, “Razoável”, “Bom” e “Ótimo”. 
# e em caso de notas baixas, deverá ser feita dado ao usuário, a possibilidade de descrever o porquê do conteúdo em questão foi avaliado de forma negativa. 
# Por fim, caso o usuário digite qualquer outro valor fora da escala, deverá ser exibido um alerta.​

print("1. Péssimo")
print("2. Ruim")
print("3. Razoável")
print("4. Bom")
print("5. Ótimo")

print("Digite um Filme ou Série: ")
MOVIE = input()

print("Digite uma nota para avaliação: ")
NOTA = float(input())

match NOTA: 
    case 1:
        print(input("Informe sua sua avaliação:"))
        print("Obrigado pela sua avaliação!")
    case 2:
        print(input("Informe a sua avalição: "))
        print("Obrigado pela sua avaliação!")
    case 3:
        print(input("Informe sua avaliação: "))
        print("Obrigado pela sua avaliação!")
    case 4:
        print("Obrigado pela sua avaliação!")
    case 5:
        print("Obrigado pela sua avaliação!")
    case _:
        print("Nota Inválida!")
# 1 - ATIVIDADE: Construa um programa que verifique a quantidade de acertos de uma prova com cinco questões, 
# sabendo que serão fornecidos pelo usuário as letras assinaladas em cada questão. 
# Para isso será criado uma lista chamada GABARITO com as seguintes respostas: B, C, A, E, D.​

GABARITO = ["B", "C", "A", "E", "D"]
OPCOES_VALIDAS = ["A", "B", "C", "D", "E"] # Lista de opções permitidas
ACERTOS = 0

print("Vamos corrigir a prova! Digite as respostas assinaladas para cada questão:")

RESPOSTAS = []
for QUESTAO in range(5):
    while True: # Inicia um loop infinito para validação
        RESPOSTA = input(f"Questão {QUESTAO + 1}: ").upper()
        
        if RESPOSTA in OPCOES_VALIDAS:
            RESPOSTAS.append(RESPOSTA)
            break # Sai do loop 'while' e vai para a próxima questão
        else:
            print("Resposta inválida! Por favor, insira uma letra de A até E.")

# Parte da correção
for QUESTAO in range(len(GABARITO)):
    if RESPOSTAS[QUESTAO] == GABARITO[QUESTAO]:
        ACERTOS += 1

print("-" * 20)
print(f"Quantidade de acertos: {ACERTOS}")
print(f"O gabarito da prova é: {GABARITO}")
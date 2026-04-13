#2 - ATIVIDADE: Construa um programa que pergunte ao usuário, qual é o melhor clube de futebol do Brasil 
# (o qual deverá estar definido no corpo do programa). 
# Enquanto ele não responder corretamente, o programa irá fazer uma advertência e retornará para a pergunta. 
# Somente após o usuário responder a pergunta corretamente, o programa irá parabenizá-lo.​

TIME = ""
while TIME != "Flamengo": #se o time for DIFERENTE do FLAMENGO...
    print("Qual o melhor time do Brasil?") 
    TIME = input() # imputando o time que o sistema deseja...
    continue #ira continuar insistindo até o usuário digitar FLAMENGO...
else: 
    print("O melhor time do Brasil é o", TIME) 


    

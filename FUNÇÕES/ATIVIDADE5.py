# 5 - ATIVIDADE: Crie um programa em Python que solicite o nome e a idade do usuário e permita a escolha de um plano de academia.
# Utilize uma função com passagem de argumentos para exibir uma mensagem personalizada com base no plano escolhido e na idade do usuário, 
# considerando:
# Menores de 16 anos não podem se matricular
# Entre 16 e 17 anos precisam de autorização dos pais
# 18 anos ou mais têm acesso liberado

def plano_academia(nome, idade): # Função que recebe o nome e a idade do usuário para determinar o plano de academia
    if idade < 16:
        print("Menor de idade! Infelizmente não poderá realizar a matrícula.")
        return # Encerra a função se o usuário for menor de 16 anos
    elif idade < 18:
        print(f"{nome}, será necessário uma autorização de um responsável.")
    else:
        print(f"{nome}, seu acesso está liberado!")

    print("\nEscolha um plano:")
    print("1 - Básico")
    print("2 - Intermediário")
    print("3 - Premium")
    plano = int(input("Escolha o plano (1/2/3): "))
    
    match plano: # Estrutura de controle para determinar a mensagem com base no plano escolhido
        case 1: # Plano Básico
            print("Treine no seu ritmo!")
        case 2: # Plano Intermediário
            print("Evolução constante!")
        case 3: # Plano Premium
            print("Acesso total e ilimitado!")
        case _: # Caso o usuário escolha um plano inválido
            print("Plano inválido.")

print("\n=== PLANO DE ACADEMIA ===\n")
nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))

plano_academia(nome, idade) # Chamada da função para processar as informações do usuário e exibir a mensagem personalizada com base na idade e plano escolhido
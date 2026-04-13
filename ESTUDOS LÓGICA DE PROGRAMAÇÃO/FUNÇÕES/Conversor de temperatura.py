# DESAFIO: "Conversor de temperaturas!"​

#"Preciso de um programa que faça a conversão 
# da temperatura, em diferentes unidades de medida:

#​ 1- De Celsius para Kelvin e Fahrenheit;​
# 2- De Kelvin para Celsius e Fahrenheit;​
# 3- De Fahrenheit para Celsius e Kelvin."​

def menu(): # menu para escolher uma das opcoes...
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    print("1 - Celsius")
    print("2 - Kelvin")
    print("3 - Fahrenheit")
    print("4 - Sair\n")


def adicionar_celsius(): # função para adicionar o valor em Celsius e fazer as conversões...
    celsius = float(input("Digite o valor em Celsius: ")) # conversão de string para float, para permitir números decimais
    
    c_f = celsius * 1.8 + 32 # conversão de celcius para Fahrenheit
    c_k = celsius + 273 # conversão de celcius para Kelvin
    print("Celsius para Fahrenheit:", c_f) # exibe o resultado da conversão de Celsius para Fahrenheit
    print("Celsius para Kelvin:", c_k) # exibe o resultado da conversão de Celsius para Kelvin


def adicionar_kelvin(): # função para adicionar o valor em Kelvin e fazer as conversões...
    kelvin = float(input("Digite o valor em Kelvin: ")) # conversão de string para float, para permitir números decimais
    
    k_c = kelvin - 273 # conversão de Kelvin para Celsius
    k_f = (kelvin - 273) * 1.8 + 32 # conversão de Kelvin para Fahrenheit 
    print("Kelvin para Celsius:", k_c) # exibe o resultado da conversão de Kelvin para Celsius
    print("Kelvin para Fahrenheit:", k_f) # exibe o resultado da conversão de Kelvin para Fahrenheit


def adicionar_fahrenheit(): # função para adicionar o valor em Fahrenheit e fazer as conversões...
    fahrenheit = float(input("Digite o valor em Fahrenheit: ")) # conversão de string para float, para permitir números decimais
    
    f_c = (fahrenheit - 32) / 1.8 # conversão de Fahrenheit para Celsius
    f_k = (fahrenheit - 32) * 5/9 + 273 # conversão de Fahrenheit para Kelvin
    print("Fahrenheit para Celsius:", f_c) # exibe o resultado da conversão de Fahrenheit para Celsius
    print("Fahrenheit para Kelvin:", f_k) # exibe o resultado da conversão de Fahrenheit para Kelvin


while True: # loop infinito para exibir o menu e permitir que o usuário escolha uma opção...
    menu() # exibe o menu para o usuário escolher uma opção...
    opcao = input("Escolha uma opção: ") # recebe a opção escolhida pelo usuário e armazena na variável "opcao"

    if opcao == "1": # se for igual a 1...
        adicionar_celsius() # chama a função para adicionar o valor em Celsius e fazer as conversões...
    elif opcao == "2": # se for igual a 2...
        adicionar_kelvin() # chama a função para adicionar o valor em Kelvin e fazer as conversões...
    elif opcao == "3": # se for igual a 3...
        adicionar_fahrenheit() # chama a função para adicionar o valor em Fahrenheit e fazer as conversões...
    elif opcao == "4": # se for igual 4...
        print("Programa encerrado") # exibe a mensagem de encerramento do programa
        break # encerra o loop infinito e, consequentemente, o programa
    else: # se a opção escolhida for diferente de 1, 2, 3 ou 4...
        print("Opção inválida") # exibe a mensagem de opção inválida e volta para o menu para o usuário escolher novamente...
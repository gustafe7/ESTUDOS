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


def adicionar_celsius(): 
    celsius = float(input("Digite o valor em Celsius: "))
    
    c_f = celsius * 1.8 + 32 # conversão de celcius para Fahrenheit
    c_k = celsius + 273 # conversão de celcius para Kelvin
    print("Celsius para Fahrenheit:", c_f)
    print("Celsius para Kelvin:", c_k)


def adicionar_kelvin():
    kelvin = float(input("Digite o valor em Kelvin: "))
    
    k_c = kelvin - 273 # conversão de Kelvin para Celsius
    k_f = (kelvin - 273) * 1.8 + 32 # conversão de Kelvin para Fahrenheit 
    print("Kelvin para Celsius:", k_c)
    print("Kelvin para Fahrenheit:", k_f)


def adicionar_fahrenheit():
    fahrenheit = float(input("Digite o valor em Fahrenheit: "))
    
    f_c = (fahrenheit - 32) / 1.8 # conversão de Fahrenheit para Celsius
    f_k = (fahrenheit - 32) * 5/9 + 273 # conversão de Fahrenheit para Kelvin
    print("Fahrenheit para Celsius:", f_c)
    print("Fahrenheit para Kelvin:", f_k)


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1": # se for igual a 1...
        adicionar_celsius()
    elif opcao == "2": # se for igual a 2...
        adicionar_kelvin()
    elif opcao == "3": # se for igual a 3...
        adicionar_fahrenheit()
    elif opcao == "4": # se for igual 4...
        print("Programa encerrado")
        break 

    else:
        print("Opção inválida")
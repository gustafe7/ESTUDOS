# 4 - ATIVIDADE: Seria possível escrever um programa que avalie a naturalidade do torcedor (carioca, paulista ou mineiro) 
# e com base nela, sugerir uma lista dos principais clubes de futebol regionais? 
# A partir desta lista, o torcedor em questão irá votar no clube do seu coração e receber uma mensagem personalizada…

print("\n=== TORCEDOR ===\n")
# Menu 
def torcedor_carioca(): # função para exibir os times de futebol do Rio de Janeiro...
    print("1 - Flamengo") 
    print("2 - Fluminense")  
    print("3 - Vasco")
    print("4 - Botafogo")

def torcedor_paulista(): # função para exibir os times de futebol de São Paulo...
    print("1 - São Paulo")
    print("2 - Corinthians")
    print("3 - Santos")
    print("4 - Palmeiras")

def torcedor_mineiro(): # função para exibir os times de futebol de Minas Gerais...
    print("1 - Atlético Mineiro")
    print("2 - Cruzeiro")
    print("3 - América Mineiro")

print("Digite o seu estado (Rio de Janeiro/Minas Gerais/São Paulo):") 
estado = input().lower() # imputando o nome do estado e convertendo para letras minúsculas para facilitar a comparação com as opções do menu...

if estado == "rio de janeiro": # se o estado for igual a Rio de Janeiro, o programa exibirá os times de futebol do Rio de Janeiro e pedirá para o usuário escolher um time...
    torcedor_carioca() # chama a função para exibir os times de futebol do Rio de Janeiro...
    print("Escolha o seu time de coração (1/2/3/4): ")
    time = int(input("Escolha seu time: ")) 
    match time: # estrutura de controle de fluxo para comparar o valor da variável "time" com as opções do menu e exibir a mensagem personalizada correspondente...
        case 1: 
            print("Mengão na área! Raça, amor e paixão!")
        case 2:
            print("Fluzão de guerreiros! Tradição e elegância!")
        case 3:
            print("Gigante da Colina! Respeita a história!")
        case 4:
            print("Glorioso! Estrela solitária que brilha sempre!")
            
elif estado == "são paulo": # se o estado for igual a São Paulo, o programa exibirá os times de futebol de São Paulo e pedirá para o usuário escolher um time...
    torcedor_paulista() # chama a função para exibir os times de futebol de São Paulo...
    print("Escolha o seu time de coração (1/2/3/4): ")
    time = int(input("Escolha seu time: "))
    match time: # estrutura de controle de fluxo para comparar o valor da variável "time" com as opções do menu e exibir a mensagem personalizada correspondente...
        case 1:
            print("Tricolor Paulista! Soberano dentro e fora de campo!")
        case 2:
            print("Timão! Loucura e fiel até o fim!")
        case 3:
            print("Peixe! A tradição de revelar craques!")
        case 4:
            print("Verdão! Avanti Palestra!")
            
elif estado == "minas gerais": # se o estado for igual a Minas Gerais, o programa exibirá os times de futebol de Minas Gerais e pedirá para o usuário escolher um time...
    torcedor_mineiro() # chama a função para exibir os times de futebol de Minas Gerais...
    print("Escolha o seu time de coração (1/2/3):  ")
    time = int(input("Escolha seu time: "))
    match time: # estrutura de controle de fluxo para comparar o valor da variável "time" com as opções do menu e exibir a mensagem personalizada correspondente...
        case 1: 
            print("Galo forte e vingador!")
        case 2:
            print("Raposa! Tradição e estrelas no peito!")
        case 3:
            print("Coelho! Guerreiro e surpreendente!")
else:
    print("Insira o nome de um dos Estados solicitados.")
    


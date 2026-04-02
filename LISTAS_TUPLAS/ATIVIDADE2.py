#2 - ATIVIDADE: Construa um programa que receba a escalação dos 11 jogadores titulares que irão iniciar uma partida, 
# registrando seus nomes e o número da camisa, além de imprimir a lista após a sua digitação. 
# Durante o intervalo do jogo, ofereça ao técnico a opção de realizar a substituição de 3 jogadores, exibindo a lista atualizada com os respectivos nomes e números.​

# Titulares
jogadores = ["Diego Alves",
             "Rodrigo Caio",
             "Pablo Mari",
             "Rafinha",
             "Filipe Luís",
             "Arão",
             "Gerson",
             "Arrascaeta",
             "Everton Ribeiro",
             "Gabigol",
             "Bruno Henrique"]

# Reservas
reservas = ["Rodinei",
            "Rodolfo",
            "Renê",
            "Diego",
            "Vitinho",
            "Cesar",
            "V. Souza",
            "Reinier",
            "Lincoln",
            "Piris",
            "Thuler",
            "Berrío"]

# Números dos titulares
numeros = [1, 3, 4, 13, 16, 5, 8, 14, 7, 9, 27]

# Mostrar escalação inicial
print("=== TIME TITULAR ===")
for i in range(len(jogadores)):
    print(f"{i} - {numeros[i]} - {jogadores[i]}")

# Substituições
print("\n=== INTERVALO ===")
opcao = input("Deseja fazer substituições? (s/n): ").lower()

if opcao == 's':
    for i in range(3):
        print(f"\nSubstituição {i+1}")

        # Mostrar titulares
        print("\nTitulares:")
        for j in range(len(jogadores)):
            print(f"{j} - {numeros[j]} - {jogadores[j]}")

        # Validar jogador que sai
        while True:
            try:
                sair = int(input("Digite o número do jogador que vai sair: "))
                if 0 <= sair < len(jogadores):
                    break
                else:
                    print("Número inválido! Tente novamente.")
            except:
                print("Digite um número válido!")

        # Mostrar reservas
        print("\nReservas:")
        for r in range(len(reservas)):
            print(f"{r} - {reservas[r]}")

        # Validar jogador que entra
        while True:
            try:
                entrar = int(input("Digite o número do reserva que vai entrar: "))
                if 0 <= entrar < len(reservas):
                    break
                else:
                    print("Número inválido! Tente novamente.")
            except:
                print("Digite um número válido!")

        # Fazer substituição
        jogadores[sair] = reservas[entrar]
        reservas.pop(entrar)

# Mostrar time final
print("\n=== TIME ATUALIZADO ===")
for i in range(len(jogadores)):
    print(f"{numeros[i]} - {jogadores[i]}")


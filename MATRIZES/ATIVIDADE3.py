# 3 - ATIVIDADE: Seria possível reconstruir o programa da aula passada, referente a escalação dos 11 jogadores titulares, 
# que foram substituídos durante o intervalo por 3 atletas suplentes? 
# Neste novo cenário, utilizaremos uma única matriz, a qual deverá ter 11 listas contendo as informações referentes ao número da camisa e o nome do jogador. 
# Se desejar, também poderá informar a posição em que o atleta atua no time.

# Função para encontrar índice pelo número da camisa
time = [[1, "Diego Alves", "Goleiro"], 
        [3, "Rodrigo Caio", "Zagueiro"], 
        [4, "Pablo Mari", "Zagueiro"], 
        [13, "Rafinha", "Lateral Direito"], 
        [16, "Filipe Luís", "Lateral Esquerdo"], 
        [5, "Arão", "Volante"], 
        [8, "Gerson", "Meio-Campo"],
        [14, "Arrascaeta", "Meio-Campo"],
        [7, "Everton Ribeiro", "Meio-Campo"],
        [9, "Gabigol", "Atacante"],
        [27, "Bruno Henrique", "Atacante"]]
 # Matriz para armazenar os jogadores reservas 
reservas = [[10, "Rodinei", "Lateral"],
            [11, "Rodolfo", "Zagueiro"],
            [12, "Renê", "Lateral"],
            [15,"Diego", "Meia"],
            [17, "Vitinho", "Atacante"],
            [18, "Cesar", "Goleiro"],
            [19, "V. Souza", "Volante"],
            [20, "Reinier", "Atacante"],
            [21, "Lincoln", "Atacante"],
            [22, "Piris", "Volante"],
            [23, "Thuler", "Zagueiro"],
            [24, "Berrío", "Atacante"]]

def buscar_indice(lista, numero):
    for i in range(len(lista)):
        if lista[i][0] == numero:
            return i
    return -1

# Mostrar escalação inicial
print("=== TIME TITULAR ===")
for jogador in time:
    print(f"{jogador[0]} - {jogador[1]} - {jogador[2]}")

# Substituições
print("\n=== INTERVALO ===")
opcao = input("Deseja fazer substituições? (s/n): ").lower()

if opcao == 's':
    for x in range(3):
        print(f"\nSubstituição {x+1}")

        # Mostrar titulares
        print("\nTitulares:")
        for jogador in time:
            print(f"{jogador[0]} - {jogador[1]} - {jogador[2]}")

        # Escolher quem sai
        while True:
            try:
                num_sair = int(input("Digite o número da camisa do jogador que vai sair: "))
                idx_sair = buscar_indice(time, num_sair)

                if idx_sair != -1:
                    break
                else:
                    print("Jogador não encontrado! Tente novamente.")
            except:
                print("Digite um número válido!")

        # Mostrar reservas
        print("\nReservas:")
        for jogador in reservas:
            print(f"{jogador[0]} - {jogador[1]} - {jogador[2]}")

        # Escolher quem entra
        while True:
            try:
                num_entrar = int(input("Digite o número da camisa do reserva: "))
                idx_entrar = buscar_indice(reservas, num_entrar)

                if idx_entrar != -1:
                    break
                else:
                    print("Reserva não encontrado! Tente novamente.")
            except:
                print("Digite um número válido!")

        # Fazer substituição
        time[idx_sair], reservas[idx_entrar] = reservas[idx_entrar], time[idx_sair]

# Mostrar time final
print("\n=== TIME ATUALIZADO ===")
for jogador in time:
    print(f"{jogador[0]} - {jogador[1]} - {jogador[2]}")
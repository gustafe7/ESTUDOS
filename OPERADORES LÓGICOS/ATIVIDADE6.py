# 6 - ATIVIDADE: Seria possível criar um programa com base na lógica do jogo "papel, pedra e tesoura"?"​
print("\n=== JOGO: PEDRA, PAPEL, TESOURA ===\n")

print("Escolha uma opção: ")
print("1 - MULTIJOGADOR")
print("2 - JOGADOR VS COMPUTADOR\n")
opcao = input("Digite o número da opção desejada: ")

if not opcao:
    print("Escolha uma opção válida, Por favor!")

if opcao == "1":
    JOGADOR1 = input("Insira seu nome: ")
    print("Nome aceito!\n")
    JOGADOR2 = input("Insira seu nome: ")
    print("Nome aceito!\n")

    PLAY1 = input(f"({JOGADOR1}) Escolha entre: pedra, papel ou tesoura: ")
    PLAY2 = input(f"({JOGADOR2}) Escolha entre: pedra, papel ou tesoura: ")

    if PLAY1 == PLAY2:
        print("EMPATE!")
    elif PLAY1 == "pedra" and PLAY2 == "tesoura" or PLAY1 == "tesoura" and PLAY2 == "papel" or PLAY1 == "papel" and PLAY2 == "pedra":
        print(f"Jogador(a) {JOGADOR1} venceu!\n")
    else:
        print(f"Jogador(a) {JOGADOR2} venceu!\n")

if opcao == "2":
    import random
    
    JOGADOR1 = input("\n""Insira o seu nome: ")
    print("Nome aceito!")
    COMPUTADOR = input("\n""Insira um nome para o adversário: ")
    print("Nome aceito!")

    PLAY1 = input(f"\n({JOGADOR1}) Escolha entre: pedra, papel ou tesoura: ")

    if not PLAY1:
        print("Escolha uma das opções, Por favor!")

    opcoes = ["pedra","papel","tesoura"]
    CPU = random.choice(opcoes)
    print(f"O(a) {COMPUTADOR} escolheu:", CPU)
        
    if PLAY1 == CPU:
        print("EMPATE!")
    elif PLAY1 == "pedra" and CPU == "tesoura" or PLAY1 == "tesoura" and CPU == "papel" or PLAY1 == "papel" and CPU == "pedra":
        print(f"\nJogador(a) {JOGADOR1} Venceu!")
    else:
        print(f"\nO(a) {COMPUTADOR} venceu!")
#2- ATIVIDADE: Construa um programa onde o usuário digitará o dia da semana. De acordo com a sua resposta, o programa deverá exibir na tela uma recomendação do que ele poderia fazer neste dia. 
# Se ele não digitar absolutamente, nada, o programa exibirá um alerta.”​


print("\n==== ESCOLHA O DIA DA SEMANA ====\n")
#menu
print("1 - Segunda-Feira")
print("2 - Terça-Feira")
print("3 - Quarta-Feira")
print("4 - Quinta-Feira")
print("5 - Sexta-Feira")
print("6 - Sábado")
print("7 - Domingo")

DIA = int(input("Insira o dia da semana, por favor: ")) # imputando o dia...

match DIA:
    case 1: # caso o dia seja 1...
        print("Segunda — Lazer leve"'\n')
        print("- Caminhada ouvindo podcast ou música relaxante")
        print("- Organizar as metas da semana")
        print("- Assistir 1 vídeo curto sobre algo que você quer aprender")
    case 2: # caso o dia seja 2...
        print("Terça — Corpo"'\n')
        print("- Academia ou treino em casa")
        print("- Alongamento e relaxamento muscular")
        print("- Caminhada ao ar livre")
    case 3: # caso o dia seja 3...
        print("Quarta — Mente"'\n')
        print("- Ler 20-30 páginas de um livro (não precisa ser técnico)")
        print("- Documentação interessante")
        print("- Filme bom (sem maratonar série infinita 😅)")
    case 4: # caso o dia seja 4...
        print("Quinta — Social"'\n')
        print(" - Conversar com amigos")
        print("- Jogar algo online")
        print("Sair para tomar algo simples com os amigos")
    case 5: # caso o dia seja 5...
        print("Sexta — Hobbies"'\n')
        print("- Filme")
        print("Série")
        print("- Futebol")
        print("- Música")
    case 6: # caso o dia seja 6...
        print("Sábado — Dia mais livre"'\n')
        print("- Passeio")
        print("Restaurante diferente")
        print("- Shopping")
        print("- Eventos culturais")
        print("Praia/Piscina")
    case 7: # caso o dia seja 7...
        print("Domingo — Dia de descanso"'\n')
        print("- Planejar a semana")
        print("- Organizar ambiente")
        print("- Caminhada leve")
        print("- Dormir mais cedo")
    case _: # caso não seja nenhuma das opcoes do menu...
        print("Opção não reconhecida. Por favor, insira um número entre 1 e 7.")
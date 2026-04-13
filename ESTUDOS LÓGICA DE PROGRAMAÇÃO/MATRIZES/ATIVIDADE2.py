# 2 - ATIVIDADE: Construa um jogo chamado quadrado mágico 3X3, no qual o usuário preencherá o vetor com números de um a nove (sem repetir números) 
# e a soma de todas as linhas, colunas e diagonais será igual a quinze. 
# Caso não conheçam sobre o jogo, pesquisar...​

print("Bem-vindo ao jogo do quadrado mágico 3X3!")
print("Preencha a matriz com números de 1 a 9, sem repetir, para formar um quadrado mágico onde a soma de todas as linhas, colunas e diagonais seja igual a 15.")

MATRIZ = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
SOMA = 0

for I in range(3):
    for J in range(3):
        while True:
            NUMERO = int(input(f"Digite um número para a posição ({I}, {J}): "))
            if NUMERO < 1 or NUMERO > 9:
                print("Número inválido! Digite um número entre 1 e 9.")
            elif any(NUMERO in row for row in MATRIZ):
                print("Número já utilizado! Digite um número diferente.")
            else:
                MATRIZ[I][J] = NUMERO
                break
print("Matriz preenchida:")
for LINHA in MATRIZ:
    print(LINHA)

# Verificação do quadrado mágico
eh_magico = True

# Verificar linhas
for i in range(3):
    if sum(MATRIZ[i]) != 15:
        eh_magico = False

# Verificar colunas
for j in range(3):
    soma_coluna = 0
    for i in range(3):
        soma_coluna += MATRIZ[i][j]
    if soma_coluna != 15:
        eh_magico = False

# Verificar diagonais
if MATRIZ[0][0] + MATRIZ[1][1] + MATRIZ[2][2] != 15:
    eh_magico = False

if MATRIZ[0][2] + MATRIZ[1][1] + MATRIZ[2][0] != 15:
    eh_magico = False

# Resultado final
if eh_magico:
    print("Parabéns! Você formou um quadrado mágico!")
else:
    print("Não é um quadrado mágico.")
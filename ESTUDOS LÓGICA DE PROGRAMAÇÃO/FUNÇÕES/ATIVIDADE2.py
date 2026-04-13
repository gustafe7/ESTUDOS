# 2 - ATIVIDADE: Crie um jogo de par ou ímpar onde o computador irá “gerar” (você digita) um número aleatório e o usuário irá digitar outro. 
# Após digitar o número, o programa irá utilizar uma função para resolver o jogo. 
# Se a soma dos números for par, o usuário vence. Se for ímpar, o computador vence.​

print("\n=== JOGO - PAR OU ÍMPAR ===\n")
print("Insira seu nome: ")
JOGADOR1 = input()
print("Insira seu nome: ")
COMPUTADOR = input()
print("Escoha um número de 1 a 10: ")
PLAY = input(f"{JOGADOR1}: ")

import random

CPU = random.randint(1, 10)
print(f"{COMPUTADOR} escolheu: {CPU}")

def JOGO():
    SOMA = int(PLAY) + int(CPU)
    print(f"A soma dos números é: {SOMA}")
    if SOMA % 2 == 0:
        print(f"{JOGADOR1} venceu!")
    else:
        print(f"{COMPUTADOR} venceu!")
JOGO()

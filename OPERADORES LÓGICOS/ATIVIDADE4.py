
# Atividade 4 - Construa um programa onde o usuário digitará a função que ele pode exercer em um jogo de futebol. 
# Se a resposta for "goleiro", "zagueiro" ou "lateral", exibir "Defesa!"; se a resposta for “ala”, "volante" ou "meia", exibir "Meio-Campo!"; 
# se a resposta for "ponta", "atacante" ou "centroavante", exibir "Ataque!". 
# Para qualquer outra resposta, exibir "Teimoso!"."​

print("Informe a função que deseja exercer: ")
FUNCAO = input() # imputando a função...

if FUNCAO == "goleiro" or FUNCAO == "zagueiro" or FUNCAO == "lateral": # caso essas funções forem inseridas...
    print("Defesa!")
elif FUNCAO == "ala" or FUNCAO == "volante" or FUNCAO == "meia": # caso essas funções forem inseridas...
    print("Meio-Campo!")
elif FUNCAO == "ponta" or FUNCAO == "atacante" or FUNCAO == "centroavante": # caso essas funções forem inseridas...
    print("Ataque!")
else: # caso nenhuma das opções seja inserida...
    print("Teimoso!")
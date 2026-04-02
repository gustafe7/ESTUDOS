# 3 - ATIVIDADE: Construa um programa que permita a criação de uma lista de afazeres, 
# totalizando a descrição de 5 tarefas diferentes.
#  A seguir, o programa irá perguntar se a primeira tarefa já foi executada. 
# Se sim, o programa deverá excluí-la, além de dar a opção de cadastrar uma nova tarefa.

TAREFAS = []

for X in range(0, 5):
    FAZER = input(f"Digite a {X+1}ª tarefa: ")
    TAREFAS.append(FAZER)

print("\nSegue a lista de tarefas:")
for Y in TAREFAS:
    print(Y)    

while True:
    print("\nEis, a tarefa que está no topo da lista: ")
    print(TAREFAS[0])
    CONCLUIU = input("Você concluiu essa tarefa? (s/n) ")
    if CONCLUIU.lower() == 's':
        del TAREFAS[0]
        FAZER = input("Digite a próxima tarefa: ")
        TAREFAS.append(FAZER)
    else:
        break
print("\nSegue a lista atualizada de tarefas:")
for Y in TAREFAS:
    print(Y)    
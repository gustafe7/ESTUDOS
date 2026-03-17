#1 - ATIVIDADE: “Criar um programa que possibilite calcular o valor fatorial de um número registrado pelo usuário. 
# Para fins de validação, este valor não poderá ser menor que 0 e nem maior que 25.​

X = int(input("Digite um número para calcular o fatorial (entre 0 e 25): ")) # imputando valor de X...  
if X < 0 or X > 25: # Verificando se o valor de X é menor que 0 ou maior que 25...
    print("Valor inválido. Por favor, digite um número entre 0 e 25.") # Imprimindo mensagem de erro...
else:
    fatorial = 1
    for i in range(1, X + 1):
        fatorial *= i
    print(f"O fatorial de {X} é {fatorial}.")
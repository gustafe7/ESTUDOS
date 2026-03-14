# Demonstração de Match/Case...

print("\n=== AVALIAÇÃO ===\n")
# menu
print("Digite um número referente ao estado da Moeda")
print("1. Flor de Cunho")
print("2. Soberba")
print("3. Muito bem conservada")
print("4. Bem conservada")
print("5. Outros estados")
ESTADO = int(input()) # imputando o estado...

match ESTADO:
    case 1: # caso seja 1...
       print("Perfeita! Vou pagar R$ 1.000.000,00!")
    case 2: # caso seja 2...
        print("Quase perfeita! Ofereço R$ 250.000,00!")
    case 3: # caso seja 3...
        print("Que ótimo! Posso dar uns R$ 100.000,00!")
    case 4: # caso seja 4...
        print("Que bom. Aceitaria R$ 30.000,00?")
    case 5: # caso seja 5...
        print("Desculpe, não aceito neste estado.")
    case _: # caso não seja nenhuma das opcoes do menu...
        print("Opção não reconhecida.")

 
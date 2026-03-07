# Demonstração de IF/ELSE...
print("Digite sua idade: ")
IDADE = int(input())

#SE..
if IDADE < 18:
 print("Você não é maior de idade")
 print("Não poderá realizar operações bancárias!")
#SE NÃO..
elif IDADE <= 65:
  print("Public")
  print("Poderemos oferecer suporte técnico...")
#ENTÃO..
else:
 print("Você é idoso(a)")

print("Obrigado por escoher nossos serviços!")
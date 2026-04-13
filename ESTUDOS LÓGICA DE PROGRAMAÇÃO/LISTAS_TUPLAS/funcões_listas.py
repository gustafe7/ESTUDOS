# Demonstração de funções em listas...
print("Eis, os meus maiores sonhos...")
SONHOS = ["1. Me divertir na Disney",
          "2. Me banhar na praia de Copacabana",
          "3. Tirar férias em Paris",
          "4. Fazer compras no WestShopping",
          "5. Ver as piramides do Egito"]
for X in SONHOS:
    print(X)

print("Ops, não quero Copacabana!")
del(SONHOS[1])
print("E nem WestShopping!") 
del(SONHOS[3])

print("Conferindo os sonhos...")
for X in SONHOS:
    print(X)
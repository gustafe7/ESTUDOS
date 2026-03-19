# Demonstração do uso de funções...

def APRESENTAR():
    print(f"Meu nome é {MyName}")
    print(f"Minha altura é de {MyHeigh} metros.")
    print(f"Minha idade é {MyAge} anos.")
    return
def CONFERIR(X):
    if X >= 18:
        print("Você é maior de idade!")
    else:
        print("Ops, menor de idade não pode!")

MyName = str(input("Digite seu nome: "))
MyHeigh = float(input("Digite sua altura: "))
MyAge = int(input("Digite a sua idade: "))

APRESENTAR()
CONFERIR(MyAge)
APRESENTAR()
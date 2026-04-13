# 1 - ATIVIDADE: Construa um programa onde o usuário digitará a sua idade. 
# Se a idade for menor de 18 anos, o programa entrará em uma função listando nomes de programas infantis. 
# Caso seja maior de idade, entrará em uma outra função com lista de carros e seus respectivos preços.

X = int(input("Digite a sua idade: ")) # imputando idade...
def PROGRAMAS(): 
    print("SÁBADO ANIMADO")
    print("TV GLOBINHO")
    print("DISNEY CHANNEL")
    print("CARTOON NETWORK")
    print("CHAVES")
    print("GLOOB")

def CARROS():
    print("RENAULT STEPWAY 1.0 - 81.000,00")
    print("ONIX 1.0 - 80.000,00")
    print("HB20 1.0 - R$ 79.500,00 ")
    print("ARGO 1.0 - R$ 78.600,00")
    print("CITROEN C3 1.0 - 70.000,00 ")
    print("FIAT MOBI 1.0 - 69.000,00")
    print("RENAULT KWID 1.0 - 68.200,00 ")

if X < 18: # se a idade for menor que 18 anos chama a função PROGRAMAS...
    PROGRAMAS()
else: # se a idade for maior que 18 anos chama a função CARROS ...
    CARROS()
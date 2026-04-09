'''
Crie uma classe chamada `Dog`
¨ Adicione um método `__init__` com parâmetros `name` e `age`, e armazene-os como propriedades usando `self`
¨ Adicione um método chamado `bark ` que imprime o nome do cachorro seguido de "diz Woof!"
¨ Crie um objeto `d1` da classe `Dog` com o nome "Buddy" e idade 3
¨ Chame o método `bark` em d1
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name, "diz Woof!")
    
d1 = Dog("Buddy", 3)
d1.bark()
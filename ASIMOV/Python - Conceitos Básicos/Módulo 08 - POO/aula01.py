class Circle:
    def __init__(self, radius = 1) -> None:
        self.radius = radius
    
    def calculate_area(self):
        return self.radius * self.radius * 3.14

    def get_radius(self):
        return self.radius

class Animal:
    def __init__(self) -> None:
        print('Animal Criado')
    
    def quem_sou_eu(self):
        print('Eu sou um animal')
    
    def comer(self):
        print('Comendo')
    
class Cachorro(Animal):
    def __init__(self):
        super().__init__()
        print('Eu sou um cachorro')
    
    def quem_sou_eu(self):
        print('Eu sou um cachorro')
        
# c1 = Circle()
# c2 = Circle(2)

# print(c1.calculate_area())
# print(c2.calculate_area())
        
a1 = Animal()
dog = Cachorro()

a1.quem_sou_eu()
dog.quem_sou_eu()
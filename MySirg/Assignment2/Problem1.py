class Person:
    def __init__(self, name=None, age=None):
        self.name=name
        self.age=age
    
    def show(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

p1=Person('Soumen', 21)
p2=Person('Bijen', 22)

p1.show()
p2.show()

class Auto:
    brand = ''
    age = 0
    color = ''
    mark = ''
    weight = ''

    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight


    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        Auto.age = +1






class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

class Car(Auto):
    def __init__(self,brand, age, color, mark, weight):
        super().__init__(brand, age, color, mark, weight)



Auto.move(print)
Auto.stop(print)
class Auto:
    brand = ''
    age = 0
    color = ''
    mark = ''
    weight = ''

    def __init__(self, brand: str, age: int, mark: str):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        Auto.age = +1



Auto.move(print)
Auto.stop(print)

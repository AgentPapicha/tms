import random


class RandomValueIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            self.count += 1
            return random.randint(1, 100)
        else:
            print('Iterator is stopped!')
            raise StopIteration


class RandomValue:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return RandomValueIterator(self.limit)


random_values = RandomValue(50)
for value in random_values:
    print(value)
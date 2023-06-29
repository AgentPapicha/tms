import random

class RandomValueIterator:
    def __init__(self, limit, start, stop):
        limit = 1
        self.limit = limit
        start = 1
        stop = 100
        self.start = start
        self.stop = stop
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count = self.count + 1
            return random.randint(self.start, self.stop)
        else:
            print('iterator is stopped')
            raise StopIteration

class RandomValue:
    def __init__(self, limit, start, stop):
        self.limit = limit
        self.start = start
        self.stop = stop

    def __iter__(self):
        return RandomValueIterator(self.limit, self.start, self.stop)



my_random = RandomValue(1, 1, 100)
results = [elem for elem in my_random]
print(results)


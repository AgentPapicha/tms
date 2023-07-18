import random
class RandomValue:
    def __init__(self, limit, *args):
        self._list = list(args)
        self._size = range(100)
        self.limit = limit

    def __str__(self):
        return f"MyList object: {self._list}"


    def __iter__(self):
        self.count = 0
        for _ in self._size:
            if self.count < self.limit:
                self.count += 1
                yield random.randint(1, 100)


my_limit = int(input("Введите лимит: "))
my_random = RandomValue(limit=my_limit)

results = [elem for elem in my_random]
print(results)


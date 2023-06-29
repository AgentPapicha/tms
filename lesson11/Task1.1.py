class RandomValue:
    def __init__(self, *args):
        self._list = list(args)

    def __str__(self):
        return f"MyList object: {self._list}"

    def __iter__(self):
        """
        Метод __iter__ возващает ссылку на Объект-Итератор, класс которого реализован ниже
        """
        return RandomValueIterator(self._list)
    """Your implementation here"""

class RandomValueIterator:
    def __init__(self, RandomValueIterator):
        self.RandomValueIterator = RandomValueIterator  # неизменнно с момента инициализации
        self._size = range(100)
        for i in RandomValueIterator:
            yield i
        #self._size = len(self.RandomValueIterator)  # неизменнно с момента инициализации
        self._curr_index = 0  # увеличивается на 1 при каждом вызове __next__!

    def __iter__(self):
        return self

    """Your implementation here"""


my_limit = int(input("Введите лимит: "))
my_random = RandomValue(limit=my_limit)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None